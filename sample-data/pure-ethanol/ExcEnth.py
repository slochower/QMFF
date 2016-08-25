import sys,os,re
import subprocess as sp
import numpy as np
from time import sleep
### Args: <Res1> <Res2>
###        wat    mth

if len(sys.argv) < 2:
  print "ARGS: provide a CUDA_VISIBLE_DEVICES number\n"
  sys.exit(0)

CVD=sys.argv[1]

RN1 = 'wat'
RN2 = 'mth'
MaxMol = 1000
#MixN = [1000, 950, 900, 800, 700, 600, 500, 400, 300, 200, 100, 50, 0]
#MixN = [0, 50, 100, 200, 300, 400, 500, 600, 700, 800, 900, 950, 1000]
MixN = [0, 1000, 500, 200, 800, 100, 900, 300, 700, 400, 600, 50, 950]
#MixN = [1000]

pdb = open(RN1+'.pdb', 'r')
for line in pdb:
  line = line.rstrip()
  if re.search('REMARK VOLUME', line):
    R,V,Vol1 = line.split(' ', 2)
    Vol1 = float(Vol1) + 0.70*float(Vol1)
pdb.close()

pdb = open(RN2+'.pdb', 'r')
for line in pdb:
  line = line.rstrip()
  if re.search('REMARK VOLUME', line):
    R,V,Vol2 = line.split(' ', 2)
    Vol2 = float(Vol2) + 0.70*float(Vol2)
pdb.close()



