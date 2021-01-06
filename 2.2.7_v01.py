'''
Дано число 1≤ n ≤ 10 7, необходимо найти последнюю цифру n-го числа Фибоначчи.
Как мы помним, числа Фибоначчи растут очень быстро, поэтому при их вычислении
нужно быть аккуратным с переполнением. В данной задаче, впрочем, этой проблемы
можно избежать, поскольку нас интересует только последняя цифра числа Фибоначчи:
если 0≤a, b≤9 — последние цифры чисел Fi и Fi+1 соответственно,
то (a+b)mod 10 последняя цифра числа Fi +2
'''

import random

# n = random.randrange(1, 40, 1)     #random range between 1 and 40, step 1
n = 10**7                              #for the tests
#n = int(input("Type number "))     #user input


numbers = [ 0 , 1 ]
numbersLast = [0, 1]
numbersTemp = 0
nextNum = 0

if n >= 2:
    for i in range(n):
        if i >= 2:
            nextNum = numbers[i-1] + numbers[i-2]
            numbers.append(nextNum)
            numbersTemp = (str(nextNum)[-1])
            # print (str(nextNum)[-1])
            numbersLast.append(numbersTemp)
    f = (numbers[-1])

print ("Last digits in Fibonacci line", numbersLast)

m = 841645
lstNum = (str(f)[m])

print ("Last digit of Fibonacci number is", lstNum)