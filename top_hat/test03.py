"""
Go back to test01 and, per the second exercise, play around with
mesh adaptivity parameters.  Let's do this only for CG, for brevity.
"""
from test01 import mesh_tree, test01
from base import cg
import opiter

# use the previous root options and ensure CG options are used
class test03(test01, cg):
    pass

root = opiter.OptionsArray('case_name', [test03])

ieb = opiter.OptionsArray('interpolation_error_bound',
                          [0.5e-2, 1.0e-2, 2.0e-2],
                          names=['fine', 'med', 'coarse'])

grad = opiter.OptionsArray('enable_gradation',
                           [True, False],
                           names=['grad', 'nograd'])

mesh_tree = root
sim_tree = root * grad * ieb
