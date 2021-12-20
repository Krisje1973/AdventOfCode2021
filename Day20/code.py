import math
import os, sys
import itertools
import numpy as np
from typing  import Counter
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from  AOCHelper import * 
input = []
def readinput():
   bin = Binary()
   global input
   global algo
   input = readinput_lines("Day20\input.txt")
   algo = input[0]
   input = input[2:]
   algo = algo.replace(".","0").replace("#","1")
   for i in range(len(input)):
      input[i] = input[i].replace(".","0").replace("#","1")
   
def first_star():
   image = input
   for _ in range(2):
      image = enhance(image)

   for row in image:
      print("".join(".#"[int(col)] for col in row))
   cnt=0
   for l in image:
      for s in l:
         if s == '1':
            cnt +=1
   print("Result First Star")
   #5867 to high :(
   print(cnt)

def expand(image):
   l = len(image)
   expanded = [image[0].center(l+6,"0").replace("1","0")]
   expanded.append(expanded[0])
  
   for i in range(l):
      expanded.append(image[i].center(l+4,"0"))
  
   expanded.append(expanded[0])
   expanded.append(expanded[0])
   return expanded
   
def enhance(image):
   image = expand(image)  
   newimage = [s.replace("1","0") for s in [line for line in image]]
   l = len(image) - 2
   for x in range(l):
      for y in range(l):
         s= ''
         for j in range(3):
            for i in range(3):
               s += image[y+j][x+i]
         newimage[y+1] = newimage[y+1][:x+2] + algo[int(s,2)] + newimage[y+1][x+2:]
         newimage[y+1] = newimage[y+1][0:l+4]
   return newimage
  
   
def second_star():
   print("Result Second Star")

def main():
   readinput()
   first_star()
   second_star()     

if __name__ == '__main__':
    main()