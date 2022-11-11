# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99. 

# Find the largest palindrome made from the product of two 3-digit numbers.

max = 0
num1 = 100
num2 = 100

for i in range(100, 1000):
	for j in range(100, 1000):
		num = i * j
		if str(num) == str(num)[::-1]:
			if num > max:
				max = num

print(max)
