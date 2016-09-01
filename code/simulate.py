import os
import subprocess

def simulate(target, parameter_file):
    '''
    This will write a new run script for each parameter set,
    and then execute it.
    '''
    run_script = '''
    #!/usr/bin/env bash
    source $AMBERHOME/amber.sh
    export CUDA_VISIBLE_DEVICES=1
    export LD_LIBRARY_PATH=/usr/local/cuda-7.5/lib64
    pmemd.cuda -O -p {} -c full.crds -i mdin-10ps -o mdout.001 -r rst.001 -x traj.001 -e mden.001 -inf mdinfo.001
    '''.format(parameter_file)
    file = open('{}/run.sh'.format(target), 'w')
    file.write(run_script)
    file.close()
    try:
        os.chdir(target)
        subprocess.call(['bash', 'run.sh'])
        os.chdir('../../../code/')
    except:
        print('Problem executing the MD run script.')
