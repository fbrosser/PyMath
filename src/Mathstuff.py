# Mathstuff.py \/ /\ \\

# A collection of useful math functions 
# (Mainly written for Project Euler Problems)
class mathstuff:

	### Lychrel Numbers
	# A number that never forms a palindrome through reversing and adding to itself
	# repeatedly (here: up to a set number of iterations) is called a Lychrel number.
		
	# Check if a number is a Lychrel number, returns true or false
	def isLychrel(self, n, maxIter):
		return (isLychrelInt(n, maxIter) == 1)

	# Check if a number is a Lychrel number, returns 1 or 0
	def isLychrelInt(self, n, maxIter):
		for i in range(0, maxIter):
			n += self.rev(n)
			if(self.rev(n) == n):
				return 0
		return 1

	# Returns a list of all Lychrel numbers below a given number
	def Lychrel(self, upTo, maxIter):
		return [x for x in range(upTo) if (self.isLychrelInt(x, maxIter) == 1)]

	# Returns the number of Lychrel numbers below a given number
	def nLychrel(self, upTo, maxIter):
		return sum(map(self.isLychrelInt, range(upTo)))


	### Pythagorean Triplets
	# A set of three natural numbers a<b<c, for which a^2 + b^2 = c^2 
	
	# Returns true iff (a,b,c) form a pythagorean triplet
	def isPythagoreanTriplet(self, a, b, c):
		if (a**2 + b**2 == c**2):
			return True
		return False
	
	# Returns a list of all Pythagorean Triplets for which a,b,c are in [lo, hi]
	def pythagoreanTriplets(self, lo, hi):
		N = []
		for m in range(lo+2, hi):
			for n in range(1, m):
				a = m**2 - n**2
				b = 2*m*n
				if(a > b):
					a, b = b, a
				c = m**2 + n**2
				if (self.isPythagoreanTriplet(a,b,c)):
					for k in range(1, (hi/c)):
						N[len(N):] = [(k*a, k*b, k*c)]
		return sorted(list(set(N)), key=lambda t: t[2])

	# Returns a list of all Pythagorean Triplets for which a,b,c are in [lo, hi]			
	def nPythagoreanTriplets(self, lo, hi):
		return len(self.pythagoreanTriplets(lo,hi))
		
	# Returns all possible sets {a,b} which form a Pythagorean triplet with a given c 
	def PythagoreanTriplet(self, c):
		N = []
		for b in range (0, c):
			for a in range (0, b):
				if(self.isPythagoreanTriplet(a,b,c)):
					N[len(N):] = [(a, b, c)]
		return N

	# Returns all possible sets {a,b,c} for which a+b+c = N
	def PythagoreanTripletsBySum(self, N):
		return [x for x in self.pythagoreanTriplets(0, N/2) if (sum(x) == N)]
		

	### Prime numbers
	# A natural number that is not evenly divisible by any natural number,
	# other than itself and 1.

	# Check if a number is a prime number
	def isPrime(self, x):
		if(x == 2 or x == 3):
			return True
		elif(x % 2 == 0 or x < 2):
			return False
		else:
			return self.MillerRabin(x)

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
			if a == 1:
				continue
			for i in range (s - 1):
				if(a == n - 1):
					continue
				a = (a * a) % n
			if (a != n - 1):
				return False
		return True


	### Helper Functions
	# Useful functions which do not belong in any particular category 
	
	# Reverse the digits in a number
	def rev(self, x):
		return int(str(x)[::-1]) 

	# Get a given number in binary form
	def binary(self, x):
  		bin = []
  		while (x > 0):
			bin[len(bin):] = [(x % 2)]
    			x = x / 2
  		return bin
