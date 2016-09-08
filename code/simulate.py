import os
import subprocess

def simulate(parameter_file, trajectory_file, debug=False):
    '''
    This will write a new run script for each parameter set,
    and then execute it.
    '''
    run_script = '''
    #!/usr/bin/env bash
    source $AMBERHOME/amber.sh
    export CUDA_VISIBLE_DEVICES=1
    export LD_LIBRARY_PATH=/usr/local/cuda-7.5/lib64
    pmemd.cuda -O -p {} -c full.crds -i mdin-10ps -o mdout.001 -r rst.001 -x {} -e mden.001 -inf mdinfo.001
    '''.format(parameter_file, trajectory_file)
    file = open('run.sh', 'w')
    file.write(run_script)
    file.close()
    try:
        subprocess.call(['bash', 'run.sh'])
    except:
        print('Problem executing the MD run script.')

    # Delete files... 

    # We need some error handling to grep (?) the MD output file for errors.

    # Check for NAN
    # Check for ****
    # Check from TIMING in mdout
    # Restart from previous rst.
    # Add equilibration
    # Cleanup after simulations unless debug=True