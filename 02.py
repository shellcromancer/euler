total = 0

a = 0
b = 1
total = 0

while a + b <= 4000000:
	c = a + b
	if c % 2 == 0:
		total += c
	a = b
	b = c

print("Total is: {}".format(total))
