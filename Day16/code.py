import math
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from  AOCHelper import * 
input = []
pos = 0
versions = []
literals = []
def readinput():
   global input
   input = readinput_lines("Day16\input.txt")[0]
   input = "620080001611562C8802118E34"
   input =  bin(int(input, 16))[2:]
   print(len(input)%4)
   
def main():
   readinput()
   first_star()
   second_star()        

def first_star():
   s=0
   v=defaultdict(int)
   l=[]
   decode(input)
   print("Result First Star")
   print(versions)

def decode(bits):
   global versions
   global literals
   while len(bits) > 5:
      versions.append(int(bits[:3], 2))
      bits=bits[3:]
      type = int(bits[:3], 2)
      bits=bits[3:]
      if type == 4:
         lit = ''
         while True:
            e = int(bits[:1], 2)
            lit += bits[:5]
            bits=bits[5:]
            if not e :break
      else:
         l = (15,11)
       
         ns = l[int(bits[:1],2)]
         bits=bits[1:]
         sp = int(bits[1:ns], 2)
         bits=bits[ns:]
         if ns == 15:
            for i in range(sp//11):           
               decode(bits[:11])
               bits=bits[11:]
         else:
            for i in range(sp):
               decode(bits[:11])
               bits=bits[11:]
               
def second_star():
   print("Result Second Star")
  
if __name__ == '__main__':
    main()