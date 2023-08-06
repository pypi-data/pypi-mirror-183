# karray
# copyright 2022, Carlos Gaete-Morales, DIW-Berlin 
"""
    karray
    copyright 2022, Carlos Gaete-Morales, DIW-Berlin 
"""
__version__ = (0, 1, 4)
__author__ = 'Carlos Gaete-Morales'


from .arrays import Long, Array, numpy_to_long, concat, from_feather, _from_feather, pandas_to_array
from .setting import settings