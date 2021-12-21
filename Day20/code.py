import math
import os, sys
import itertools
import numpy as np
from typing  import Counter
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from  AOCHelper import * 
input = []
def readinput():
  
   global input
   global p1,p2
 
   input = readinput_lines("Day21\input.txt")
   p1= int(input[0].split(':')[1])
   p2= int(input[1].split(':')[1])
   print(p1)
   
def first_star():
   global p1,p2
   cnt,roll = 0,0
   t1,t2 = 0,0
   b1=True
   while True:
      roll+=1
      cnt+=1
      if cnt %3 == 0:         
         cnt = 0
         t = roll*3-3
         if b1:
            p1 += t 
            p1 = 10 if not p1 %10 else p1%10
            t1 += p1
            if t1>=1000:
               print(roll*t2)
               return
         else:
            p2 += t 
            p2 = 10 if not p2 %10 else p2%10
            t2 += p2
            if t2>=1000:
               print(roll*t1)
               return
           
         b1 = b1 == False
            
         

      #p1 += i%10
      

  
   print("Result First Star")
   


   
def second_star():
   print("Result Second Star")

def main():
   readinput()
   first_star()
   second_star()     

if __name__ == '__main__':
    main()