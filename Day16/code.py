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

def second_star():
   print("Result First Star")
   print(unpack()[0].Calculate())



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
   
   def Calculate(self) -> int:
      for c in self.children:
         c.Calculate()
      if self.type == 0:  # Sum
            self.evaluated_value = sum([c.evaluated_value for c in self.children])
            return self.evaluated_value
      elif self.type == 1:  # Product
            self.evaluated_value = 1
            for c in self.children:
               self.evaluated_value *= c.evaluated_value
            return self.evaluated_value
      elif self.type == 2:  # Minimum
            self.evaluated_value = min([c.evaluated_value for c in self.children])
            return self.evaluated_value
      elif self.type == 3:  # Maximum
            self.evaluated_value = max([c.evaluated_value for c in self.children])
            return self.evaluated_value
      elif self.type == 4:  # Literal
            self.evaluated_value =  int(self.literal,2)
            return self.evaluated_value
      elif self.type == 5:  # Greater Than
            self.evaluated_value = 1 if self.children[0].evaluated_value > self.children[1].evaluated_value else 0
            return self.evaluated_value
      elif self.type == 6:  # Less Than
            self.evaluated_value = 1 if self.children[0].evaluated_value < self.children[1].evaluated_value else 0
            return self.evaluated_value
      elif self.type == 7:  # Equal To
            self.evaluated_value = 1 if self.children[0].evaluated_value == self.children[1].evaluated_value else 0
            return self.evaluated_value
      else:
            print(f"Unknown packet type: {self.type}")
            a = input()


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
  
if __name__ == '__main__':
    main()