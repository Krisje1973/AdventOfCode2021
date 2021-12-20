import math
import ast
import os, sys
from typing  import Counter
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from  AOCHelper import * 
input = ''
def readinput():
   global input
   #input = ast.literal_eval(readinput_lines("Day18\input_ex.txt")[0])
   ls = readinput_lines("Day18\input_ex.txt")
   ls = '[[3,[2,[1,[7,3]]]],[6,[5,[4,[3,2]]]]]'
   for l in ls:
      input+=l
  #if isinstance(ex,list):
def main():
   readinput()
   first_star()
   second_star()        

def first_star():
   explode(input)
   print("Result First Star")
 
def explode(exp):
   rh = RegexHelper()
   open = []
   p = 0
   sb = ''
   
   for c in exp:
      if c == '[':  open.append(p+1)
      p+=1
      sb+=c
      if len(open) == 5: break
      
   if len(open) == 5:
      xy = rh.extract_numerics(exp[open[-1]:open[-1]+3])
      if len(xy) == 2:
         x,y = xy
         while open:
            open.pop(-1)
            xy = rh.extract_numerics(exp[open[-1]:open[-1]+3])
            if len(xy) == 0: continue
            if len(xy) == 1:
               sb = sb[:-2] + '[' + str(xy[0]+x) + ',0]'
               break
            if len(xy) == 2:
               sb = sb[:-2] + '[' + str(xy[0]+x) + ',' + str(y) +']'
               break
      else : return
  

   
  
def intify(s):
   if s!='': return int(s)
   return 0
   

def second_star():
   print("Result Second Star")
  
if __name__ == '__main__':
    main()