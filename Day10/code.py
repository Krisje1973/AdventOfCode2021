import math
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from  AOCHelper import * 
input = []
def readinput():
   global input
   global tags
   input = readinput_lines("Day10\input.txt")
   tags = {}
   tags['('] = ('(',1,3)
   tags['['] = ('[',1,57)
   tags['{'] = ('{',1,1197)
   tags['<'] = ('<',1,25137)
   tags[')'] = ('(',-1,1)
   tags[']'] = ('[',-1,2)
   tags['}'] = ('{',-1,3)
   tags['>'] = ('<',-1,4)

   
def main():
   readinput()
   first_star()
   #187575 to low
   #193275 
   second_star()        

def first_star():
   result = defaultdict(int)
   for line in input:
      open_sym = []
      for tag in line:
         if tags[tag][1] > 0:
            open_sym.append(tag)
         else:
            if open_sym[-1] != tags[tag][0] or open_sym.count(tags[tag][0]) ==0:
               result[tags[tag][0]] += tags[tags[tag][0]][2]
               break
            else:            
               del open_sym[len(open_sym) - open_sym[::-1].index(tags[tag][0]) - 1]

   print("Result First Star")
   print(sum(result.values()))

def second_star():
   print("Result Second Star")
  
if __name__ == '__main__':
    main()