arr = [-4, 3, -9, 0, 4, 1]

n = len(arr)

print n, arr

plus = minus = zero = 0.0

for item in arr:
    if item > 0:
        plus += 1
    elif item < 0:
        minus += 1
    else:
        zero += 1

print plus/n
print minus/n
print zero/n
