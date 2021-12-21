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
# Cristian Ciupitu, Eau de Web

# Zope imports
from Globals import InitializeClass
from DateTime import DateTime

# Product imports
from Products.PageTemplates.PageTemplateFile import PageTemplateFile
from Products.NaayaWidgets.Widget import Widget, WidgetError, manage_addWidget


def addDateWidget(container, id="", title="Date Widget", REQUEST=None,
                  **kwargs):
    """ Contructor for Date widget"""
    return manage_addWidget(DateWidget, container, id, title, REQUEST,
                            **kwargs)


class DateWidget(Widget):
    """Date Widget"""

    meta_type = "Naaya Date Widget"
    meta_label = "Date"
    meta_description = "A valid date chosen by the user"
    meta_sortorder = 200
    icon_filename = 'widgets/www/widget_date.gif'

    _properties = Widget._properties + ()

    # Constructor
    _constructors = (addDateWidget,)
    render_meth = PageTemplateFile('zpt/widget_date.zpt', globals())

    def getDatamodel(self, form):
        """Get datamodel from form"""
        value = form.get(self.getWidgetId(), None)
        if not value:
            return None
        try:
            day, month, year = [int(i) for i in value.strip().split('/')]
            value = DateTime(year, month, day)
        except Exception:
            raise WidgetError(('Invalid date string for "${title}"',
                               {'title': self.title}))
        return value


InitializeClass(DateWidget)


def register():
    return DateWidget
