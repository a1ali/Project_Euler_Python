
import datetime as dt
# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

# Find the sum of all the primes below two million.


# Python program to print all primes smaller than or equal to
# n using Sieve of Eratosthenes

def SieveOfEratosthenes(n):

	# Create a boolean array "prime[0..n]" and initialize
	# all entries it as true. A value in prime[i] will
	# finally be false if i is Not a prime, else true.
	prime = [True for i in range(n+1)]
	p = 2
	while (p * p <= n):

		# If prime[p] is not changed, then it is a prime
		if (prime[p] == True):

			# Update all multiples of p
			for i in range(p * p, n+1, p):
				prime[i] = False
		p += 1
	total = 0
	# Print all prime numbers
	for p in range(2, n):
		if prime[p]:

			total = total + p
			#print(p)
			
		
	print(total)
			

# driver program 
if __name__=='__main__': 
	start  = dt.datetime.now()
	n = 2000000
	print ("Following are the prime numbers smaller")
	print ("than or equal to", n) 
	SieveOfEratosthenes(n) 
	end = dt.datetime.now()

	total_t = end - start
	print('Time: {}'.format(total_t))