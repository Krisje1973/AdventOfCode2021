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
   sd = [set() for _ in range(3)]
   for i in range(3):
      for r in cubes:
         sd[i].add(r[i][0])
         sd[i].add(r[i][1])

   sd = list(map(sorted, sd))
   grid = [[[0] * (len(sd[2]) - 1) for _ in range(len(sd[1]) - 1)] for _ in range(len(sd[0]) - 1)]
   for cube in cubes:
      for xx in range(cube[0][0],cube[0][1]):
         for yy in  range(cube[1][0],cube[1][1]):
            for zz in  range(cube[2][0],cube[2][1]):
               grid[xx][yy][zz] = cubes[cube] 
   
   t = 0
   for x in range(len(grid)):
      for y in range(len(grid[x])):
         for z in range(len(grid[x][y])):
               if grid[x][y][z]:
                  t += (sd[0][x + 1] - sd[0][x]) * (sd[1][y + 1] - sd[1][y]) * (sd[2][z + 1] - sd[2][z])
   print("Result Second Star")
   print(t)

def find_overlap(x,y):
     return range(max(x.start,y.start), min(x.stop,y.stop)) or None
     
def create_cuboid(cuboid,x,y,z,switch,bound):
   if bound:
      if x[1]+1 >=51 <= -51 or y[1]+1 >51 <= -51 or z[1]+1 >51 <= -51: return cuboid
      x1 = max(x[0], -50)
      y1 = max(y[0], -50)
      z1 = max(z[0], -50)
      
      x2 = min(x[1], 50)
      y2 = min(y[1], 50)
      z2 = min(z[1], 50)
      
   for xx in range(x1,x2+1):
      for yy in  range(y1,y2+1):
         for zz in  range(z1,z2+1):
            cuboid[(xx,yy,zz)] = switch=='on'
   return cuboid
  
   
def main():
   readinput()
   #first_star()
   second_star()     

if __name__ == '__main__':
    main()