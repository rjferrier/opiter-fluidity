"""
In accordance with the first top hat exercise, play around with CG
stabilisation.
"""
from test01 import mesh_tree, test01
from base import cg
import opiter

# use the previous root options and ensure CG options are used
class test02(test01, cg):
    # we've modified the template
    sim_options_template_filename = 'test02.flml.template'

root = opiter.OptionsArray('case_name', [test02])
stab = opiter.OptionsArray('stabilisation', ['SUPG', 'SU', 'nostab'])

mesh_tree = root
sim_tree = root * stab
