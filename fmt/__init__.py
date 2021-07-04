# -*- coding: utf-8 -*-
"""
f-strings(Python 3.6) style literal string interpolation.
"""

from __future__ import absolute_import

import sys

from .fmt import Fmt

version = __version__ = '0.3.1'
version_info = [int(num) for num in version.split('.')]
__author__ = 'damnever (X.C Dong)'
__email__ = 'dxc.wolf@gmail.com'
__license__ = 'The BSD 3-Clause License'

f = Fmt()
