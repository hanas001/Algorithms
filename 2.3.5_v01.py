'''
По данным двум числам 1≤a, b≤2 * 10**9 найдите их наибольший общий делитель.
'''

# a = 35
# b = 18
#
# a = 14159572
# b = 63967072
# 14159572 63967072

ab = input()        #user input
ab = ab.split(' ')  #split a string into a list by whytespace

# print ("AB", ab)
# print (type(ab))

a = int(ab[0])      #assign first list to a and convirt to integer
# print ("A", a)
# print (type(a))
b = int((ab[-1]))   #assign last element of the list to b and convirt to integer
# print ("B", b)

# step = 0    #to count steps

# if a == 0 then return b
if not a:
    gcd = b

# if b == 0 then return a
elif not b:
    gcd = a


else:
    while b != 0 and a != 0:    #loop untill one of the numbers become zero
        if b >= a:              #b should be bigger or equal then a
            n = b % a           # mod from b and a

            # step += 1
            # print ("Step", step)

            b = n               #assign n to b

            # print ("A", a)
            # print("B", b)
            # print("N", n)

        elif a > b:         #changing greater number to b
            a, b = b, a
            # print ("change")
    gcd = a

print (gcd)