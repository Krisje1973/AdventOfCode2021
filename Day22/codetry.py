import math
import os, sys
from itertools import permutations,combinations
import numpy as np
from typing  import Counter
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from  AOCHelper import * 
input = []
cubes = defaultdict(list)
def readinput():
   global input
   global cubes
  
   input = readinput_lines("Day22\input.txt")
   for cube in [[s,s[1].split('x='),s[1].split('y='),s[1].split('z=')] for s in [line.split() for line in input]]:
      x= tuple(map(int,cube[1][1].split(',')[0].split('..')))
      y= tuple(map(int,cube[2][1].split(',')[0].split('..')))
      z= tuple(map(int,cube[3][1].split(',')[0].split('..')))
      cubes[x,y,z] = cube[0][0] == 'on'
      
         
def first_star():
   cuboid = defaultdict(bool)
   for x,y,z in cubes.keys():
      cuboid = create_cuboid(cuboid,x,y,z,cubes[(x,y,z)],True)
   
   print("Result First Star")
   print(sum(cuboid.values()))

def second_star():
   s,e = 0,0
   #cubes[x,y,z,0,0,0,0,0,0]
   # 3= minx,4=maxx,5=miny,6=maxy,7=minz,8=maxz
   ron = [[] for c in cubes]
   rof = [[] for c in cubes]
   cuboid = defaultdict(bool)
   for i,cube in enumerate(cubes):
      if cubes[cube] : ron[i] = cube
      else:  rof[i] = cube
   
   #for r in ron:
    #  over = []
     # for ro in rof:
      #   over.append(find_overlap(range(r[0][0],r[0][1]),range(ro[0][0],ro[0][1])))
   cnt=0
   tot=0
   tot2=0
   for cube in cubes:
      overx = defaultdict(tuple)
      overy = defaultdict(tuple)
      overz = defaultdict(tuple)
    
      for ro in rof[cnt:]:
         if len(ro) == 0 : continue
         x= find_overlap(range(cube[0][0],cube[0][1]),range(ro[0][0],ro[0][1]))
         if x: overx[x] = [x.start,x.stop]
         y = find_overlap(range(cube[1][0],cube[1][1]),range(ro[0][0],ro[1][1]))
         if y: overy[y] = [y.start,y.stop]
         z=find_overlap(range(cube[2][0],cube[1][1]),range(ro[0][0],ro[2][1]))
         if z: overz[z]= [z.start,z.stop]

      defr = range(-100000,100000)
      if len(overx)==0:
         overx[defr] = [defr.start,defr.stop]
      if len(overy)==0:
         overy[defr] = [defr.start,defr.stop]
      if len(overz)==0:
         overz[defr] = [defr.start,defr.stop]

      bounds = [min(overx.values())[0],max(overx.values())[1],min(overy.values())[0],max(overy.values())[1],min(overz.values())[0],max(overz.values())[1]]
      s = [min(overx.values())[0],min(overy.values())[0],min(overz.values())[0]]
      e = [max(overx.values())[1],max(overy.values())[1],max(overz.values())[1]]
      if cubes[cube]:
         tot += (e[2] - s[2]) * (e[1] - s[1]) * (e[0] - s[0])
      else:
         tot -= (e[2] - s[2]) * (e[1] - s[1]) * (e[0] - s[0])
      
      if cubes[cube]:
         tot2 += (cube[0][1] - cube[0][0]) * (cube[1][1] - cube[1][0]) * (cube[2][1] - cube[2][0])
      else:
         tot2 -= (cube[0][1] - cube[0][0]) * (cube[1][1] - cube[1][0]) * (cube[2][1] - cube[2][0])
   print(tot2,tot)
   #1237264238382479
   #9605574853876117
   #cuboid = create_cuboid(cuboid,cube[0],cube[1],cube[2],cubes[cube]=='on',bounds)
      
   print("Result Second Star")
   print(sum(cuboid.values()))

def second_staré():
   s,e = 0,0
   #cubes[x,y,z,0,0,0,0,0,0]
   # 3= minx,4=maxx,5=miny,6=maxy,7=minz,8=maxz
   print(find_overlap(range(500,1000),range(800,20000)))
  
   bounds = defaultdict(int)
   for i in range(3):
      for cube in [c for c in cubes if not cubes[c]]:
         s = cube[i][0] if cube[i][0] < s else s
         e = cube[i][1] if cube[i][1] > e else e
      for cube in [c for c in cubes if not cubes[c]]:
         bounds[i] = [s,e]
   cuboid = []
   for x,y,z in cubes.keys():
      cuboid = create_cuboid_withbounds(cuboid,x,y,z,cubes[(x,y,z)],bounds)
  
   print("Result Second Star")
   print(len(cuboid))
   
  
def create_cuboid_withbounds(cuboid,x,y,z,switch,bounds):
   for xx in range(bounds[0][0],bounds[0][1]):
      for yy in  range(bounds[1][0],bounds[1][1]):
         for zz in  range(bounds[2][0],bounds[2][1]):
            if switch:
               cuboid.append(([xx],[yy],[zz])) 
            else:
               cuboid.pop(([xx],[yy],[zz])) 
   return cuboid

def get_overlap(x,y):
     return range(max(x.start,y.start), min(x.stop,y.stop)) or None

def find_overlap(x,y):
     return range(max(x.start,y.start), min(x.stop,y.stop)) or None
     
def create_cuboid(cuboid,x,y,z,switch,bounds):
  
   x1 = max(x[0], bounds[0])
   y1 = max(y[0], bounds[2])
   z1 = max(z[0], bounds[4])
   
   x2 = min(x[1], bounds[1])
   y2 = min(y[1], bounds[3])
   z2 = min(z[1], bounds[5])
   for xx in range(x1,x2+1):
      for yy in  range(y1,y2+1):
         for zz in  range(z1,z2+1):
            if switch:
               cuboid[(xx,yy,zz)] = switch
            else:
               cuboid.pop((xx,yy,zz),None)
   return cuboid
  
   
def main():
   readinput()
   #first_star()
   second_star()     

if __name__ == '__main__':
    main()