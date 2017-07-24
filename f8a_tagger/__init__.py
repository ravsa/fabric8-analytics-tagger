"""Keyword extraction/tagger for fabric8-analytics."""

__version_info__ = ('0', '1')
__version__ = '.'.join(__version_info__)
__title__ = 'fabric8-analytics-tagger'
__author__ = 'Fridolin Pokorny'
__license__ = 'ASL 2.0'
__copyright__ = 'Copyright 2017 Fridolin Pokorny'

from .corpus import Corpus
from .keywords_chief import KeywordsChief
from .tokenizer import Tokenizer