# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
import sys

nums = [11, 13, 14, 16, 17, 18, 19, 20]

for i in range (2520, sys.maxsize, 20):
	flag = True
	for j in nums:
		if i % j != 0:
			flag = False;
	if flag:
		print(i)
		sys.exit(0)