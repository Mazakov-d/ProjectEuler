i = 20
while 1:
	if not (i % 19):
		for j in range(2, 21):
			if i % j:
				break
			if j == 20:
				print(i)
				exit()
	i += 20

