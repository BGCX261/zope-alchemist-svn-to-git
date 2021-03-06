##############################################################################
#
# Copyright (c) 2005 Zope Foundation and Contributors.
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
"""Test the PTS language integration.

$Id: pts_test_languages.py 113602 2010-06-18 06:28:38Z ctheune $
"""
import os, sys
if __name__ == '__main__':
    execfile(os.path.join(sys.path[0], 'framework.py'))

def test_suite():
    from Testing.ZopeTestCase import installProduct, FunctionalDocFileSuite
    installProduct('Five')
    installProduct('PlacelessTranslationService')
    return FunctionalDocFileSuite('pts_test_languages.txt',
                                  package='Products.Five.browser.tests')

if __name__ == '__main__':
    framework()
