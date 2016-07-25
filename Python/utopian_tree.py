# Brandon Tsao
# Utopian Tree

T = int(raw_input())

for j in range(T):

	n = int(raw_input())
	height = 1

	for i in range(n):

		if i % 2 == 0:
			height *= 2
		else:
			height += 1
	print height
       