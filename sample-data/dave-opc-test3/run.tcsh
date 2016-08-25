#!/bin/tcsh

setenv CUDA_VISIBLE_DEVICES 2
set i = 0
while ($i <= 500)
  @ j = $i + 1
  pmemd.cuda -O -p full.topo -c rst.npt.$i -i mdin-nve -o mdout.nve.$j -r rst.nve.$j -x traj.nve.$j -e mden.nve.$j -inf mdinfo.nve.$j
  pmemd.cuda -O -p full.topo -c rst.nve.$j -ref rst.nve.$j -i mdin-npt -o mdout.npt.$j -r rst.npt.$j -e mden.npt.$j -inf mdinfo.npt.$j
  @ i += 1
end



