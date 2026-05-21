squareSum = 0
basicSum = 0

for i in range(1, 101):
	squareSum += i * i
	basicSum += i

print((basicSum * basicSum) - squareSum)