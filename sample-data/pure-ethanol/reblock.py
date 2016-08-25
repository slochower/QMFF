
### You should have cpptraj in your path!

import numpy as np # numerical array library
import subprocess as sp # system calls
import sys,os

### Functions
def factors(n):   # Return list of integer factors
  facs=[]
  sqrt=int(round(np.sqrt(n)+0.5))
  i = 1
  while i <= sqrt:
    if n % i == 0:
      facs.append(i)
      j=n/i
      if j != i:
        facs.append(j)
    i += 1
  return sorted(facs, key=int)

def nearestmax(n):  # Nearest number that is 100 less than input and divisible by two
  int=[]
  numfac=[]
  maxfac=0
  if n % 2 == 0:
    low=n-100
    high=n
  else:
    low=n-101
    high=n-1
  if low < 0:
    low = 0
  for i in range(low,high+2,2):
    numfac = len(factors(i))
    if numfac >= maxfac:
      maxfac = numfac
      mostfac = i
  return mostfac

def seom(N,arr):
  Facs=[]
  Facs=factors(N)
  Bn=np.zeros([len(Facs)], np.int32) # Number of blocks for a given block size
  Bmean=np.zeros([len(Facs),Facs[-1]], np.float64) # Means for each block of each block size
  SEOM=np.zeros([len(Facs)-2],np.float64)
  for i in range(len(Facs)-2):   # Run over all block sizes except the final two: two blocks, one block.
    for j in range(Facs[-i-1]):  # Run over all blocks in the data for a specific size.
      Bmean[i,j]=np.mean(arr[j*Facs[i]:(j+1)*Facs[i]])
    Bn[i]=j+1
    SEOM[i]=np.std(Bmean[i,0:Bn[i]],ddof=0)/np.sqrt(Bn[i]-1) # or ddof=1? I think 0, see Flyvbjerg
    print Facs[i],SEOM[i],SEOM[i]/np.sqrt(2*(Bn[i]-1))  # Blocksize, SEOM, Error of SEOM (see equation 28 in Flyvbjerg, JCP, 1989)
  hist,edges = np.histogram(SEOM,range=[np.min(SEOM),np.max(SEOM)],bins=50,)  ### edges = len(hist)+1
  return np.max(SEOM),edges[np.argmax(hist)+1]  # Assume the blocking plateau corresponds to the max histogram count!

### Calculate Statistical Inefficiency (g).  Input a 1D numpy array.
def calcg(data):
  sum = 0
  randnum = ("%05.0f" % (int(100000*np.random.random())))
  datafn = '/dev/shm/series.'+randnum+'.dat'
  acffn = '/dev/shm/acf.'+randnum+'.dat'
  cppfn = '/dev/shm/pt-acf.'+randnum+'.in'
  np.savetxt(datafn,data)
  cpptin = open(cppfn, 'w')
  cpptin.write("readdata "+datafn+" name "+randnum+"\nautocorr "+randnum+" out "+acffn+" noheader prec 15.10\n")
  cpptin.close()

  FNULL = open(os.devnull, 'w')
  sp.call(['cpptraj','-i',cppfn], stdout=FNULL, stderr=sp.STDOUT)

  with open(acffn, 'r') as acf:
    for line in acf:
      col = line.split()
      t = float(col[0]) - 1.0
  T = t

  with open(acffn, 'r') as acf:
    for line in acf:
      col = line.split()
      t = float(col[0]) - 1.0
      v = float(col[1])
      if t == 0:
        continue
      if v < 0.0:
        break
      sum += ( 1 - (t/T) )*(v)

  sp.call(['rm',datafn,acffn,cppfn])

  return 1+(2*sum)

# Do the job of pymbar timerseries: subsample
def makesubsamp(g,N):
  list = [0]
  n = 1
  step = int(np.round(n*g))
  while step < N:
    list.extend([step])
    n += 1
    step = int(np.round(n*g))
  return list



pipe = sys.stdin.read()
data = np.array(pipe.splitlines(), np.float64) # piped data
dataind = np.array(pipe.splitlines(), np.float64) # separate array for subsampled data

Nblk = nearestmax(data.size)  # N for blocking (nearest)
Ntot = data.size # Total Number of data points

seommax,seommod = seom(Nblk,data[0:Nblk])
blkmean=np.mean(data[0:Nblk])
blkvar=np.var(data[0:Nblk])

stineff = calcg(data[0:Ntot])
indices = makesubsamp(stineff,Ntot)
Nind = len(indices)
dataind[0:Nind] = data[indices]


#print "# Ntot= %.0f    Nblk= %.0f BlkMean= %.4f  BlkMaxErr= %.7f BlkModeErr= %.7f        StIn= %.4f NumIndSamp= %.0f StInMean= %.4f StInSEM= %.7f" % (Ntot,Nblk,blkmean,seommax,seommod,stineff,Nind,np.mean(data[0:Ntot]),np.std(data[0:Ntot])/np.sqrt(Nind))
print "# NTot= %.0f  NBlk= %.0f BlkAvg= %.7f BlkMaxSEM= %.7f BlkModSEM= %.7f  StIn= %.4f NIndSamp= %.0f StInAvg= %.4f StInSEM= %.7f  BMaxNIS= %.5f BModNIS= %.5f" % (Ntot,Nblk,blkmean,seommax,seommod,stineff,Nind,np.mean(data[0:Ntot]),np.std(data[0:Ntot])/np.sqrt(Nind),blkvar/(seommax**2),blkvar/(seommod**2))


#print "Num= %.0f StIn= %.4f NumIndSamp= %.0f StInMean= %.4f StInSEM= %.7f" % (Nmax,stineff,Nind,np.mean(data[0:Nind]),np.std(data[0:Nind])/np.sqrt(Nind))






