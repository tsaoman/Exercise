n = 6

a = [" "] * (n)


for i in range(n):
    a[n-i-1] = "#"
    print "".join(a)
