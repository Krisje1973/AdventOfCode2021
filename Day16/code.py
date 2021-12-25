import math
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from  AOCHelper import * 
input = []
pos = 0
versions = []
literals = []
re = IndexedReader('')
def readinput():
   global input
   input = readinput_lines("Day16\input.txt")[0]
  
   input =  bin(int(input, 16)).replace('b','0')[2:]
   input = input.zfill(len(input) + len(input)%4)

def main():
   readinput()
   first_star()
   second_star()        

def first_star():
   print("Result First Star")
   print(unpack()[0].VersionTotal())
   
class Package():
   def __init__(self,v:int,t:int):
      self.type = int(t,2)
      self.version = int(v,2)
      self.literal = ''
      self.children = []
      self.evaluated_value = None
      self.literal_type = 4
      self.mode = 1
      self.sub_length = 11
   
   def isLiteral(self) -> bool:
      return self.type==self.literal_type
   
   def VersionTotal(self) -> int:
      return sum([c.VersionTotal() for c in self.children]) + self.version


def unpack():
   global re
   packages = []
   re = IndexedReader(input)
   while not re.eof():
      v,t = re.read(3),re.read(3)
      if int(v.zfill(1)) == 0 and int(t.zfill(1))==0:
         break

      pack = Package(v,t)
      if pack.isLiteral():
         decode_literal(pack)
      else:
         decode_operator(pack)

      packages.append(pack)

   return packages

def decode_literal(pack:Package):
   while int(re.read(1)):
      pack.literal+=re.read(4)
   pack.literal+=re.read(4)
   
def decode_operator(pack:Package):
   if not int(re.read(1)): 
      pack.mode = 0
      pack.sub_length = int(re.read(15),2)
      s=re.getindex()
      while re.getindex() < s+pack.sub_length:
         sub = Package(re.read(3),re.read(3))
         if sub.isLiteral(): 
            decode_literal(sub)
         else:
            decode_operator(sub)
         pack.children.append(sub)
   else: 
      pack.sub_length = int(re.read(11),2)
      for i in range(pack.sub_length):
         sub = Package(re.read(3),re.read(3))
         if sub.isLiteral(): 
            decode_literal(sub)
         else:
            decode_operator(sub)
         pack.children.append(sub)







  


def decode(bits):
   global versions
   global literals

   while len(bits) > 5:
      versions.append(int(bits[:3], 2))
      bits=bits[3:]
      type = int(bits[:3], 2)
      bits=bits[3:]
      if type == 4:
         #prefix 1, then 4 digits, last = prefix 0
         lit = ''
         while True:
            e = int(bits[:1], 2)
            lit += bits[1:5]
            bits=bits[5:]
            if not e :
               literals.append(lit)
               break
      else:
         l = (15,11)
       
         ns = l[int(bits[:1],2)]
        
         sp = bits[1:ns+1]
         sp = int(sp, 2)
         bits=bits[ns+1:]
         if ns == 15:
            for i in range(sp//11):           
               decode(bits[:11])
            bits=bits[sp:]
         else:
            for i in range(sp):
               b= bits[11:11*i+1]
               bits=bits[11:]
               decode(b)
               
               
def second_star():
   print("Result Second Star")
  
if __name__ == '__main__':
    main()