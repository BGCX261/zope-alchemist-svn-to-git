##############################################################################
#
# Copyright (c) 2006 Zope Foundation and Contributors.
# All Rights Reserved.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#
##############################################################################
"""Five baseclasses for zope.formlib.form

$Id: formbase.py 113602 2010-06-18 06:28:38Z ctheune $
"""
import os.path

from datetime import datetime
import Acquisition

import zope.event
import zope.formlib
import zope.app.event.objectevent
from zope import interface
from zope.formlib import interfaces, form, namedtemplate
from zope.app.i18n import ZopeMessageFactory as _

from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from Products.Five.browser.decode import processInputs, setPageEncoding

_FORMLIB_DIR = os.path.dirname(zope.formlib.__file__)
_PAGEFORM_PATH = 'pageform.pt'
_SUBPAGEFORM_PATH = os.path.join(_FORMLIB_DIR, 'subpageform.pt')


class FiveFormlibMixin(Acquisition.Explicit):

    # Overrides the formlib.form.FormBase.template attributes implemented 
    # using NamedTemplates. NamedTemplates using ViewPageTemplateFile (like
    # formlib does by default) cannot work in Zope2.

    # XXX Maybe we need to have Five-compatible NamedTemplates?

    template = ViewPageTemplateFile(_PAGEFORM_PATH)

    # Overrides formlib.form.FormBase.update. Make sure user input is
    # decoded first and the page encoding is set before proceeding.

    def update(self):
        processInputs(self.request)
        setPageEncoding(self.request)
        super(FiveFormlibMixin, self).update()


class FormBase(FiveFormlibMixin, form.FormBase):
    pass


class EditFormBase(FiveFormlibMixin, form.EditFormBase):

    # Overrides formlib.form.EditFormBase.handle_edit_action, to remove
    # dependecy on request.locale
    
    @form.action(_("Apply"), condition=form.haveInputWidgets)
    def handle_edit_action(self, action, data):
        if form.applyChanges(
            self.context, self.form_fields, data, self.adapters):

            zope.event.notify(
                zope.app.event.objectevent.ObjectModifiedEvent(self.context)
                )
            # TODO: Needs locale support. See also Five.form.EditView.
            self.status = _(
                "Updated on ${date_time}", 
                mapping={'date_time': str(datetime.utcnow())}
                )
        else:
            self.status = _('No changes')


class DisplayFormBase(FiveFormlibMixin, form.DisplayFormBase):
    pass


class AddFormBase(FiveFormlibMixin, form.AddFormBase):
    pass


class PageForm(FormBase):

    interface.implements(interfaces.IPageForm)

Form = PageForm


class PageEditForm(EditFormBase):

    interface.implements(interfaces.IPageForm)

EditForm = PageEditForm


class PageDisplayForm(DisplayFormBase):

    interface.implements(interfaces.IPageForm)

DisplayForm = PageDisplayForm


class PageAddForm(AddFormBase):

    interface.implements(interfaces.IPageForm)

AddForm = PageAddForm


class SubPageForm(FormBase):

    template = ViewPageTemplateFile(_SUBPAGEFORM_PATH)

    interface.implements(interfaces.ISubPageForm)


class SubPageEditForm(EditFormBase):

    template = ViewPageTemplateFile(_SUBPAGEFORM_PATH)

    interface.implements(interfaces.ISubPageForm)


class SubPageDisplayForm(DisplayFormBase):

    template = ViewPageTemplateFile(_SUBPAGEFORM_PATH)

    interface.implements(interfaces.ISubPageForm)
