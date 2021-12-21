# The contents of this file are subject to the Mozilla Public
# License Version 1.1 (the "License"); you may not use this file
# except in compliance with the License. You may obtain a copy of
# the License at http://www.mozilla.org/MPL/
#
# Software distributed under the License is distributed on an "AS
# IS" basis, WITHOUT WARRANTY OF ANY KIND, either express or
# implied. See the License for the specific language governing
# rights and limitations under the License.
#
# The Initial Owner of the Original Code is European Environment
# Agency (EEA).  Portions created by Finsiel Romania and Eau de Web are
# Copyright (C) European Environment Agency.  All
# Rights Reserved.
#
# Authors:
#
# Alin Voinea, Eau de Web
# Cristian Ciupitu, Eau de Web

# Zope imports
from Products.PageTemplates.PageTemplateFile import PageTemplateFile
from Globals import InitializeClass

# Product imports
from Products.NaayaWidgets.Widget import manage_addWidget, WidgetError

from MatrixWidget import MatrixWidget


def addCheckboxMatrixWidget(container, id="", title="CheckboxMatrix Widget",
                            REQUEST=None, **kwargs):
    """ Contructor for CheckboxMatrix widget"""
    return manage_addWidget(CheckboxMatrixWidget, container, id, title,
                            REQUEST, **kwargs)


class CheckboxMatrixWidget(MatrixWidget):
    """ CheckboxMatrix Widget """

    meta_type = "Naaya Checkbox Matrix Widget"
    meta_label = "Checkbox matrix"
    meta_description = ("Group of multiple choice questions with multiple "
                        "answers per row")
    meta_sortorder = 501
    icon_filename = 'widgets/www/widget_checkboxmatrix.gif'

    _properties = MatrixWidget._properties + ()

    # Constructor
    _constructors = (addCheckboxMatrixWidget,)
    render_meth = PageTemplateFile('zpt/widget_checkboxmatrix.zpt', globals())

    def getChoices(self, REQUEST=None, anyLangNonEmpty=False):
        return super(CheckboxMatrixWidget, self).getChoices(
            anyLangNonEmpty=anyLangNonEmpty)

    def getDatamodel(self, form):
        """Get datamodel from form"""
        widget_id = self.getWidgetId()
        value = []
        for i in range(len(self.rows)):
            row_value = form.get('%s_%d' % (widget_id, i), [])
            row_value = [int(x) for x in row_value]
            value.append(row_value)
        return value

    def validateDatamodel(self, value):
        """Validate datamodel"""
        if not self.required:
            return
        unanswered = [x for x in value if not x]
        if unanswered:
            raise WidgetError(('Value required for "${title}"',
                               {'title': self.title}))

    def get_value(self, datamodel=None, **kwargs):
        """ Return a string with the data in this widget """
        if datamodel is None:
            return self._get_default_value()
        res = []
        for index, row_answers in enumerate(datamodel):
            title = self.rows[index]
            value = []
            if not row_answers:
                res.append('%s: -' % title)
                continue
            for answer in row_answers:
                value.append(self.choices[answer])
            value = ', '.join(value)
            res.append('%s: %s' % (title, value))
        return '\n'.join(res)


InitializeClass(CheckboxMatrixWidget)


def register():
    return CheckboxMatrixWidget
