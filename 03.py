# The prime factors of 13195 are 5, 7, 13, 29

# What is the largest prime factor of the number 600851475143

import math

n = 600851475143

primes = []

for i in range(3, int(math.sqrt(600851475143))):
	if n % i == 0:
		primes.append(i)
		n = n / i

max = 0;
for num in primes:
	if num > max:
		max = num
	

print(max)
