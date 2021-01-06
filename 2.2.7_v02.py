'''
Дано число 1≤ n ≤ 10 7, необходимо найти последнюю цифру n-го числа Фибоначчи.
Как мы помним, числа Фибоначчи растут очень быстро, поэтому при их вычислении
нужно быть аккуратным с переполнением. В данной задаче, впрочем, этой проблемы
можно избежать, поскольку нас интересует только последняя цифра числа Фибоначчи:
если 0≤a, b≤9 — последние цифры чисел Fi и Fi+1 соответственно,
то (a+b)mod 10 последняя цифра числа Fi +2
'''

import random

n = random.randrange(1, 40, 1)      #random range between 1 and 40, step 1
n = 841645                          #for the tests
n = 90
#n = int(input("Type number "))     #user input


numbers = [ 1 , 1 ]
# steps = len(numbers)

for i in range(n):
    if i > 2:
        sum = (int(numbers[-2])) + (int(numbers[-1])) % 10
        numbers.append(sum)
    # steps += 1


print("Last digits in Fibonacci line", numbers)
print ("Fibonacci number at step", n, "is", numbers[-1])
# print (sum)