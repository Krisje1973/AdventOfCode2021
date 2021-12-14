import math
import os, sys
from typing import Counter
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from  AOCHelper import * 
input = []
def readinput():
   global input
   global template
   global rules
   input = readinput_lines_skip_enters("Day14\input.txt")
   template = input[0]
   rules = {}
   for rule in input[1:]:
      k,v =  rule.split(' -> ')
      rules[k] = v
   
def main():
   readinput()
   #first_star()
   second_star()        

def first_star():
   val = Counter(formule(10))
   print("Result First Star")
   print(int(max(val.values()))- int(min(val.values())))
 
def second_star():
   readinput()
   #4807056953867 = to high
   result = formule2(40)
  
   print("Result Second Star")
   print(int(max(result.values()))- int(min(result.values()))) 

def formule(count):
   global template
   for _ in range(count):
      s= template[0]
      for x, y in zip(template, template[1:]):
         xy = x+y
         if xy in rules:
            s += str(rules[xy]) +y
         else:
            s=+ x
         
      template = s
            
   return template

def formule2(count):
   global template
   pairs = defaultdict(int)
   for pair in [x+y for x,y in zip(template, template[1:])]:
      pairs[pair] += 1
   for i in range(count):
      new_pairs = defaultdict(int)
      for pair in pairs:
         if pair in rules:
            new_pairs[pair[0] + rules[pair]] += pairs[pair]
            new_pairs[rules[pair] + pair[1]] += pairs[pair]
         else: 
            new_pairs[pair] = pairs[pair]
      pairs = new_pairs

   result = defaultdict(int)
   for k,v in pairs.items():
      result[k[0]] += v
   result[template[-1]] += 1
   
   return result
if __name__ == '__main__':
    main()