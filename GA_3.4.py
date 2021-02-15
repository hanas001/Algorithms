def sum(xarr):
    # xarr = 0
    total = 0
    for x in xarr:
        total += x
    return total

xarr = [1, 2, 122, 4, 6, 9, 11]

print (sum(xarr))

def max(arr):
    xmax = 0
    for x in arr:
        print ("x", x)
        if xmax < x:
            xmax = x
        else:
            return xmax


print ("Maximum", max(xarr))