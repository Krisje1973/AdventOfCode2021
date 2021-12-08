import math
import os, sys
from typing import Counter
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from  AOCHelper import * 
input = []
def readinput():
   global input
   global sigs
   global digs
   input = readinput_lines ("Day8\input_ex.txt")
   sigs = []
   digs = []
   for line in input:
      s,d = line.split("|")
      sigs.append(s.strip())
      digs.append(d.strip())
def main():
   readinput()
   first_star()
   second_star()        

def first_star():
   tot = 0
   for v in digs:
      for val in v.split():
         val = val.strip()       
         if len(val) == 2 or len(val) == 3 or len(val) == 4 or len(val) == 7:
            tot += 1
   print("Result First Star")
   print(tot)
   
def second_star():
   print("Result Second Star")
  
if __name__ == '__main__':
    main()