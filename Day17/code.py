import math
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from  AOCHelper import * 
input = []
def readinput():
   global input
   global X,Y
   rh = RegexHelper()
   X, Y = map(rh.extract_numerics, open("Day17\input.txt", "r").read().split(","))
   
def main():
   readinput()
   first_star()
   second_star()        

def first_star():
   best, total = 0
   for y in range(-200, 200):
      for x in range(0, 200):
         pos = [0, 0]
         v = [x, y]
         maxy = 0
         while pos[0] <= X[1] and Y[0] <= pos[1]:
               maxy = max(maxy, pos[1])
               if check_target(pos):
                  best = max(best, maxy)
                  total += 1
                  break
               pos[0] += v[0]
               pos[1] += v[1]
               if v[0] > 0:
                  v[0] -= 1
               v[1] -= 1
   print("Result First Star")
   print(best, total)

def check_target(pos):
    return X[0] <= pos[0] <= X[1] and Y[0] <= pos[1] <= Y[1]

def second_star():
   print("Result Second Star")
  
if __name__ == '__main__':
    main()