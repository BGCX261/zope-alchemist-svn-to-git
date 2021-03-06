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
"""Test browser resources

$Id: test_resource.py 113602 2010-06-18 06:28:38Z ctheune $
"""
import os, sys
if __name__ == '__main__':
    execfile(os.path.join(sys.path[0], 'framework.py'))

def test_suite():
    import unittest
    from Testing.ZopeTestCase import installProduct, ZopeDocFileSuite
    from Testing.ZopeTestCase import FunctionalDocFileSuite
    installProduct('PythonScripts')  # for Five.tests.testing.restricted
    return unittest.TestSuite((
            ZopeDocFileSuite('resource.txt',
                             package='Products.Five.browser.tests'),
            FunctionalDocFileSuite('resource_ftest.txt',
                                   package='Products.Five.browser.tests'),
            ))

if __name__ == '__main__':
    framework()
