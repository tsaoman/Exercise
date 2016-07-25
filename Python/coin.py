from random import randint
import sys

try:
    n = int(sys.argv[1])
except:
    n = 1

bits = []

while(len(bits) < n):
    if randint(0,1):    #first toss = 1
        if not randint(0,1):    #second toss = 0
            bits.append(0)

    else: #first toss = 0
        if randint(0,1): #second toss = 1
            bits.append(1)

print ''.join(map(str,bits))
