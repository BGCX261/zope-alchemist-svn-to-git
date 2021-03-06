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
"""Initialize the Five product

$Id: __init__.py 113602 2010-06-18 06:28:38Z ctheune $
"""
import Acquisition
from Globals import INSTANCE_HOME

import zcml
import pythonproducts

# public API provided by Five
# usage: from Products.Five import <something>
from browser import BrowserView
from skin.standardmacros import StandardMacros

def initialize(context):
    pythonproducts.setupPythonProducts(context)
    zcml.load_site()
