'''

'''

import string
import sys
from operator import itemgetter


############################################################################################
input = open('4.txt', 'r')  # расскомментировать решая задачу локально
# input = sys.stdin         # расскомментировать при сдаче задачи в системе

s = []
n = int(input.readline())
for i in range(1,n+1):
  x,y = map(int, input.readline().split())
  s.append([x,y])

# print (s)

s = sorted (s, key=itemgetter(1))     # sort list by second point
# print (s)


############################################################################################
points = []
nTmp = 0
k = 0

sNew = []

while len(s) > 0:
  nTmp = s [ k ] [ -1 ]         #current right point
  print ( "nTmp" , nTmp )

  if k < len(s) - 1:
    while nTmp >= s[k + 1][0]:    #if current right point is >= that next left point then ...
      points += str(nTmp)         #add points to a list
      k += 1                      #increase counter by 1

  # sNew.append ( s [ k ] )  # add range to new list
  # print ( "sNew" , sNew )

  print ("s", s)
  # s.remove (sNew)

# print (numberPoints)
pointsSet = set(points)   #include unique points to a set

print (len(pointsSet))

print (*pointsSet)
# print (type(pointsSet))
