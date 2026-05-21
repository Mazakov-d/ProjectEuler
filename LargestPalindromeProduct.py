num1 = 500
num2 = 500
palindrome = 9009

while num1 < 1000:
	num2 = num1 + 1
	while num2 < 1000:
		num = str(num1 * num2)
		length = len(num)
		left = (length // 2) - 1
		if (length % 2):
			right = (length // 2) + 1
		else:
			right = (length // 2)
		while (left >= 0 and right < length and (num[left] == num[right])):
			if (left == 0):
				if num1 * num2 > palindrome:
					palindrome = num1 * num2
				break
			left -= 1
			right += 1
		num2 += 1
	num1 += 1

print(palindrome)