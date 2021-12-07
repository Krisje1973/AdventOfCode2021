import math
import os, sys
from collections import Counter
from collections import OrderedDict 
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from  AOCHelper import * 
input = []
def readinput():
   global input
   global crabs
   global dist
   input = readinput_lines_as_ints_with_separator("Day7\input.txt",",")
   input.sort()
   crabs = dict(Counter(input))
   dist = defaultdict(int)
def main():
   readinput()
   first_star()
   second_star()       
def first_star():
  
   for crab in range(len(input)+1):
      dist[crab] = sum([abs(crab - c) * crabs[c] for c in crabs if c != crab])
  
   print("Result First Star")
   print(min(dist.values()))

def second_star():
  
   for crab in range(len(input)+1):
      dist[crab] = sum([sum(range(abs(crab - c)+1)) * crabs[c] for c in crabs if c != crab])

   print("Result Second Star")
   print(min(dist.values()))
if __name__ == '__main__':
    main()