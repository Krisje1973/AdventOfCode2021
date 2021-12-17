import math
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from  AOCHelper import * 
input = []
def readinput():
   global input,targetX,targetY
   rh = RegexHelper()
   targetX, targetY = map(rh.extract_numerics, open("Day17\input.txt", "r").read().split(","))
   
def main():
   readinput()
   first_star()
   second_star()        

def first_star():
   best, total = 0,0
   for y in range(-200, 200):
      for x in range(0, 200):
         pos = [0, 0]
         step = [x, y]
         maxy = 0
         while pos[0] <= targetX[1] and targetY[0] <= pos[1]:
               maxy = max(maxy, pos[1])
               if check_target(pos):
                  best = max(best, maxy)
                  total += 1
                  break
               pos[0] += step[0]
               pos[1] += step[1]
               if step[0] > 0:
                  step[0] -= 1
               step[1] -= 1
   print("Result First Star")
   print(best, total)

def check_target(pos):
    return targetX[0] <= pos[0] <= targetX[1] and targetY[0] <= pos[1] <= targetY[1]

def second_star():
   print("Result Second Star")
  
if __name__ == '__main__':
    main()