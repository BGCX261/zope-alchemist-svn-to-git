"""
database access definition

$Id: db.py 129 2006-11-27 22:50:41Z hazmat $
"""

from ore.alchemist.engine import get_engine

database = get_engine('mysql://root@localhost/orgperson', encoding='utf-8', convert_unicode=True, echo=True)
