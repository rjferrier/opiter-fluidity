from opiter.utilities import SerialFunctor, Success, Failure

import os
import vtktools
import numpy as np
import matplotlib.pyplot as plt


def get_filename(options, n):
    return '{}/{}_{}.vtu'.format(
        options.case_name, options.simulation_name, n)


def monotonic(x, f):
    isort = sorted(range(len(x)), key=lambda i: x[i])
    x = np.array([x[i] for i in isort])
    f = np.array([f[i] for i in isort])
    return x, f


class Plot(SerialFunctor):
    def preamble(self, options):
        plt.clf()

    def __call__(self, options):
        stem = '{}/{}'.format(options.case_name, options.simulation_name)
        # get the last dump file
        n = 0
        while os.path.isfile(get_filename(options, n + 1)):
            n += 1
        # load results and plot
        vtu_obj = vtktools.vtu(get_filename(options, n))
        x = vtu_obj.GetLocations()[:,0]
        f = vtu_obj.GetScalarField('Tracer')
        x, f = monotonic(x, f)
        plt.plot(x, f, label=options.simulation_name)
        self.print_end(options.simulation_name, options)
        
    def postamble(self, options):
        "This gets called after iteration"
        plt.axis([0.0, 3.0, -0.1, 1.1])
        plt.xlabel('$x$')
        plt.ylabel('Tracer')
        plt.title(options.case_name)
        plt.legend(loc='best')
        plt.show()

        
