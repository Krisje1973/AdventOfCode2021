import math
import os, sys
import copy
import itertools
import numpy as np
from typing  import Counter
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from  AOCHelper import * 
input = []
cols = 0
rows = 0
def readinput():
   global input
   global cols,rows
   sea = []
   input = readinput_lines("Day25\input.txt")
   for line in input:
      sea.append([l for l in line])
   input = sea
   rows,cols =  len(input)-1, len(input[0])-1
  
   
def first_star():
   #> = x+1, V=y+1
  
            
   cnt = 0
   while True:
      cnt+=1
      sea = []
      for line in input:
         sea.append([l for l in line])
      move_east()
      move_south()
      if sea==input: break

   for l in input:
      print(''.join([str(x) for x in l]))
   print(cnt)
  
     
   print("Result First Star")

def move_east():
   global input
   sea = []
   for line in input:
      sea.append([l for l in line])

   for y,r in enumerate(sea):
      for x,c in enumerate(r):
         if c == '.' or c == 'v': continue
         if x== cols: x=-1
         if sea[y][x+1] == '.':
            input[y][x] = '.'
            input[y][x+1] = c
def move_south():
   global input
   sea = []
   for line in input:
      sea.append([l for l in line])

   for y,r in enumerate(sea):
      for x,c in enumerate(r):
         if c == '.' or c == '>': continue
         if y== rows: y=-1
         if sea[y+1][x] == '.':
            input[y][x] = '.'
            input[y+1][x] = c

def second_star():
   print("Result Second Star")

def main():
   readinput()
   first_star()
   second_star()     

if __name__ == '__main__':
    main()