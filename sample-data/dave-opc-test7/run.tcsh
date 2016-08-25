
          -------------------------------------------------------
          Amber 16 PMEMD                              2016
          -------------------------------------------------------

| PMEMD implementation of SANDER, Release 16

| Run on 08/04/2016 at 08:51:26

|   Executable path: pmemd.cuda
| Working directory: /home/henrikse/data_kirkwood/projects/forcefield/set2/dave-opc-test7
|          Hostname: entropy.ucsd.edu

  [-O]verwriting output

File Assignments:
|   MDIN: mdin-nve                                                              
|  MDOUT: mdout.nve.1                                                           
| INPCRD: rst.npt.0                                                             
|   PARM: full.topo                                                             
| RESTRT: rst.nve.1                                                             
|   REFC: refc                                                                  
|  MDVEL: mdvel                                                                 
|   MDEN: mden.nve.1                                                            
|  MDCRD: traj.nve.1                                                            
| MDINFO: mdinfo.nve.1                                                          
|  MDFRC: mdfrc                                                                 


 Here is the input file:

                                                                               
Production, NVE, 20ps                                                          
&cntrl                                                                         
  ntx=5,                                                                       
  irest=1,                                                                     
  ntc=2,                                                                       
  ntf=2,                                                                       
  dt=0.001,                                                                    
  nstlim=20000,                                                                
  cut=8.0,                                                                     
  temp0=298.16,                                                                
  iwrap=0,                                                                     
  nscm=0,                                                                      
  ntt=0,                                                                       
  ntpr=20000,                                                                  
  ntwr=20000,                                                                  
  ntxo=2,                                                                      
  ntwx=1000,                                                                   
  ioutfm=1,                                                                    
  ntwe=500,                                                                    
/                                                                              
                                                                               


Note: ig = -1. Setting random seed to   251265 based on wallclock time in 
      microseconds.
 
|--------------------- INFORMATION ----------------------
| GPU (CUDA) Version of PMEMD in use: NVIDIA GPU IN USE.
|                    Version 16.0.0
| 
|                      02/25/2016
| 
| Implementation by:
|                    Ross C. Walker     (SDSC)
|                    Scott Le Grand     (nVIDIA)
| 
| Precision model in use:
|      [SPFP] - Single Precision Forces, 64-bit Fixed Point
|               Accumulation. (Default)
| 
|--------------------------------------------------------
 
|----------------- CITATION INFORMATION -----------------
|
|    When publishing work that utilized the CUDA version
|    of AMBER, please cite the following in addition to
|    the regular AMBER citations:
|
|  - Romelia Salomon-Ferrer; Andreas W. Goetz; Duncan
|    Poole; Scott Le Grand; Ross C. Walker "Routine
|    microsecond molecular dynamics simulations with
|    AMBER - Part II: Particle Mesh Ewald", J. Chem.
|    Theory Comput., 2013, 9 (9), pp3878-3888,
|    DOI: 10.1021/ct400314y.
|
|  - Andreas W. Goetz; Mark J. Williamson; Dong Xu;
|    Duncan Poole; Scott Le Grand; Ross C. Walker
|    "Routine microsecond molecular dynamics simulations
|    with AMBER - Part I: Generalized Born", J. Chem.
|    Theory Comput., 2012, 8 (5), pp1542-1555.
|
|  - Scott Le Grand; Andreas W. Goetz; Ross C. Walker
|    "SPFP: Speed without compromise - a mixed precision
|    model for GPU accelerated molecular dynamics
|    simulations.", Comp. Phys. Comm., 2013, 184
|    pp374-380, DOI: 10.1016/j.cpc.2012.09.022
|
|--------------------------------------------------------
 
|------------------- GPU DEVICE INFO --------------------
|
|            CUDA_VISIBLE_DEVICES: 0
|   CUDA Capable Devices Detected:      1
|           CUDA Device ID in use:      0
|                CUDA Device Name: GeForce GTX 980
|     CUDA Device Global Mem Size:   4095 MB
| CUDA Device Num Multiprocessors:     16
|           CUDA Device Core Freq:   1.22 GHz
|
|--------------------------------------------------------
 
 
| Conditional Compilation Defines Used:
| PUBFFT
| BINTRAJ
| CUDA
| EMIL

| Largest sphere to fit in unit cell has radius =    15.524

| New format PARM file being parsed.
| Version =    1.000 Date = 06/27/16 Time = 10:18:50

| Note: 1-4 EEL scale factors are being read from the topology file.

| Note: 1-4 VDW scale factors are being read from the topology file.
| Duplicated    0 dihedrals

| Duplicated    0 dihedrals

--------------------------------------------------------------------------------
   1.  RESOURCE   USE: 
