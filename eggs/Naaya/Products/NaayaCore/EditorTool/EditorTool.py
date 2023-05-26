"""
This tool provides an WYSIWYG api for rich content editing with text
formatting, image, multimedia etc. It's used in almost all Naaya content
types.

"""

import re
from copy import deepcopy
from ConfigParser import ConfigParser
from os.path import join, dirname
import simplejson as json

from AccessControl import ClassSecurityInfo
from App.ImageFile import ImageFile
from Globals import InitializeClass
from OFS.Folder import Folder

from Products.NaayaCore.constants import ID_EDITORTOOL, TITLE_EDITORTOOL
from Products.NaayaCore.constants import METATYPE_EDITORTOOL
from Products.NaayaCore.EditorTool.utilities import parse_css_margin
from Products.NaayaCore.EditorTool.utilities import parse_css_border_width
from Products.NaayaCore.EditorTool.utilities import strip_unit
from Products.NaayaCore.EditorTool.config import SECTIONS
from naaya.core.zope2util import url_quote
from Products.PageTemplates.PageTemplateFile import PageTemplateFile
from naaya.core.StaticServe import StaticServeFromZip


TINY_MCE_PATH = '{base_url}/tinymce/js/tinymce'


def manage_addEditorTool(self, REQUEST=None):
    """ ZMI method that creates an EditorTool object instance
        into the portal"""
    ob = EditorTool(ID_EDITORTOOL, TITLE_EDITORTOOL)
    self._setObject(ID_EDITORTOOL, ob)
    if REQUEST:
        return self.manage_main(self, REQUEST, update_menu=1)


def loadConfig(section='tinymce', SECTIONS=SECTIONS):
    """ Loads the default configuration from *config.py*.
    The configuration is loaded from the *config.py* file.
    `section` Section to load from config.py. You can use config.py
    to create multiple templates for the editor and name them differently.
    Returns a dictionary with tinymce configuration options
    """
    return deepcopy(SECTIONS.get(section, dict()))

configuration = loadConfig()  # Global configuration loaded from *config.py*


