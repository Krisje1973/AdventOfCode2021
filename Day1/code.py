import math
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from  AOCHelper import * 
input = []
def readinput():
   global input
   input = readinput_lines_as_ints("Day1\input.txt")
  
def main():
   readinput()
   first_star()
   second_star()        
          
def first_star():
   print("Result First Star")
   print(CountIncreases(input))

def second_star():
   dim = []
   for idx,num in enumerate(input[0:math.trunc(len(input)/3)*3]):
      dim.append(num+input[idx+1]+input[idx+2])
  
   print("Result Second Star")
   print(CountIncreases(dim))

def CountIncreases(input):  
   count = 0
   for idx,num in enumerate(input[1:]):
      if num > input[idx]:
         count+=1    
   return count

if __name__ == '__main__':
    main()