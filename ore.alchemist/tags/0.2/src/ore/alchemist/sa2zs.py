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
SQLAlchemy to Zope3 Schemas

$Id: sa2zs.py 121 2006-11-25 23:22:55Z hazmat $
"""

import sys
from zope.interface import Interface, moduleProvides, directlyProvides
from zope.interface.interface import InterfaceClass
from zope import schema
from zope.schema.interfaces import ValidationError

from zope.component import provideAdapter

from sqlalchemy import types as rt
import sqlalchemy as rdb

from interfaces import ITableSchema, TransmutationException, IAlchemistTransmutation, \
     IModelAnnotation, IIModelInterface

moduleProvides( IAlchemistTransmutation )

class ColumnTranslator( object ):

    def __init__(self, schema_field):
        self.schema_field = schema_field
        
    def extractInfo( self, column, info ):
        d = {}
        d['title'] = unicode( info.get('label', column.name )  )
        d['description'] = unicode( info.get('description', '' ) )
        d['required'] = not column.nullable

        # this could be all sorts of things ...
        if isinstance( column.default, rdb.ColumnDefault ):
            default = column.default.arg
        else:
            default = column.default

        # create a field on the fly to validate the default value... 
        # xxx there is a problem with default value somewhere in the stack
        # 
        validator = self.schema_field()
        try:
            validator.validate( default )
            d['default'] = default
        except ValidationError:
            pass
        
        return d

    def __call__( self, column, annotation ):
        info = annotation.get( column.name, {} )
        d = self.extractInfo( column, info)
        return self.schema_field( **d )

class SizedColumnTranslator( ColumnTranslator ):

    def extractInfo( self, column, info ):
        d = super( SizedColumnTranslator, self).extractInfo( column, info )
        d['max_length'] = column.type.length
        return d
        

class ColumnVisitor( object ):

    column_type_map = [
        ( rt.Float,  ColumnTranslator( schema.Float )   ),
        ( rt.SmallInteger, ColumnTranslator( schema.Int ) ),
        ( rt.Date, ColumnTranslator( schema.Date ) ),
        ( rt.DateTime, ColumnTranslator( schema.Datetime ) ),
#        ( rt.Time, ColumnTranslator( schema.Datetime ),
        ( rt.Boolean, ColumnTranslator( schema.Bool ) ),
        ( rt.String, SizedColumnTranslator( schema.TextLine ) ),
        ( rt.Binary, ColumnTranslator( schema.Bytes ) ),
        ( rt.Unicode, SizedColumnTranslator( schema.Bytes ) ),
        ( rt.Numeric, ColumnTranslator( schema.Float ) ),
        ( rt.Integer,  ColumnTranslator( schema.Int ) )
        ]

    def __init__(self, info ):
        self.info = info or {}

    def visit( self, column ):
        column_handler = None
        
        for ctype, handler in self.column_type_map:
            if isinstance( column.type, ctype ):
                if isinstance( handler, str ):
                    # allow for instance method customization
                    handler = getattr( self, handler )
                column_handler = handler

        if column_handler is None:
            raise TransmutationException("no column handler for %r"%column)

        return column_handler( column, self.info )


class SQLAlchemySchemaTranslator( object ):

    def translate( self, table, annotation, __module__, **kw):

        annotation = annotation or {}
        visitor = ColumnVisitor(annotation)
        iname ='I%sTable'%table.name

        d = {}
        order_max = 0
        for column in table.columns:
            if annotation.get( column.name, {}).get('omit', False ):
                continue
            d[ column.name ] = visitor.visit( column )
            order_max = max( order_max, d[ column.name ].order )
        if 'properties' in kw:
            for name, field in kw['properties'].items():
                # append new fields
                if name not in d:
                    order_max = order_max + 1
                    field.order = order_max
                # replace in place old fields
                else:
                    field.order = d[name].order
                d[ name ] = field

        DerivedTableSchema = InterfaceClass( iname,
                                             (ITableSchema,),
                                             attrs=d,
                                             __module__ = __module__ )

#        pprint.pprint(schema.getFieldsInOrder( DerivedTableSchema ))
        return DerivedTableSchema
        
def transmute(  table, annotation=None, __module__=None, **kw):

    # if no module given, use the callers module
    if __module__ is None:
        __module__ = sys._getframe(1).f_globals['__name__']

    z3iface = SQLAlchemySchemaTranslator().translate( table,
                                                      annotation,
                                                      __module__,
                                                      **kw )

    # mark the interface itself as being model driven
    directlyProvides( z3iface, IIModelInterface)
        
    # provide a named annotation adapter to go from the iface back to the annotation
    if annotation is not None:
        name = "%s.%s"%(z3iface.__module__, z3iface.__name__)
        provideAdapter( annotation, adapts=(IIModelInterface,), provides=IModelAnnotation, name = name )

    return z3iface
