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
   
   scans = defaultdict(list)
  
   cnt = 0
   for scanner in beacons:
      for scanner2 in [s for s in beacons if s != scanner]:
         dist= []
         found = defaultdict(int)
         for cons in beacons[scanner]:
            for beacon in cons:
               x,y,z =  beacon               
               dist+=find_beacons(scanner2,x,y,z)

            for di in dist:
               found[di] += 1 
            for k,v in [k,v for k,v in found.values() if v > 10]:
               print(v)
         #print(found[(68,-1246,-43)])  
   #d_inter = dict(set(found[0]).intersection(found[1]))
  
   print("Result First Star")
  

def partial_match(key, d):
    for k, v in d.iteritems():
        if all(k1 == k2 or k2 is None  for k1, k2 in zip(k, key)):
            yield v
def find_beacons(scanner,x,y,z):
   dist = []
   
   for cons2 in beacons[scanner]:
      for beacon2 in cons2:
         x2,y2,z2 = beacon2
      
         dist.append((x+(x2*-1),y+(y2*-1),z+(z2*-1)))
         dist.append((x+(x2),y+(y2),z+(z2)))
         dist.append((x+(x2),y+(y2*-1),z+(z2)))
         dist.append((x+(x2),y+(y2*-1),z+(z2*-1)))           
            
   return dist

def second_star():
   print(find_beacons(1,-618,-824,-621))
   print("Result Second Star")
  
if __name__ == '__main__':
    main()