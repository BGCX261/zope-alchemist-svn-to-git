##############################################################################
#
# Copyright (c) 2004, 2005 Zope Foundation and Contributors.
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
"""Generic Components ZCML Handlers

$Id: metaconfigure.py 113602 2010-06-18 06:28:38Z ctheune $
"""
from zope.configuration.exceptions import ConfigurationError
from zope.app.component import contentdirective
from Products.Five.security import protectName, initializeClass

class ContentDirective(contentdirective.ContentDirective):

    def __protectName(self, name, permission_id):
        self.__context.action(
            discriminator = ('five:protectName', self.__class, name),
            callable = protectName,
            args = (self.__class, name, permission_id)
            )

    def __protectSetAttributes(self, attributes, permissions):
        raise ConfigurationError('set_attributes parameter not supported.')

    def __proctectSetSchema(self, schema, permission):
        raise ConfigurationError('set_schema parameter not supported.')

    def __mimic(self, _context, class_):
        raise ConfigurationError('like_class parameter not supported.')

    def __call__(self):
        return self.__context.action(
            discriminator = None,
            callable = initializeClass,
            args = (self.__class,)
            )
