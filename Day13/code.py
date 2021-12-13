import math
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from  AOCHelper import * 
input = []
def readinput():
   global input
   global grid
   global folds
   input = readinput_lines("Day13\input_ex.txt")
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
   first_star()
   second_star()        

def first_star():
  
   for xy,v in folds:
      v=int(v)
      if xy.strip() == 'y':
        
         f1 = grid[:v+1]
         f2 = grid[v:]
         f2.reverse()
         new_grid = [[0 for x in range(len(f1[0]))] for x in range(v+1)]
         for y,f in enumerate(f2):
            for i,c in enumerate(f):       
               new_grid[y][i] = int(f1[y][i]) | c
             
             
         print(new_grid)
       
   print("Result First Star")
 

def second_star():
   print("Result Second Star")
  
if __name__ == '__main__':
    main()