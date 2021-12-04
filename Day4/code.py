import math
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from  AOCHelper import * 
input = []
def readinput():
   global input
   global nums
   global boardsinput
   input = readinput_lines_skip_enters("Day4\input.txt")
   
   nums = list(map(int, input[0].split(",")))
   boardsinput = input[1:]
   
def main():
   readinput()
   first_star()
   second_star()        

def first_star():
   boards = {}
   cnt=0
   bo=1
   for board in boardsinput:
      cnt+=1      

      if not bo in boards.keys():
         boards[bo] = [list(map(int,board.split()))]
      else:
         boards[bo] += [list(map(int,board.split()))]

      if (cnt % len(board.split()) ) == 0:
         boards[bo] += list(map(list, zip(*boards[bo])))       
         bo+=1

   print("Result First Star")
   print(findbingo(boards))

def findbingo(boards):
   cnt = 0
   last = False
   check = boards
   for num in nums:      
      for boardkey in boards.keys():
         board = boards[boardkey]
         if not boardkey in check.keys():
            continue
         for b in board:
            for n in b:
               if n==num:
                  b.remove(n)
            if sum(b) == 0:
               tot = {}
               for x in board:
                  for y in x:
                     if y != num:
                        tot[y] = y
               som = sum(tot.values())
               result = (sum(tot.values())) * int(num)
               if len(check) == 1:
                  return result
               check = removekeyfromdict(check, boardkey)

               
def second_star():

   print("Result Second Star")
 

if __name__ == '__main__':
    main()