--------------------------------------------------------------------------------

 getting new box info from bottom of inpcrd
 NATOM  =    4000 NTYPES =       3 NBONH =    3000 MBONA  =    1000
 NTHETH =       0 MTHETA =       0 NPHIH =       0 MPHIA  =       0
 NHPARM =       0 NPARM  =       0 NNB   =    7000 NRES   =    1000
 NBONA  =    1000 NTHETA =       0 NPHIA =       0 NUMBND =       3
 NUMANG =       0 NPTRA  =       0 NATYP =       3 NPHB   =       1
 IFBOX  =       1 NMXRS  =       4 IFCAP =       0 NEXTRA =    1000
 NCOPY  =       0

| Coordinate Index Table dimensions:     6    6    6
| Direct force subcell size =     5.1750    5.1750    5.1747

     BOX TYPE: RECTILINEAR

--------------------------------------------------------------------------------
   2.  CONTROL  DATA  FOR  THE  RUN
--------------------------------------------------------------------------------

default_name                                                                    

General flags:
     imin    =       0, nmropt  =       0

Nature and format of input:
     ntx     =       5, irest   =       1, ntrx    =       1

Nature and format of output:
     ntxo    =       2, ntpr    =   20000, ntrx    =       1, ntwr    =   20000
     iwrap   =       0, ntwx    =    1000, ntwv    =       0, ntwe    =     500
     ioutfm  =       1, ntwprt  =       0, idecomp =       0, rbornstat=      0

Potential function:
     ntf     =       2, ntb     =       1, igb     =       0, nsnb    =      25
     ipol    =       0, gbsa    =       0, iesp    =       0
     dielc   =   1.00000, cut     =   8.00000, intdiel =   1.00000

Frozen or restrained atoms:
     ibelly  =       0, ntr     =       0

Molecular dynamics:
     nstlim  =     20000, nscm    =         0, nrespa  =         1
     t       =   0.00000, dt      =   0.00100, vlimit  =  -1.00000

SHAKE:
     ntc     =       2, jfastw  =       0
     tol     =   0.00001

| Intermolecular bonds treatment:
|     no_intermolecular_bonds =       1

| Energy averages sample interval:
|     ene_avg_sampling =   20000

Extra-points options:
     frameon =       1, chngmask=       1

Ewald parameters:
     verbose =       0, ew_type =       0, nbflag  =       1, use_pme =       1
     vdwmeth =       1, eedmeth =       1, netfrc  =       1
     Box X =   31.050   Box Y =   31.050   Box Z =   31.048
     Alpha =   90.000   Beta  =   90.000   Gamma =   90.000
     NFFT1 =   32       NFFT2 =   32       NFFT3 =   32
     Cutoff=    8.000   Tol   =0.100E-04
     Ewald Coefficient =  0.34864
     Interpolation order =    4
|      EXTRA_PTS, trim_bonds: num bonds BEFORE trim =  3000     0
|      EXTRA_PTS, trim_bonds: num bonds AFTER  trim =  3000     0
|      EXTRA_PTS, trim_bonds: num bonds BEFORE trim =  1000     0
|      EXTRA_PTS, trim_bonds: num bonds AFTER  trim =     0     0
|      EXTRA_PTS, trim_theta: num angle BEFORE trim =     0     0
|      EXTRA_PTS, trim_theta: num angle AFTER  trim =     0     0
|      EXTRA_PTS, trim_theta: num angle BEFORE trim =     0     0
|      EXTRA_PTS, trim_theta: num angle AFTER  trim =     0     0
|      EXTRA_PTS, trim_phi:  num diheds BEFORE trim =     0     0
|      EXTRA_PTS, trim_phi:  num diheds AFTER  trim =     0     0
|      EXTRA_PTS, trim_phi:  num diheds BEFORE trim =     0     0
|      EXTRA_PTS, trim_phi:  num diheds AFTER  trim =     0     0

--------------------------------------------------------------------------------
   3.  ATOMIC COORDINATES AND VELOCITIES
--------------------------------------------------------------------------------

default_name                                                                    
 begin time read from input coords =   120.000 ps

 
 Number of triangulated 3-point waters found:     1000

     Sum of charges from parm topology file =   0.00000549
     Forcing neutrality...

| Dynamic Memory, Types Used:
| Reals              228826
| Integers           180013

| Nonbonded Pairs Initial Allocation:      668100

| GPU memory information (estimate):
| KB of GPU memory in use:     11954
| KB of CPU memory in use:      4866

--------------------------------------------------------------------------------
   4.  RESULTS
--------------------------------------------------------------------------------

 ---------------------------------------------------
 APPROXIMATING switch and d/dx switch using CUBIC SPLINE INTERPOLATION
 using   5000.0 points per unit in tabled values
 TESTING RELATIVE ERROR over r ranging from 0.0 to cutoff
