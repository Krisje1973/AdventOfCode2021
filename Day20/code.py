import math
import os, sys
import itertools
import numpy as np
from itertools import permutations, product
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

def roll_dice():   
   global p1,p2
   cnt,roll = 0,0
   s1,s2 = 0,0
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
            s1 += p1
            if s1>=1000:
               return roll*s2
         else:
            p2 += t 
            p2 = 10 if not p2 %10 else p2%10
            s2 += p2
            if s2>=1000:
               return roll*s1
           
         b1 = b1 == False

def first_star():
   print("Result First Star")
   print(roll_dice())
     
def second_star():
   global p1,p2

   rolls = [sum(p) for p in product([1, 2, 3], repeat=3)]
   
   universes = Counter([(p1, p2, 0, 0)])
   while not all(s1 >= 21 or s2 >= 21 for p1, p2, s1, s2 in universes):
      next_universes = Counter()
      for (p1, p2, s1, s2), count in universes.items():
         if s1 >= 21 or s2 >= 21:
               next_universes[p1, p2, s1, s2] += count
               continue

         for r in rolls:
               np = (((p1 + r) - 1) % 10) + 1
               next_universes[(np, p2, s1 + np, s2)] += count

      universes = next_universes

      next_universes = Counter()
      for (p1, p2, s1, s2), count in universes.items():
         if s1 >= 21 or s2 >= 21:
               next_universes[p1, p2, s1, s2] += count
               continue

         for r in rolls:
               np = (((p2 + r) - 1) % 10) + 1
               next_universes[(p1, np, s1, s2 + np)] += count

      universes = next_universes

   p1_wins = 0
   p2_wins = 0

   for (p1, p2, s1, s2), v in universes.items():
      if s1 >= 21:
         p1_wins += v
      else:
         p2_wins += v


   print("Result Second Star")
   print(max(p1_wins, p2_wins))

def main():
   readinput()
   first_star()
   second_star()     

if __name__ == '__main__':
    main()