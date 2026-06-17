import math

def CountDivisors(n: int) -> int:
	count = 0
	sqrt_n = int(math.isqrt(n))
	for i in range(1, sqrt_n + 1):
		if n % i == 0:
			count += 2
			if i * i == n:
				count -= 1
	return count

triangularSum = 0
for i in range(10000000):
	triangularSum += i
	if triangularSum > 10000:
		if CountDivisors(triangularSum) > 500:
			print(triangularSum)
			break