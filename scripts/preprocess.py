#!/usr/bin/env python

"""
  This file is part of FIRS Industry Set for OpenTTD.
  FIRS is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, version 2.
  FIRS is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
  See the GNU General Public License for more details. You should have received a copy of the GNU General Public License along with FIRS. If not, see <http://www.gnu.org/licenses/>.
"""
from time import time
start = time()

print "[PYTHON] python preprocessing"

import os.path
currentdir = os.curdir

import sys
sys.path.append(os.path.join(currentdir, 'src')) # add to the module search path

import firs

# render the docs
start = time()
import render_nml_nfo
render_nml_nfo.main()
print format((time() - start), '.2f')+'s'

# render the docs
start = time()
import render_docs
render_docs.main()
print format((time() - start), '.2f')+'s'
