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
   input = "8A004A801A8002F478"
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
   while s < len(input)-5:
      s,v,l = decode(input,s)
   print("Result First Star")
   print(s,v,l)

def decode(bits,start):
   global versions
   global literals
   if len(bits) < 6 : return
   versions.append(int(bits[start:start+3], 2))
   start+=3
   type = int(bits[start:start+3], 2)
   start+=3
   if type == 4:
      lit = ''
      while True:
         e = int(bits[start:start+1], 2)
         lit += bits[start:start+5]
         start += 5
         if not e :break
   else:
      l = (15,11)
      versions.append(int(bits[start:start+1],2))
      ns = l[versions[-1]]
      start+=1
      sp = int(bits[start:start+ns], 2)
      start+=ns
      if ns == 15:
         for i  in range(sp//11):           
            decode(bits[start+(11*i):start+(11*i)+11],0)
         start+=sp
         
      else:
         for i in range(sp):
            decode(bits[start+(11*i):start+(11*i)+11],0)
         start+=sp
         
   return start


            




         
   
def second_star():
   print("Result Second Star")
  
if __name__ == '__main__':
    main()