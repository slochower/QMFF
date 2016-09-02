import subprocess as subprocess

def prepare_simulation_files(target, mdin, coordinate_file, parameter_file):
    '''
    This function copies (or links) files necessary to run a simulation to a destination
    directory.  
    '''
    try:
        subprocess.call(['ln', '-s', '{}'.format(mdin), '{}/'.format(target)])
    except:
        print('Problem linking the MD input file: {}'.format(mdin))
    try:
        subprocess.call(['ln', '-s', '{}'.format(coordinate_file), 
        '{}/'.format(target)])
    except:
        print('Problem linking the coordinate file: {}'.format(coordinate_file)) 
    try:
        subprocess.check_call(['mv', '{}'.format(parameter_file), 
        '{}/'.format(target)])
    except:
        print('Problem moving the parameter file: {}'.format(parameter_file))
    
    return
    