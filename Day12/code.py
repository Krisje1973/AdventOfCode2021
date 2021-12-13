import math
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from  AOCHelper import * 
input = []
paths = defaultdict(list)
def readinput():
   global input
   global paths
   input = readinput_lines("Day12\input_ex.txt")
   
   for inp in list([a for a in [line.split('-') for line in input]]):
      paths[inp[0]].append(inp[1])
      paths[inp[1]].append(inp[0])

def main():
   readinput()
   first_star()
   second_star()        

def first_star():
   print("Result First Star")
   print(checkpath('start',{'start'}))

def checkpath(cur,seen):
   if cur == 'end': 
      return 1

   return sum(checkpath(path, seen | {path.lower()}) for path  in [p  for p in paths[cur] if p not in seen])

def checkpath2(cur,seen,double):
   if cur == "end":
      return 1

   total = 0
   for path in paths[cur]:
      if path.islower():
         if path not in seen:
            total += checkpath2(path, seen | {path}, double)
         elif double and path != "start":
            total += checkpath2(path, seen, False)
      else:
         total += checkpath2(path, seen, double)
   return total 

def second_star():
   print("Result Second Star")
   print(checkpath2('start',{'start'},True))
  
if __name__ == '__main__':
    main()