for N2 in MixN:
  N1 = MaxMol-N2
  Ratio = "%.2f" % (float(N2)/float(MaxMol))
  BoxEdge = (float(N1)*Vol1 + float(N2)*Vol2)**(1./3.)
  print N1,N2,Ratio
  folder = 'x'+str(Ratio)
  if not os.path.exists(folder):
    os.makedirs(folder)
  sp.call (['cp',RN1+'.pdb',RN2+'.pdb',folder])
  if RN1 != 'wat':
    sp.call(['cp',RN1+'.mol2',folder])
  if RN2 != 'wat':
    sp.call(['cp',RN2+'.mol2',folder])


  ### Loop to build system until there aren't any errors
  itr=0
  while itr < 10 and ( not os.path.isfile(folder+'/eq1.out') or not 'TIMINGS' in open(folder+'/eq1.out').read() or 'NaN' in open(folder+'/eq1.out').read() or '********' in open(folder+'/eq1.out').read() ):

    print folder,": Round",itr

    RandNum = np.random.randint(999999999)
    packinp = open(folder+'/packmol.in', 'w')
    packinp.write("""
tolerance 2.0
filetype pdb
output mixture.pdb
seed %.0f

structure %s.pdb
  number %s
  inside cube 0. 0. 0. %.5f
end structure

structure %s.pdb
  number %s
  inside cube 0. 0. 0. %.5f
end structure

""" % (RandNum,RN1,N1,BoxEdge,RN2,N2,BoxEdge))
    packinp.close()
    packinp = open(folder+'/packmol.in', 'r')
    packout = open(folder+'/packmol.out', 'w')
    sp.call('packmol',cwd=folder,stdin=packinp,stdout=packout,stderr=packout)
    packinp.close()
    packout.close()

    tleapin = open(folder+'/tleap.in', 'w')
    tleapin.write("""
loadamberparams parm10.dat
source leaprc.gaff2
WAT = OPC 
source leaprc.water.opc
""")
    if RN1 != 'wat':
      tleapin.write("%s = loadmol2 %s.mol2\n" % (RN1.upper(),RN1))
    if RN2 != 'wat':
      tleapin.write("%s = loadmol2 %s.mol2\n" % (RN2.upper(),RN2))
    tleapin.write("""
model = loadpdb mixture.pdb

setbox model vdw

savepdb model full.pdb
saveamberparm model full.topo full.crds

quit
""")
    tleapin.close()
    tleapout = open(folder+'/tleap.out', 'w')
    sp.call(['tleap','-s','-f','tleap.in'],cwd=folder,stdout=tleapout,stderr=tleapout)
    tleapout.close()

    mini = open(folder+'/mini.in', 'w')
    mini.write("""
Minimization
&cntrl
  imin=1,
  maxcyc=10000,
  ncyc=100,
  ntpr=100, 
/
""")
    mini.close()
    sp.call('pmemd.cuda -O -p full.topo -c full.crds -i mini.in -o mini.out -r mini.rst -inf /dev/null', cwd=folder, env=dict(os.environ, CUDA_VISIBLE_DEVICES=str(CVD)), shell=True)

    eq1 = open(folder+'/eq1.in', 'w')
    eq1.write("""
Hot Start, NPT, 0.02ns
&cntrl
  ntx=1,
  irest=0,
  ntc=2,
  ntf=2,
  dt=0.002,
  nstlim=10000,
  cut=8.0,
  temp0=298.15,
  iwrap=1,
  ntt=3,
  ig=-1,
  gamma_ln=1,
  ntp=1,
  barostat=2,
  mcbarint=10,
  ntpr=10000,
  ntwr=10000,
  ntwx=0,
  ntwe=50,
/
""")
    eq1.close()
    sp.call('pmemd.cuda -O -p full.topo -c mini.rst -i eq1.in -o eq1.out -r eq1.rst -e eq1.mden -inf eq1.inf',cwd=folder, env=dict(os.environ, CUDA_VISIBLE_DEVICES=str(CVD)), shell=True)

    itr += 1

  ### If we made it here, everything should run ok
   
  eq2 = open(folder+'/eq2.in', 'w')
  eq2.write("""
Hot Start, NPT, 0.1ns
&cntrl
  ntx=5,
  irest=1,
  ntc=2,
  ntf=2,
  dt=0.002,
  nstlim=50000,
  cut=8.0,
  temp0=298.15,
  iwrap=1,
  ntt=3,
  ig=-1,
  gamma_ln=1,
  ntp=1,
  barostat=2,
  ntpr=50000,
  ntwr=50000,
  ntwx=0,
  ntwe=500,
/
""")
  eq2.close()
  sp.call('pmemd.cuda -O -p full.topo -c eq1.rst -i eq2.in -o eq2.out -r eq2.rst -e eq2.mden -inf eq2.inf',cwd=folder, env=dict(os.environ, CUDA_VISIBLE_DEVICES=str(CVD)), shell=True)
  
  mdin = open(folder+'/mdin', 'w')
  mdin.write("""
Production, NPT, 1ns
&cntrl
  ntx=5,
  irest=1,
  ntc=2,
  ntf=2,
  dt=0.002,
  nstlim=500000,
  cut=8.0,
  temp0=298.15,
  iwrap=1,
  ntt=3,
  ig=-1,
  gamma_ln=1,
  ntp=1,
  barostat=2,
  ntpr=500000,
  ntwr=500000,
  ntxo=2,
  ntwx=5000,
  ioutfm=1,
  ntwe=250,
  
/
""")
  mdin.close()
  sp.call('pmemd.cuda -O -p full.topo -c eq2.rst -i mdin -o mdout.001 -r rst.001 -x traj.001 -e mden.001 -inf mdinfo.001',cwd=folder, env=dict(os.environ, CUDA_VISIBLE_DEVICES=str(CVD)), shell=True)

  sp.call('grep L3 mden.001 | tail -n +2 | awk \'{printf "%.5f\\n",$2}\' > vol.dat', cwd=folder, shell=True)
  sp.call('cat vol.dat | python /home/henrikse/pe/reblock.py >& vol.err.dat', cwd=folder, shell=True)
  sp.call('grep L6 mden.001 | tail -n +2 | awk \'{printf "%.5f\\n",$3}\' > eptot.dat', cwd=folder, shell=True)
  sp.call('cat eptot.dat | python /home/henrikse/pe/reblock.py >& eptot.err.dat', cwd=folder, shell=True)
  sp.call('grep L9 mden.001 | tail -n +2 | awk \'{printf "%.5f\\n",$5}\' > dens.dat', cwd=folder, shell=True)
  sp.call('cat dens.dat | python /home/henrikse/pe/reblock.py >& dens.err.dat', cwd=folder, shell=True)

  sys.stdout.flush()





