num = 0
for i in range(1000):
	if not (i % 5) or not (i % 3):
		num += i

print(num)