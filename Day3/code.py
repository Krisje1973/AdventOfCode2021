import math
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from  AOCHelper import * 
input = []
def readinput():
   global input
   input = readinput_lines("Day3\input_ex.txt")

def main():
   readinput()   
   first_star()
   second_star()        

def first_star():
   bins = {}
   bins = countbins(bins, input)
   gamma = ""
   epsilon = ""
   h = len(input)/2
   for k in bins:     
      if bins[k]>=h:
         gamma += "1"
         epsilon += "0"
      else:
         gamma += "0"
         epsilon += "1"

  
   print("Result First Star")
   print(int(epsilon,2) * int(gamma,2))

def second_star():
   bins = {}  
   bins = countbins(bins, input)
   co2 = int(loopbins(bins,input,"0"),2)
   bins.clear()
   bins = countbins(bins, input)
   oxy = int(loopbins(bins,input,"1"),2)
  
   print("Result Second Star")
   print(oxy* co2 )

def loopbins(bins,input,val):
   result = ""
   h = len(input)/2
   if len(bins) == 0:
      return result

   if next(iter(bins.values())) >=h:
      result = val
   else:
      result = "0" if val == "1" else "1"

   if next(iter(bins.values())) == h:
      result = val

   input = [x[1:] for x in input if x.startswith(result)]   
   if(len(input)==1):
      return result + input[0]  
   bins.clear()
   bins = countbins(bins,input)
   loop = loopbins(bins,input,val);

   if loop == "":
      return result
   result += loop

   return result

def countbins(bins,input):
   for line in input:
      cnt = 0
      for li in line:
         cnt+=1
         if cnt in bins.keys():
            bins[cnt] = bins[cnt] + int(li)
         else:
            bins[cnt] = int(li)
   return bins

if __name__ == '__main__':
    main()