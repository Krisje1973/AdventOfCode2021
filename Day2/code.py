import math
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from  AOCHelper import * 
input = []
def readinput():
   global input
   input = readinput_lines("Day2\input.txt")
  
def main():
   readinput()
   first_star()
   second_star()        

def first_star():
   oper = {}
   oper["forward"] = [1,0]
   oper["down"] = [1,0]
   oper["up"] = [-1,0]
   
   # make it unreadable :) :) 
   for t in map(lambda x: x.split(),input):
      oper[t[0]] = [oper[t[0]][0],oper[t[0]][1] + int(t[1])*oper[t[0]][0]]
   
   print("Result First Star")
   print(oper["forward"][1] * (oper["down"][1]+oper["up"][1]))

def second_star():
   ho,ve,aim=0,0,0
   for op,q in [x.split() for x in input]:
      q=int(q)
    
      if op == "forward":
         ho+=q
         ve+=aim*q
      if op == "up":
         aim-=q
      if op == "down":
         aim+=q
  
   print("Result Second Star")
   print(ho*ve)
if __name__ == '__main__':
    main()