"""
Table Definitions for database structure

$Id: schema.py 122 2006-11-25 23:38:13Z hazmat $
"""

from sqlalchemy import *
from ore.alchemist.metadata import ZopeBoundMetaData
from db import database

__all__ = ['rdb_schema', 'PersonTable', 'AddressTable']

rdb_schema = ZopeBoundMetaData(database)

AddressTable = Table(
    'Addresses',
    rdb_schema,
    autoload = True
    )

# incidentally if we autoload person table first sqlalchemy will autoload addrreesses becaues
# of the fk relationship. so we could just use the below.. but we won't have an addressable
# table, though its retrievable from the metadata.

StateTable = Table(
    'States',
    rdb_schema,
    autoload = True
    )

PersonTable = Table(
    'Persons',
    rdb_schema,
    autoload = True 
    )


