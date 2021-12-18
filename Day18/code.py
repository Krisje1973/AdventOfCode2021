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
   li = exp.split('[')[:6]
   cn = Counter(li)[']']
   lr = exp.split(']')[1:6]
  
   if len(li) > 4:
      
      x,y = map(intify, li[5].split(']')[0].split(','))
     
      
      for i in range(4,-1,-1):  
         if li[i] == '': continue      
         xb,yb = map(intify,li[i].split(']')[0].split(','))
         if xb > 0 :
            li[i] = str(xb+x) + ',' + str(yb) 
            break

      for r in range(len(lr)):
         if lr[r] == '' : continue
         if rh.has_string_numeric_regex(lr[r]):
            lr[r] = '[' + str(int(lr[r][1])+y)
            break
     
      s=' '
      for l in li[1:5]:
         s+= '[' + l
      for r in lr:
         s+= r + ','
      print(exp)
      exp = s.strip()
      print('         '+ exp)
      print('expected [[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]]')
      exp += explode(exp)
      


   
  
def intify(s):
   if s!='': return int(s)
   return 0
   

def second_star():
   print("Result Second Star")
  
if __name__ == '__main__':
    main()