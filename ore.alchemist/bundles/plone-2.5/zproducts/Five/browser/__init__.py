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
"""Provide basic browser functionality

$Id: __init__.py 113602 2010-06-18 06:28:38Z ctheune $
"""
import Acquisition
import zope.app.publisher.browser

class BrowserView(Acquisition.Explicit, zope.app.publisher.browser.BrowserView):
    """Five browser view

    Mixes in explicit acquisition so that security can be acquired for
    views"""
