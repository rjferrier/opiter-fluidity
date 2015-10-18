"""
Do the third exercise which modifies the CV scheme.
"""
from test01 import mesh_tree, test01
from base import cv
import opiter

# ensure CV options are used
class test04(test01, cv):
    pass

# make two sets of options corresponding to the unmodified and
# modified schemes
class unmod:
    pass

class mod:
    # here we've modified the template as well as the 
    sim_options_template_filename = 'test04_mod.flml.template'

    
root = opiter.OptionsArray('case_name', [test04])

cvsch = opiter.OptionsArray('cvscheme', [unmod, mod])

mesh_tree = root
sim_tree = root * cvsch
