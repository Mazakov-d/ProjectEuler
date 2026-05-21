FiboList = [1, 2]
length = 2

while FiboList[length - 1] < 4000000:
	length = len(FiboList)
	FiboList.append(FiboList[length - 1] + FiboList[length - 2])

num = 0
for i in range(len(FiboList)):
	if (FiboList[i] % 2) == 0:
		num += FiboList[i]

print(num)