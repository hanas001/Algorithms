'''
Дано целое число 1 <= n <= 40,
необходимо вычислить n-е число Фибоначчи (напомним, что F0=0, F1 = 1, Fn = Fn-1 + Fn-2 ghb n >= 2).
'''


import random

n = random.randrange(1, 40, 1)  #random range between 1 and 40
n = 2
numbers = [0, 1]

if n >= 2:
    print (n)
elif n == 1:
    print ( numbers [ 1 ] )
elif n == 0:
    print (numbers[0])
