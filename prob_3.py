from datetime import datetime as dt

def isPrime(x):
	for divisor in range(2,x):
		if x%divisor == 0:
			# X is non-prime
			return False
	
	return True
	
def factorize(x):
	primeFactors = []
	divisor = 2
	while x > 1:
		if isPrime(divisor):
			if x % divisor == 0:
				x = x / divisor
				primeFactors.append(divisor)
			else:
				divisor += 1
		else:
			divisor += 1	
	return primeFactors
	
startTime = dt.now()
factors = factorize(600851475143)
timeDiff = dt.now() - startTime

print(factors)
print("Time taken: {}s".format(timeDiff.total_seconds()))