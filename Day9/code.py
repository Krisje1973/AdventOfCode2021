import math
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from  AOCHelper import * 
input = []
def readinput():
   global input
   global nums
   input = readinput_lines_skip_enters("Day9\input.txt")
   nums = list(map(int, input))
   nums = input
def main():
   readinput()
   first_star()
   second_star()        

def first_star():
   maxx=len(str(nums[0]))-1
   maxy=len(nums)-1
   lows = []
   for x in range(maxx+1):
      for y in range(maxy+1):
         ne = [int(str(nums[y])[x-1]) if x>0 else 9,int(str(nums[y])[x+1])if x<maxx else 9,int(str(nums[y-1])[x]) if y>0 else 9,int(str(nums[y+1])[x]) if y<maxy else 9]        
         if int(str(nums[y])[x]) < min(ne):
            lows.append(int(str(nums[y])[x])+1)

   print("Result First Star")
   print(sum(lows))
   
def second_star():
   print("Result Second Star")
  
if __name__ == '__main__':
    main()