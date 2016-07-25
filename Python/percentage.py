master = {}

n = int(raw_input())
for i in xrange(n):

    s = raw_input().split()

    master[s[0]] = (float(s[1])+float(s[2])+float(s[3]))/3

request = raw_input()

print forma(master[request], '.2f')
