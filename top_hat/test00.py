"""
A simple test case with basic options.
"""

import base
import opiter

class test00(base.admin, base.meshing, base.simulation, base.cg):
    # inherit a load of base options - that's it
    pass

# Make an array called 'case_name' with test00 as its only node.  This
# gives us a starting dictionary which contains the entry
# {'case_name': 'test00'} in addition to the contents of test01.*
root = opiter.OptionsArray('case_name', [test00])

# just have one mesh and simulation at this stage
mesh_tree = root
sim_tree = root


# *Alternatively, we could have made an orphan node:
# opiter.OptionsNode(test00, node_key='case_name')