| CHECK switch(x): max rel err =   0.2738E-14   at   2.422500
| CHECK d/dx switch(x): max rel err =   0.8332E-11   at   2.782960
 ---------------------------------------------------
|---------------------------------------------------
| APPROXIMATING direct energy using CUBIC SPLINE INTERPOLATION
|  with   50.0 points per unit in tabled values
| Relative Error Limit not exceeded for r .gt.   2.47
| APPROXIMATING direct force using CUBIC SPLINE INTERPOLATION
|  with   50.0 points per unit in tabled values
| Relative Error Limit not exceeded for r .gt.   2.89
|---------------------------------------------------

 NSTEP =    20000   TIME(PS) =     140.000  TEMP(K) =   298.55  PRESS =     0.0
 Etot   =    -10497.0096  EKtot   =      1779.8403  EPtot      =    -12276.8499
 BOND   =         0.0000  ANGLE   =         0.0000  DIHED      =         0.0000
 1-4 NB =         0.0000  1-4 EEL =         0.0000  VDWAALS    =      1901.8101
 EELEC  =    -14178.6600  EHBOND  =         0.0000  RESTRAINT  =         0.0000
 ------------------------------------------------------------------------------


      A V E R A G E S   O V E R       1 S T E P S


 NSTEP =    20000   TIME(PS) =     140.000  TEMP(K) =   298.55  PRESS =     0.0
 Etot   =    -10497.0096  EKtot   =      1779.8403  EPtot      =    -12276.8499
 BOND   =         0.0000  ANGLE   =         0.0000  DIHED      =         0.0000
 1-4 NB =         0.0000  1-4 EEL =         0.0000  VDWAALS    =      1901.8101
 EELEC  =    -14178.6600  EHBOND  =         0.0000  RESTRAINT  =         0.0000
 ------------------------------------------------------------------------------


      R M S  F L U C T U A T I O N S


 NSTEP =    20000   TIME(PS) =     140.000  TEMP(K) =     0.00  PRESS =     0.0
 Etot   =         0.0000  EKtot   =         0.0000  EPtot      =         0.0000
 BOND   =         0.0000  ANGLE   =         0.0000  DIHED      =         0.0000
 1-4 NB =         0.0000  1-4 EEL =         0.0000  VDWAALS    =         0.0000
 EELEC  =         0.0000  EHBOND  =         0.0000  RESTRAINT  =         0.0000
|E(PBS) =         0.0000
 ------------------------------------------------------------------------------

--------------------------------------------------------------------------------
   5.  TIMINGS
--------------------------------------------------------------------------------

|  NonSetup CPU Time in Major Routines:
|
|     Routine           Sec        %
|     ------------------------------
|     Nonbond           3.85   40.35
|     Bond              0.00    0.00
|     Angle             0.00    0.00
|     Dihedral          0.00    0.00
|     Shake             0.17    1.78
|     RunMD             5.50   57.66
|     Other             0.02    0.22
|     ------------------------------
|     Total             9.54

|  PME Nonbond Pairlist CPU Time:
|
|     Routine              Sec        %
|     ---------------------------------
|     Set Up Cit           0.00    0.00
|     Build List           0.00    0.00
|     ---------------------------------
|     Total                0.00    0.00

|  PME Direct Force CPU Time:
|
|     Routine              Sec        %
|     ---------------------------------
|     NonBonded Calc       0.00    0.00
|     Exclude Masked       0.00    0.00
|     Other                0.01    0.10
|     ---------------------------------
|     Total                0.01    0.10

|  PME Reciprocal Force CPU Time:
|
|     Routine              Sec        %
|     ---------------------------------
|     1D bspline           0.00    0.00
|     Grid Charges         0.00    0.00
|     Scalar Sum           0.00    0.00
|     Gradient Sum         0.00    0.00
|     FFT                  0.00    0.00
|     ---------------------------------
|     Total                0.00    0.00

|  Final Performance Info:
|     -----------------------------------------------------
|     Average timings for last       0 steps:
|     Elapsed(s) =       0.00 Per Step(ms) =   Infinity
|         ns/day =       0.00   seconds/ns =   Infinity
|
|     Average timings for all steps:
|     Elapsed(s) =       9.55 Per Step(ms) =       0.48
|         ns/day =     180.96   seconds/ns =     477.46
|     -----------------------------------------------------

|  Setup CPU time:            0.75 seconds
|  NonSetup CPU time:         9.54 seconds
|  Total CPU time:           10.29 seconds     0.00 hours

|  Setup wall time:           2    seconds
|  NonSetup wall time:        9    seconds
|  Total wall time:          11    seconds     0.00 hours
