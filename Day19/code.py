import math
import os, sys
import itertools
from typing  import Counter
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from  AOCHelper import * 
input = []
def readinput():
   global input
   global nums
   global beacons
   input = readinput_lines("Day19\input_ex.txt")
   beacons = defaultdict(list)
   b = []
   idx = 0
   for line in input:      
      line.strip()
      if line == '' : 
         beacons[idx].append(b)
         b = []
         idx+=1
         continue
      
      if line.startswith('--'):
         continue
      x,y,z = [int(v) for v in line.split(',')]
      b.append((x,y,z))
   beacons[idx].append(b)

def main():
   readinput()
   first_star()
   #second_star()        

def first_star():
   # coord voor x -->
   # 4 x NESW
   # 2 X up/down
   # scanner 1 kan 2000 pos verschillen per richting (x,y,z)
   global beacons
   x2,y2,z2 = 0,0,0
   for scanner in beacons:
      for scanner2 in [s for s in beacons if s != scanner]:
         dist= defaultdict(list)
         for cons in beacons[scanner]:           
            for beacon in cons:
               x,y,z =  beacon        
               f = find_beacons(scanner2,x,y,z)
               for b in f:
                  dist[b].append(f[b])

         for di in dist:
            if len(dist[di]) >= 12:
               print(di) 
   
   print("Result First Star")
  
def find_beacons(scanner,x,y,z):
   dist = defaultdict(list)
   for cons in beacons[scanner]:
      for beacon in cons:
         x2,y2,z2 = beacon
      
         dist[(x-(x2),y-(y2),z-(z2))].append((x,y,z))
         dist[(x-(x2),y-(y2*-1),z-(z2))].append((x,y,z))
         dist[(x-(x2),y-(y2*-1),z-(z2*-1))].append((x,y,z))      
         dist[(x-(x2*-1),y-(y2*-1),z-(z2*-1))].append((x,y,z))
            
   return dist

def second_star():
   print(find_beacons(1,-618,-824,-621))
   print("Result Second Star")
  
if __name__ == '__main__':
    main()