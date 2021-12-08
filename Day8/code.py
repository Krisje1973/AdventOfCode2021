import math
import os, sys
from typing import Counter
from operator import and_, or_
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from  AOCHelper import * 
input = []
def readinput():
   global input
   global sigs
   global digs
   input = readinput_lines ("Day8\input.txt")
   sigs = []
   digs = []
   for line in input:
      s,d = line.split("|")
      sigs.append(s.strip())
      digs.append(d.strip())
def main():
   readinput()
   #first_star()
   second_star()        

def first_star():
   tot = 0
   for v in digs:
      for val in v.split():
         val = val.strip()       
         if len(val) == 2 or len(val) == 3 or len(val) == 4 or len(val) == 7:
            tot += 1
   print("Result First Star")
   print(tot)
   #print(sum([1 for key in [d.split() for d in digs] if len(key) == 2 or len(key) == 3 or len(key) == 4 or len(key) == 7]))
  

def second_star():
 
   results = []
   cnt = 0
   for dig in digs:
      digits = getdigits(sigs[cnt].split())
      result = ''
      for di in dig.split():
         for d in digits:
            if len(di) == len(d) and containsAll(di,d) == len(di):
               result += str(digits[d])

      results.append(result)
      cnt +=1
   print("Result Second Star")
   print(sum(map(int,results)))
def getdigits(signals):
   result = defaultdict(str)
   digits = defaultdict(int)
   digits[1] = str([c  for c in signals if len(c) == 2][0])
   digits[4] = str([c  for c in signals if len(c) == 4][0])
   digits[7] = str([c  for c in signals if len(c) == 3][0])
   digits[8] = str([c  for c in signals if len(c) == 7][0])
   top = digits[7]
   for c in  digits[1]:
      top = top.replace(c,'')

   for sig in [c  for c in signals if len(c) == 6]:
      e = digits[8]
      for c in sig:
         e = e.replace(c,'')
      
      if digits[4].count(e) == 0:
         digits[9] = sig
      else:
         if digits[1].count(e) == 0:
            digits[0] = sig
         else:
            digits[6] = sig

   for sig in [c  for c in signals if len(c) == 5]:
      e = digits[6]
      for c in sig:
         e = e.replace(c,'')

      if len(e) == 2:
         e = digits[7]
         for c in sig:
            e = e.replace(c,'')
         if len(e) == 0:
            digits[3] = sig
         else:
            digits[2] = sig

      elif digits[1].count(e) == 0:
         digits[5] = sig   

   for dig in digits:
      result[digits[dig]] = dig

   return result

def containsAll(str1, str2):
   return  sum([characters in str1 for characters in str2])

if __name__ == '__main__':
    main()