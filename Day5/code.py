import math
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from  AOCHelper import * 
input = []
def readinput():
   global input
   global cords
   input = readinput_lines("Day5\input_ex.txt")
   cords = []
   for line in input:
      l, r = line.split(" -> ")
      cords.append(list(map(int,l.split(","))) + list(map(int,r.split(","))))
   
def main():
   readinput()
   first_star()
   second_star()   
  

def first_star():
   m = max(max(cords[0],cords[1],cords[2],cords[3]))
   grid = {}
   for c in cords:
      x1,y1,x2,y2 = map(int,c)
      if x1 == x2 or y1 ==y2:
         for x in range(min(x1, x2), max(x1, x2) + 1):
            for y in range(min(y1, y2), max(y1, y2) + 1):
               grid[(x, y)] = grid.get((x, y), 0) + 1

   tot = len([key for (key, value) in grid.items() if value > 1])
  
   print("Result First Star")
   print(tot)

def second_star():
  
   grid = {}
   for c in cords:
      x1,y1,x2,y2 = map(int,c)
      if x1 == x2 or y1 ==y2:
         for x in range(min(x1, x2), max(x1, x2) + 1):
            for y in range(min(y1, y2), max(y1, y2) + 1):
               grid[(x, y)] = grid.get((x, y), 0) + 1
      else:
         xg,yg = [],[]
         step = 1 if x2-x1 >= 0 else -1
         x2 += step
         for x in range(x1,x2,step):
            xg.append(x)
         step = 1 if y2-y1 >= 0 else -1
         y2+=step
         for y in range(y1,y2,step):
            yg.append(y)
      
         for xy in list(zip(xg,yg)):           
            grid[xy] = grid.get(xy, 0) + 1

   tot = len([key for (key, value) in grid.items() if value > 1])
  
   print("Result Second Star")
   print(tot)

if __name__ == '__main__':
    main()