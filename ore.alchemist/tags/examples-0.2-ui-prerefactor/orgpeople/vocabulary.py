"""
Define a vocabulary for states
$Id: vocabulary.py 122 2006-11-25 23:38:13Z hazmat $ 
"""

from ore.alchemist.vocabulary import VocabularyTable
from schema import StateTable

StateVocabulary = VocabularyTable( StateTable, "state_code", "state_name" )
