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
   input = readinput_lines("Day23\input.txt")
   print(input)
   
def first_star():
   image = input
  
   print("Result First Star")
  
def second_star():
   print("Result Second Star")

def main():
   readinput()
   first_star()
   second_star()     

if __name__ == '__main__':
    main()