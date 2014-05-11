total = 0
lastPrimeISaw = 2
for n in range(3, 1001):
	tests = range(2, n - 1)
	prime = True
	for t in tests:
		if n % t == 0:
			prime = False
	
	if prime == True:
		total = total + n

print total