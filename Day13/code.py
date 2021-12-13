import math
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from  AOCHelper import * 
input = []
def readinput():
   global input
   global grid
   global folds
   global maxx
   global maxy
   input = readinput_lines("Day13\input.txt")
   dots = {}
   folds = []
   maxx = 0
   maxy = 0
   for idx,line in enumerate(input):
      if line == '':
         break
      dots[idx] = line.split(',')
      if int(dots[idx][0]) > maxx:
         maxx = int(dots[idx][0])
      if int(dots[idx][1]) > maxy:
         maxy= int(dots[idx][1])
   maxx +=1
   maxy +=1
   for line in input[idx+1:]:
      s=line.split('=')
      folds.append([s[0].split('fold along')[1],s[1]])
   grid = [[0 for x in range(maxx)] for x in range(maxy)]
   for dot in dots.values():
      grid[int(dot[1])][int(dot[0])] = 1
def main():
   readinput()
   #first_star()
   second_star()        

def first_star():
   global grid
   #102 TO Low
   #Zucht, het was ENKEL 1 fold :( grrr :P
   for xy,v in folds:
      v=int(v)
      v2= v*2
      if xy.strip() == 'y':
         for y in range(v):
            for idx,x in enumerate(grid[y]):
               grid[y][idx] = int(grid[y][idx]) | int(grid[v2-y][idx])
         grid = grid[0:v+1]
             
      if xy.strip() == 'x':
         for y in grid:
            for idx in range(v):
               y[idx] = int(y[idx]) | int(y[v2-idx])
               y.pop(-1)
            y.pop(-1)
      break           
   tot = 0
   for r in grid:
      tot+=sum(r)
   
   print("Result First Star")
   print(tot)   

def second_star():
   global grid
   for xy,v in folds:
      v=int(v)
      v2= v*2
      if xy.strip() == 'y':
         for y in range(v):
            for idx,x in enumerate(grid[y]):
               grid[y][idx] = int(grid[y][idx]) | int(grid[v2-y][idx])
         grid = grid[0:v+1]
             
      if xy.strip() == 'x':
         for y in grid:
            for idx in range(v):
               y[idx] = int(y[idx]) | int(y[v2-idx])
               y.pop(-1)

   print("Result Second Star")
   for row in grid:
      print("".join(" #"[col] for col in row))
if __name__ == '__main__':
    main()