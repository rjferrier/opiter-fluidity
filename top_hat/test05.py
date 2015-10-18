"""
Bonus exercise: since we haven't done anything with the mesh yet,
go back to non-adaptivity and try three different mesh resolutions for
two different discretisations.
""" 
from test00 import test00
from base import cg, dg, cv
import opiter

class test05(test00):
    pass

root = opiter.OptionsArray('case_name', [test05])
discr = opiter.OptionsArray('discretisation', [cg, cv])

# here we'll use a tag to signal to the mesh_name item that it needs
# to include variations in dx, and we'll use name_format to make the
# names of those variations filename-friendly (i.e. remove the points)
dx = opiter.OptionsArray('dx', [0.00625, 0.0125, 0.025],
                         name_format=lambda dx: str(dx).replace('.', 'p'),
                         tags=['mesh'])

mesh_tree = root * dx
sim_tree = root * discr * dx
