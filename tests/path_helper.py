import sys
import os
from os.path import dirname
from os.path import abspath

# add app path to pythonpath
directory = abspath(dirname(dirname(__file__)))
app_path = os.path.join(directory, 'app')

#path to python path
sys.path.append(app_path)