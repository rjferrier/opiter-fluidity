#!/usr/bin/env python
import importlib
import sys
import os
import opiter
import postproc


# the first command line arg gives the test case of interest
try:
    case = importlib.import_module(sys.argv[1])
except IndexError:
    # no first arg given
    print "Usage: runner.sh <casename> [pre mesh run plot]"
    sys.exit()

    
# the remaining args form a list of commands
commands = sys.argv[2:]
if len(commands) == 0:
    # default to doing everything 
    commands = ['pre', 'mesh', 'run', 'plot']


if 'pre' in commands:
    # the mesh template is simple enough that we may use Python's built-in
    # template expansion function, which this functor defaults to
    mesh_options_expander = opiter.ExpandTemplate(
        'geo_template_filename', 'geo_filename',
        source_dir_key='template_dir', target_dir_key='case_name')

    opiter.smap(mesh_options_expander, case.mesh_tree,
                message="Expanding geometry files")

    # the simulation options file is more complex; use the Jinja2
    # template engine
    sim_options_expander = opiter.ExpandTemplate(
        'sim_options_template_filename', 'sim_options_filename',
        source_dir_key='template_dir', target_dir_key='case_name',
        engine=opiter.Jinja2TemplateEngine())
    
    opiter.smap(sim_options_expander, case.sim_tree, 
                message="Expanding options files")


if 'mesh' in commands:
    mesh_func = opiter.RunProgram('meshing_args', 'geo_filename', 'mesh_name',
                                  working_dir_key='case_name')

    opiter.pmap(mesh_func, case.mesh_tree, message="Meshing")

    
if 'run' in commands:
    sim_func = opiter.RunProgram(
        'simulation_args', 'simulation_prerequisites', 'simulation_name',
        working_dir_key='case_name')

    opiter.pmap(sim_func, case.sim_tree, message="Running simulations")

    
if 'plot' in commands:
    opiter.smap(postproc.Plot(), case.sim_tree, message="Plotting")

if 'study' in commands:
    conv_func = postproc.StudyConvergence(2.125, 1.0)
    opiter.smap(conv_func, case.sim_tree, message="Calculating convergence")

