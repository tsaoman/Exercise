n = 3
a = [[11, 2, 4], [4, 5, 6], [10, 8, -12]]

sum1 = sum2 = 0

for i in xrange(n):
    sum1 += a[i][i]
    sum2 += a[i][n-i-1]

print abs(sum1 - sum2)
