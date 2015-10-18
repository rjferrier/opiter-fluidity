"""
This test case reproduces the top hat example from the Fluidity
manual, which considers three discretisations with mesh adaptivity.
""" 

# reuse the mesh from test00
from test00 import test00
from base import cg, dg, cv
import opiter

class test01(test00):
    # the only thing we need to do to the root options is switch
    # mesh_adaptivity on
    mesh_adaptivity = True

root = opiter.OptionsArray('case_name', [test01])
discr = opiter.OptionsArray('discretisation', [cg, dg, cv])

# meshing stays the same; simulations now done with three
# discretisations
mesh_tree = root
sim_tree = root * discr
