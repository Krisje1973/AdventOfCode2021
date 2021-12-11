import math
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from  AOCHelper import * 
input = []
def readinput():
   global input
   global nums
   global maxx
   global maxy 
   input = readinput_lines_skip_enters("Day9\input.txt")
   nums = list(map(int, input))
   nums = input
   maxx=len(str(nums[0]))
   maxy=len(nums)

def main():
   readinput()
   first_star()
   #second_star()        
   #1315672 = to low
def first_star():
   lows = []
   for x in range(maxx):
      for y in range(maxy):
         cur = int(str(nums[y])[x])
         if all([num > cur for num in get_adjacent_nums(x,y)]):
            lows.append(cur+1)

   print("Result First Star")
   print(sum(lows))
   
def second_star():
   bassins = []  
   for x in range(maxx+1):
      for y in range(maxy+1):
         ne = [int(str(nums[y])[x-1]) if x>0 else 9,int(str(nums[y])[x+1])if x<maxx else 9,int(str(nums[y-1])[x]) if y>0 else 9,int(str(nums[y+1])[x]) if y<maxy else 9]        
         if int(str(nums[y])[x]) < min(ne):
            bas = defaultdict(int)
            basv = defaultdict(int)
            print(x,y)
            print(list(get_adjacent(x,y)))
            bas[(x,y)] = 1
           
            for x,y in navigate(x,y,-1,0):  
               bas[(x,y)] = 1
            for x,y in navigate(x,y,+1,0):
               bas[(x,y)] = 1

            for x,y in bas.keys():
               for k,v in navigate(x,y,0,-1):
                  basv[(k,v)] = 1
               for k,v in navigate(x,y,0,+1):
                  basv[(k,v)] = 1

            for x,y in basv:
                bas[(x,y)] = 1

            for x,y in basv:
               for k,v in navigate(x,y,-1,0):
                  bas[(k,v)] = 1
               for k,v in navigate(x,y,+1,0):
                  bas[(k,v)] = 1

            bassins.append(sum(bas.values()))
   print(max(bassins))
   bassins.sort(reverse=True)
   #bassins[0] = bassins[0] + 1
   print("Result Second Star")
   print(bassins[0]*bassins[1]*bassins[2])

def get_adjacent_nums(x, y):
    for nx, ny in (x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1):
        if 0 <= nx < maxx and 0 <= ny < maxy:
            yield int(str(nums[ny])[nx])

def get_adjacent(x, y):
    for nx, ny in (x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1):
        if 0 <= nx < maxy and 0 <= ny < maxx:
            yield (nx, ny)

def navigate(x,y,x1,y1):
  
   bas = defaultdict(int)
   y+=y1
   while y1 !=0 and y <= maxy and y>=0:
      
      if int(str(input[y])[x]) < 9:
         bas[(x,y)] = 1
      else:
         break
      y+=y1

   x+=x1
   while x1!=0 and x <= maxx and x>=0:
      if int(str(input[y])[x]) < 9:
         bas[(x,y)] = 1
      else:
         break
      x+=x1

   return bas
       

if __name__ == '__main__':
    main()