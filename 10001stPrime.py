def isPrimeNumber(num):
	if not num % 2:
		return False
	factor = 3
	while factor <= num // 2:
		if not num % factor:
			return False
		factor += 2
	return True

length = 4
primes = [2, 3, 5, 7]
num = 11
while length < 10001:
	if isPrimeNumber(num):
		print(num)
		length += 1
		primes.append(num)
	num += 2

print(primes[10000])