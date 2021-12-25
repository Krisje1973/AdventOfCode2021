import math
import os, sys
import itertools
import numpy as np
from itertools import permutations
from typing  import Counter
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from  AOCHelper import * 
input = []
def readinput():
   global input
   global rh
   global vars
   global all
  
   input = readinput_lines("Day24\input.txt")
   vars = defaultdict(int)
   rh = RegexHelper()
   all = defaultdict(int)
   #359639319555114052907624 = 10000000000000 dan -12 voor volgende
   #y=359639319555114052907624
   #for i in range(10000000000000,99999999999999):
   print(18%26)
   l = []
   l.append('51131616112781')
  

   for s in l:
      process(s)
   print(all)

  
def process(model):
  
   W = [9, 9, 5, 9, 8, 9, 9, 3, 9, 9, 9, 9, 9, 9] 
   W = [9, 3, 1, 5, 1, 4, 1, 1, 7, 1, 1, 2, 3, 7] 
   X= [11,12,10,-8,15,15,-11,10,-3,15,-3,-1,-10,-16]
   Z= [1,1,1,26,1,1,26,1,26,1,26,26,26,26]
   Y = [8,  8, 12,  10,  2, 8,  4, 9, 10, 3, 7, 7, 2, 2]
   while True:

      x = 0
      y = 0
      z = 0
      for i in range(0,14):
         z26 = z%26
         goal = z26 + X[i]
         if 1<=goal<=9:
            W[i] = goal

         z //= Z[i]
         x = (0 if W[i]==goal else 1)
         z *= (25 if x==1 else 0) + 1
         z += (W[i]+Y[i] if x==1 else 0)
         print(f'i={i} goal={goal} z%26={z26} X[i]={X[i]} Y[i]={Y[i]} W[i]={W[i]} Z[i]={Z[i]} z={[(z//26**i)%26 for i in range(14)]}')
         if X[i] < 10 and W[i]!=goal:
            break
      print(W, z, ''.join([str(x) for x in W]))
      if z==0:
         sys.exit(0)
      print()
      sys.exit(0)
   

def processold(model):
   global vars
   global all
   ml = [int(s) for s in model]
   assert len(ml)== 14
   
   for instr in input:
      s = instr.split()
      if len(s) == 2:
         vars[s[1]] = ml.pop(0)
      else:
         op = s[0]
         d = vars[s[1]]
         m = int(s[2]) if rh.is_string_numeric_regex(s[2]) else vars[s[2]]
         if op == 'mul':
            vars[s[1]] *=m
         elif op == 'add':
            vars[s[1]] +=m
         elif op == 'div' and d != 0:
            vars[s[1]] = int(d//m)
         elif op == 'mod'  :
            vars[s[1]] = d%m 
         elif op == 'eql ':
            vars[s[1]] = int(d==m)
   all[('x',vars[s[1]])] = vars['x']
   all[('y',vars[s[1]])] = vars['y']
   all[('z',vars[s[1]])] = vars['z']
   all[('w',vars[s[1]])] = vars['w']

   if vars['z'] <= 10000000 and vars['z'] > 0:
      print('************* MODEL ******** ' + model)
      print(vars['z'])


  
   
def first_star():
   
   print("Result First Star")
   print()

def second_star():
   
   print("Result Second Star")

def main():
   readinput()
   first_star()
   second_star()     

if __name__ == '__main__':
    main()