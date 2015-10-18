import os

bin_prefix = os.getenv('FLUIDITYPATH') + '/bin/'
mesher = bin_prefix + 'interval'
simulator = bin_prefix + 'fluidity'

class admin:
    template_dir = 'templates'
    geo_template_filename = 'line.geo.template'
    
    def mesh_name(self):
        # use the get_string method with a tag ('mesh') to pick up
        # variants affecting the resulting mesh (e.g. 'dx')
        return 'line' + self.get_string(only=['mesh'])
        
    def geo_filename(self):
        return self.mesh_name + '.geo'
    
    def mesh_filename(self):
        return self.mesh_name + '.msh'

    def meshing_args(self):
        return [mesher, '--dx='+str(self.dx), '--reverse',
                '0', str(self.domain_length), self.mesh_name]

    def simulation_name(self):
        # all variations affect the resulting simulation, so use
        # get_string with no tags specified
        return self.get_string()
    
    def sim_options_filename(self):
        return self.simulation_name + '.flml'

    def simulation_args(self):
        return [simulator, self.sim_options_filename]

    def simulation_prerequisites(self):
        return [simulator, self.mesh_filename, self.sim_options_filename]
    

class meshing:
    domain_length = 3.0
    dx = 0.025
    def nx(self):
        return int(self.domain_length / self.dx)

    
class simulation:
    mesh_adaptivity = False
    enable_gradation = True
    interpolation_error_bound = 1.0e-2
    
class cg:
    sim_options_template_filename = 'cg.flml.template'
    tracer_mesh_name =  "CoordinateMesh"
    courant_number_name =  "CFLNumber"


class dg:
    sim_options_template_filename = 'dg.flml.template'
    tracer_mesh_name =  "DGMesh"
    courant_number_name =  "DG_CourantNumber" 


class cv:
    sim_options_template_filename = 'cv.flml.template'
    tracer_mesh_name =  "CoordinateMesh"
    courant_number_name =  "ControlVolumeCFLNumber"

