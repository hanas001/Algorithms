'''
Дано целое число 1 <= n <= 40,
необходимо вычислить n-е число Фибоначчи (напомним, что F0 = 0, F1 = 1, Fn = Fn-1 + Fn-2 ghb n >= 2).
'''


import random

#n = random.randrange(1, 40, 1)  #random range between 1 and 40, step 1
n = 30                          #for the tests
#n = int(input("Type number "))    #user input


def fibonacciNumbers(n):
    numbers = [ 1 , 1 ]
    nextNum = 0
    if n >= 2:
        for i in range(n):
            if i >= 2:
                nextNum = numbers[i-1] + numbers[i-2]
                numbers.append(nextNum)
        return (numbers[-1])
    elif n == 1:
        return numbers [ 1 ]
    elif n == 0:
        return numbers [ 0 ]

#print ("Full Fibonacci line", numbers)
print ("Fibonacci number at step", n, "is", fibonacciNumbers(n))