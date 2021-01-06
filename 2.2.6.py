'''
Дано целое число 1 <= n <= 40,
необходимо вычислить n-е число Фибоначчи (напомним, что F0 = 0, F1 = 1, Fn = Fn-1 + Fn-2 ghb n >= 2).
'''


import random

#n = random.randrange(1, 40, 1)                         #random range between 1 and 40, step 1
n = 30                                                  #for the tests
#n = int(input("Type number "))                         #user input


def fibonacciNumbers(n):
    numbers = [ 1 , 1 ]                                 #Fibonacci sequience starts with
    nextNum = 0
    if n >= 2:                                          #calculate only if n is more then 2
        for i in range(n):                              #range of n steps
            if i >= 2:                                  #add calculated number to the list only starting after second step
                nextNum = numbers[i-1] + numbers[i-2]   #calculate next number in a line
                numbers.append(nextNum)                 #append calculated number to the list
        return (numbers[-1])                            #return last number
    elif n == 1:
        return numbers [ -1 ]                           #return last number from the list
    elif n == 0:
        return numbers [ 0 ]                            #return 0 position from the list

#print ("Full Fibonacci line", numbers)
print ("Fibonacci number at step", n, "is", fibonacciNumbers(n))