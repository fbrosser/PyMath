### MathstuffPrimes.py
# A collection of functions for handling prime numbers

### Prime numbers
# A natural number that is not evenly divisible by any natural number,
# other than itself and 1.
class mathstuffPrimes:

	# Check if a number is a prime number
	def isPrime(self, x):
		if(x == 2 or x == 3):
			return True
		elif(x % 2 == 0 or x < 2):
			return False
		else:
			return self.MillerRabin(x)

	# Returns true iff the two given numbers are coprime (no common divisors apart from 1).
	def coPrime(self, x, y):
		return (self.gcd(x, y) == 1)

	# Returns a list of the prime factors of a given number 
	def factor(self, n):  
		if (n == 1 or self.isPrime(n)): 
			return [n]
		factors = []
		for i in self.primes(self.squareRootInteger(n)):
		        while n % i == 0:  
				factors.append(i)
				n = n / i
		return factors

	# Returns a list of all the primes below a given number by using primality checks
	def primes(self, upTo):
		return [x for x in range(upTo) if (self.isPrime(x))]

	# Returns a list of all the primes below a given number by using a prime sieve
	def primesSieve(self, upTo):

		primes = [2]
    		n = upTo + 1
    		c = ([False] * n)    		

    		for i in range(3, n, 2):
        		if c[i]:
            			continue
        		for f in range(i*2, n, i):
            			c[f] = True
        		primes.append(i)
	
    		return primes

	# Returns the number of primes below a given number	
	def nPrimes(self, upTo):
		return len(primes(upTo))

	# Miller-Rabin primality check for number n.
	def MillerRabin(self, n):
		tN = [2,3,5,7,11,13,17,31,61,73]			
		if(n in tN):
			return True

		# Get n-1 on the form 2^s * d	
		s = 0
		d = n - 1		
		while (d % 2 == 0):
			d >>= 1
			s += 1

		for r in range(len(tN)):
			a = pow(tN[r], d, n)
			if(a == 1):
				continue
			for i in range (s - 1):
				if(a == n - 1):
					continue
				a = (a * a) % n
			if (a != n - 1):
				return False
		return True
		
	### Circular Primes
	# A prime is circular if all rotations of its digits are prime
		
	# Returns true iff the given number is prime and circular
	def isCircularPrime(self, x):
		r = self.rotations(x)
		for i in range(0, len(r)):
			if not(self.isPrime(r[i])):
				return False
		return True
	
	# Returns a list of all the circular primes upto a given number
	def circularPrimes(self, upTo):
		return [x for x in self.primesSieve(upTo) if (self.isCircularPrime(x))]
	
	# Returns the number of circular primes upto a given number
	def nCircularPrimes(self, upTo):
		return len(self.circularPrimes(upTo))
	
