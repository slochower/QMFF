#!/bin/tcsh

setenv CUDA_VISIBLE_DEVICES 0

pmemd.cuda -O -p full.topo -c eq2.rst -o mdout.001 -r rst.001 -x traj.001 -e mden.001 -inf mdinfo.001


