import math
import os, sys
from typing import Iterator
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from  AOCHelper import * 
input = []
def readinput():
   global input
   global octo
   global maxx
   global maxy

   input = readinput_lines("Day11\input.txt")
   octo=[]
   for o in input:
      octo.append(list(map(int, o)))
   
   maxx = len(octo[0])
   maxy = len(octo) 
   
def main():
   readinput()
   first_star()
   second_star()        

def first_star():
   gh = GridHelper()
   cnt = 0
   while True:
      cnt+=1
    
      for r in octo:
         for c in range(maxy):      
            r[c] += 1 
      #b = list([o for o in r for r in octo if o>9] )
      flashed = defaultdict(int)
      flash = list([(r,c) for c in range(maxx) for r in range(maxy) if octo[r][c]>9])
      
      while True:
         for r,c in flash:
            flashed[(r,c)] = 1
            ne = gh.get_adjacent_pos_with_diag(c,r,maxx,maxy)
            for x,y in ne:
               octo[y][x] += 1
            octo[r][c] = 0

         flash = list([(r,c) for c in range(maxx) for r in range(maxy) if octo[r][c]>9])
         if len(flash)== 0 : break

      #cnt += len(flashed)
      for r,c in flashed:
         octo[r][c] = 0  
      
      if len(flashed) == 100: 
         break
       
   print("Result First Star")
   print(cnt)
def second_star():
   print("Result Second Star")
  
if __name__ == '__main__':
    main()


         