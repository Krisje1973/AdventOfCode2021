import math
import os, sys
from typing import Counter
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from  AOCHelper import * 
input = []
def readinput():
   global input
   input = readinput_lines("Day6\input.txt")
   input = list(map(int,input[0].split(",")))
def main():
   readinput()
   first_star()
   second_star()        

def first_star():
   
   fishes = dict(Counter(input))
   for i in range(80):
      repro = defaultdict(int)
      for key, val in fishes.items():
         if key == 0:
            repro[6] += val
            repro[8] += val
         else:
            repro[key - 1] += val
      fishes = repro

   print("Result First Star")
   print(sum(fishes.values()))
 

def second_star():
   print("Result Second Star")
  
if __name__ == '__main__':
    main()