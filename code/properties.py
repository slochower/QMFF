import pytraj as pt
import numpy as np
import scipy as sc

def get_density(parameter_file, trajectory_file, experimental, debug=True):
    '''
    This is a sample objective function, returning the absolute difference between
    the target density, obtained from a simulation given by the input parameters,
    and the reference density. 
    '''
    pt_trajectory = pt.iterload(trajectory_file, parameter_file)
    # 1.66 gram per amu
    density_mean = np.mean((np.sum(pt_trajectory.topology.mass) * 1.660539040) /
                       pt.volume(pt_trajectory))
    density_sem = sc.stats.sem((np.sum(pt_trajectory.topology.mass) * 1.660539040) /
                       pt.volume(pt_trajectory))
    if debug:
        # print('Density = {} +/- {}'.format(density_mean, density_sem))
    
    return abs(experimental - density_mean)