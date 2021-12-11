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
   global result

   input = readinput_lines("Day11\input.txt")
   octo=[]
   for o in input:
      octo.append(list(map(int, o)))
   
   maxx = len(octo[0])
   maxy = len(octo) 
   
def main():
   global result
   readinput()
   result =  list(map(int,count_flashes(100)))
   first_star()
   second_star()        

def first_star():
   print("Result First Star")
   print(result[0])
def second_star():
  
   print("Result Second Star")
   print(result[1])

def count_flashes(q):
   gh = GridHelper()
   cnt=0
   cnt1=0
   while True:
      cnt+=1
    
      for r in octo:
         for c in range(maxy):      
            r[c] += 1 

      flashed = defaultdict(int)
      flash = list([(r,c) for c in range(maxx) for r in range(maxy) if octo[r][c]>9])
      
      while True:
         for r,c in flash:
            flashed[(r,c)] = 1
            for x,y in  gh.get_adjacent_pos_with_diag(c,r,maxx,maxy):
               octo[y][x] += 1
            octo[r][c] = 0

         flash = list([(r,c) for c in range(maxx) for r in range(maxy) if octo[r][c]>9])
         if len(flash)== 0 : break

      cnt1 += len(flashed)
      for r,c in flashed:
         octo[r][c] = 0  

      if cnt==q:
         yield cnt1
      
      if len(flashed) == 100 : 
         yield cnt
         break
   
if __name__ == '__main__':
    main()


         