import math
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from  AOCHelper import * 
input = []
def readinput():
   global input
   input = readinput_lines("Day5\input.txt")
   
def main():
   readinput()
   first_star()
   second_star()        

def first_star():
   print("Result First Star")
 

def second_star():
   print("Result Second Star")
  
if __name__ == '__main__':
    main()