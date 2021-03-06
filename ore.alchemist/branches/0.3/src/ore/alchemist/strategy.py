##################################################################
#
# (C) Copyright 2006 ObjectRealms, LLC
# All Rights Reserved
#
# This file is part of Alchemist.
#
# Alchemist is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# Alchemist is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with CMFDeployment; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
##################################################################
"""
zope sqlalchemy strategy

for now just utilize the thread local

$Id: strategy.py 118 2006-11-24 14:54:13Z hazmat $
"""

from sqlalchemy.engine.strategies import ThreadLocalEngineStrategy, EngineStrategy

class ZopeEngineStrategy( ThreadLocalEngineStrategy ):
    def __init__(self):
        EngineStrategy.__init__(self, 'zope')

ZopeEngineStrategy()    