class EditorTool(Folder):
    """ **EditorTool** installs itself into the portal and provides rich text
        editing capabilities attachable via to HTML input elements such as
        textarea.
        It uses *TinyMCE* (http://tinymce.moxiecode.com/) editor.
        Please see README.txt located into this module for notes
    """

    meta_type = METATYPE_EDITORTOOL
    icon = 'misc_/NaayaCore/EditorTool.gif'
    manage_options = (Folder.manage_options)
    security = ClassSecurityInfo()

    def __init__(self, id, title):
        """ Initialize variables"""
        self.id = id
        self.title = title

    def getConfiguration(self):
        """ Return current default configuration """
        return configuration

    def includeLibs(self, lang=None):
        """ Returns HTML code that includes required JavaScript libraries.
        Parameters:

            `lang`
                **Not used**
        """

        return (
            '<script type="text/javascript" language="javascript" '
            'src="{path}/jquery.tinymce.min.js"></script>'
        ).format(path=TINY_MCE_PATH.format(base_url=self.absolute_url()))

    security.declarePublic('additional_styles')

    def additional_styles(self):
        """
        Returns the additional naaya styles to be displayed in tinymce
        """
        ret = ''

        # insert other styles here

        styleselect = self._get_styleselect_styles()
        if styleselect is not None:
            ret += styleselect

        # custom local syles. Add a DTML Document called "custom_css" inside
        # portal_editor to benefit from this.
        custom = self.get('custom_css')
        if custom:
            ret += custom(self.REQUEST)

        self.REQUEST.RESPONSE.setHeader('Content-Type', 'text/css')
        return ret

    def _get_styleselect_styles(self):
        """
        Returns the styles to use for styleselect listing inside tinymce
        Searches the current style objects for the specific format
        /*BEGIN-TINYMCE-STYLESELECT*/
        ...
        selector { style }
        ...
        /*END-TINYMCE-STYLESELECT*/
        """
        style_objects = self.getLayoutTool().getCurrentStyleObjects()
        for so in style_objects:
            text = so()
            match = re.search(
                '/\\*BEGIN-TINYMCE-STYLESELECT\\*/(.*?)'
                '/\\*END-TINYMCE-STYLESELECT\\*/', text, re.S)
            if match is not None:
                return match.group(1)
        return None

    def _add_styleselect_to_cfg(self, cfg):
        """
        Adds a style select box to the front of the first row of buttons
        if it can find the styles file it needs
        if not it does nothing

        the format for the styles is
        /*BEGIN-TINYMCE-STYLESELECT*/
        ...
        selector { style }
        ...
        /*END-TINYMCE-STYLESELECT*/
        """
        # get the styles
        text = self._get_styleselect_styles()
        if text is None:
            return

        # find class selectors
        selectors_text = re.sub('{(.|\n)*?}', '', text)
        selectors = re.findall('\\.\w+(?=\s|[,{])', selectors_text)
        selectors = [sel[1:] for sel in selectors]

        # add the button and selectors to it
        cfg['style_formats'].extend([
            dict(title=sel.capitalize(), inline='span', classes=sel)
            for sel in selectors
        ])

    def render(self, element, lang=None, image_support=False,
               extra_options={}):
        """Return the HTML necessary to run the TinyMCE.
        Parameters:

            `element`
                `id` of HTML element that editor will is attached to.
            `lang`
                **Not used**
            `image_support`
                **No longer used** In order to disable images.
                Use extra_options, see below.
            `extra_options`
                Extra options you can pass to tinyMCE editor. See `config.py`
                for further reference. You can pass any option from there
                to override default one.
                `extra_options['config_template']` Loads one of the defined
                templates from `config.py`. Default is 'tinymce'.
                Also you can use 'tinymce_noimage' to disable image insertion.
        """
        doc_url = "/".join(self.aq_parent.getPhysicalPath())

        if hasattr(self, 'custom_config'):
            cfg = loadConfig('tinymce', self.custom_config())
        elif 'config_template' in extra_options:
            section = extra_options['config_template']
            cfg = loadConfig(section)
        else:
            cfg = deepcopy(configuration)

        base_url = self.absolute_url()

        cfg.update({
            'select_image_url': '{0}/select_image?document={1}'.format(
                base_url, doc_url),
            'edit_image_url':
                '{0}/prepare_image?mode=edit&document={1}'.format(
                    base_url, doc_url),
            'link_popup_url': '{0}/select_link'.format(self.absolute_url()),
            'element_id': element,
            'script_url': '{0}/tinymce.min.js'.format(
                TINY_MCE_PATH.format(base_url=self.absolute_url())
            ),
            'site_url': self.getSite().absolute_url(),
            'language': self.gl_get_selected_language(),
        })
        cfg.update(extra_options)
        # romancri 20100420:
        # When using dialects, clobber the dialect. Otherwise, TinyMCE fails
        # because it doesn't have these translation files.
        if 'language' in cfg.keys() and cfg['language']:
            cfg['language'] = cfg['language'].split('-')[0]

        self._add_styleselect_to_cfg(cfg)

        css_url = '/'.join(self.getPhysicalPath()) + '/additional_styles'
        old_css = cfg.get('content_css', '')
        cfg['content_css'] = css_url
        if old_css != '':
            cfg['content_css'] += ',' + old_css

        return (
            '<script type="text/javascript">'
            '$().ready(function() {{'
            '   $("textarea#{element}").tinymce({config});'
            '}});'
            '</script>'
        ).format(element=element, config=json.dumps(cfg, indent=2))

    def get_preview_img(self, REQUEST=None):
        """ Compute src attribute for the preview image. Uploads image if
        requested.
        Returns the URL to the image.
        """
        url = ''
        if 'url' in REQUEST.form:
            url = REQUEST.form['url']
        if 'mode' in REQUEST.form:
            mode = REQUEST.form['mode']
            if mode == 'upload':
                url = self._upload_image(REQUEST)

        if not url.startswith('http') and not url.startswith('/'):
            document = self.getEnclosingDocument(REQUEST)
            if document is not None:
                url = '%s/%s' % (document.absolute_url(), url)

        return url

    def _upload_image(self, REQUEST=None):
        """ Upload an image into the document container. """
        if REQUEST:
            if 'file' in REQUEST.form:
                file = REQUEST.form['file']
                document = self.getEnclosingDocument(REQUEST)
                if document:
                    imageContainer = document.imageContainer
                    uploaded = imageContainer.uploadImage(file, None)
                    return uploaded.absolute_url()
        else:
            print 'no image to upload'

    def enumerateImages(self, source, page=0, query=None, REQUEST=None):
        """ Retrieve the list of images depending on the source.
        Return a list of ``Image`` objects
        """

        def get_image_info(source, image):
            image_object = {
                'url': image.absolute_url(),
                'title': url_quote(to_utf8(image.title_or_id())),
                'source': '',
                'author': ''
            }

            if source == 'album':
                image_object['source'] = url_quote(
                    to_utf8(image.source))
                image_object['author'] = url_quote(
                    to_utf8(image.author))

            return image_object

        ret = []
        if source == 'document':
            document = self.getEnclosingDocument(REQUEST)
            if document:
                ret = document.imageContainer.getImages()
        if source == 'website':
            site = self.getSite()
            ret = site.imageContainer.getImages()
        if source == 'album':
            album_url = REQUEST.form['album']
            if query is None:
                album = self.restrictedTraverse(album_url)
                ret = album.getObjects()
            else:
                ctool = self.getCatalogTool()
                filter_index = ('objectkeywords_' +
                                self.gl_get_selected_language())
                ret_brains = ctool.search(
                    {'path': album_url, 'meta_type': 'Naaya Photo',
                     filter_index: query})
                ret = [x.getObject() for x in ret_brains]

        total_images = len(ret)
        images = ret[(int(page) * 12):((int(page) + 1) * 12)]

        options = {
            'total_images': total_images,
            'images': [get_image_info(source, image) for image in images]
        }

        return json.dumps(options)

    def enumeratePhotoAlbums(self, REQUEST=None):
        """
        Lookup photo galleries from the site.
        Return a list with all photo galleries available within the site.
        """
        ctool = self.getCatalogTool()
        return [x.getObject()
                for x in ctool.search({'meta_type': 'Naaya Photo Folder'})]

    def getEnclosingDocument(self, REQUEST):
        """
        Return the enclosing document where this editor tool
        instance is located.

            `REQUEST`
                Http request that **must** contain the 'document' parameter

        Return enclosing document object
        """
        if 'document' in REQUEST.form:
            document_url = REQUEST.form['document']
            return self.restrictedTraverse(document_url)
        return None

    def prepare_image_styles(self, REQUEST=None):
        """ Parse `REQUEST` and retrieve image attributes to set them into
        preview. This method is called when user selects the image into editor
        and then presses image button to adjust its settings.
        Return a dictionary with found attributes such as border, margin etc.
        """
        ret = {
            'title': self.get_request_param(REQUEST, 'title'),
            'alignment': self.get_request_param(REQUEST, 'left'),
            'css_alignment': '', 'margin': '', 'border_preview': '',
            'width_preview': '', 'height_preview': '', 'border': '',
            'width': '', 'height': '', 'h_margin': '', 'v_margin': '',
        }
        if 'alignment' in REQUEST.form:
            alignment = REQUEST.form['alignment']
            if alignment:
                if alignment == 'left' or alignment == 'right':
                    ret['css_alignment'] = 'float: %s' % alignment
                else:
                    ret['css_alignment'] = 'vertical-align: %s' % alignment
        if 'margin' in REQUEST.form:
            ret['margin'] = 'margin: %s' % REQUEST.form['margin']
        if 'border' in REQUEST.form:
            ret['border_preview'] = 'border: %s' % REQUEST.form['border']
            ret['border'] = parse_css_border_width(REQUEST.form['border'])
        if 'width' in REQUEST.form:
            ret['width_preview'] = 'width: %s' % REQUEST.form['width']
            ret['width'] = strip_unit(REQUEST.form['width'])
        if 'height' in REQUEST.form:
            ret['height_preview'] = 'height: %s' % REQUEST.form['height']
            ret['height'] = strip_unit(REQUEST.form['height'])
        if REQUEST and 'margin' in REQUEST.form:
            margins = parse_css_margin(REQUEST.form['margin'])
            ret['h_margin'] = margins[0]
            ret['v_margin'] = margins[1]
        return ret

    def get_request_param(self, REQUEST, name, default=''):
        """ Safely retrieve a parameter from request
        Parameters:

        `REQUEST`
            Http request
        `name`
            Name of the parameter
        `default`
            Default value to return if parameter not found. If not specified
            is empty string.

        Return the parameter or default if none found.
        """
        if name in self.REQUEST:
            return self.REQUEST.form[name]
        return default

    def isImageContainer(self, document):
        """ Verifies document if is image container or inherits the
        imageContainer of NySite.
        Parameters:

            `document`
                Document to be checked.

        Return ``true`` if document has its own instance of `imageContainer`
        """
        return self.getSite().imageContainer != document.imageContainer

    image_js = ImageFile('www/image.js', globals())
    link_js = ImageFile('www/link.js', globals())
    image_css = ImageFile('www/image.css', globals())
    tinymce = StaticServeFromZip('tinymce', 'www/tinymce.zip', globals())
    tinymce_naaya = StaticServeFromZip(
        'Naaya', 'www/tinymce_naaya.zip', globals())
    select_image = PageTemplateFile('zpt/select_image', globals())
    select_image_size = PageTemplateFile('zpt/select_image_size', globals())
    prepare_image = PageTemplateFile('zpt/prepare_image', globals())
    select_link = PageTemplateFile('zpt/select_link', globals())

InitializeClass(EditorTool)


def to_utf8(string):
    try:
        string.decode('utf-8')
        return string
    except UnicodeEncodeError:
        return string.encode('utf-8')
