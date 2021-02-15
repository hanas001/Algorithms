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
print (s)


############################################################################################
points = []
nTmp = 0
k = 0


for i in range(len(s)):
  print ("i", i)
  nTmp = s [ k ] [ -1 ]         #current right point
  print ( "nTmp" , nTmp )
  points += str ( nTmp )

  if nTmp < s[i][0]:
    k = i
    print ("k", k)
    points += str(nTmp)

  # print ("k_after", k)
  
pointsSet = set(points)         #include unique points to a set


############################################################################################
print (len(pointsSet))
print (*pointsSet)
