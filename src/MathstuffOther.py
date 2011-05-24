### MathstuffOther.py
# A collection of helper functions for Mathstuff
# Contains among other things Fibonnaci numbers, GCD, digit sum

class mathstuffOther:

	### Fibonacci Numbers
	# Each new term in the sequence is generated by adding the previous two terms
	def fib(self, upTo):
		f = [1, 2]
		i = 2
		while(f[i-2] + f[i-1] < upTo):
			f.append(f[i-2] + f[i-1])
			i = i + 1
		return f
		
	### Gauss Elimination
	# Functions for solving linear systems of equations
	
	# Triangularize given matrix
	def eliminate(self, m, N):
		for k in range (0, N):
			for j in range (k+1, N):
				if m[k][k] != 0:
					m[k][j] = m[k][j] / m[k][k]
					m[k][k] = 1.0
			for i in range (k+1, N):
				for j in range (k+1, N):
					m[i][j] = m[i][j] - (m[i][k] * m[k][j])
				m[i][k] = 0.0
		return m
		
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
  		
  	# Get the sum of the digits in a number
  	def sumOfDigits(self, x):
  		return sum(self.digits(x))
  		
  	# Get a list of the digits in a number
  	def digits(self, x):
  		d = []
    		x = abs(x)
  		while(x / 10 > 0):
  			d.append(x % 10)
  			x = x / 10
  		d.append(x % 10)
  		return d[::-1]		
  		
  	# Returns true iff x is a palindrome
  	def isPalindrome(self, x):
  		return x == rev(x)
  		
  	# Returns true iff x is pandigital
  	# A pandigital number contains all the numbers 1..n exactly once
  	def isPandigital(self, x, n):
  		return sorted(self.digits(x)) == range(1, n+1)

	# Simple square root function
	def squareRoot(self, x):
		return x ** 0.5

	# Returns the square root as an integer (rounded to neareast integer)
	def squareRootInteger(self, x):
		s = x ** 0.5
		return int(s)

	# Euler's totient function
	## The number of positive integers less than or equal to a given number n that are coprime to n 
  	def totient(self, n):
		i = 0		
		for x in range (1, n+1):
			if(self.coPrime(x, n)):
				i = i + 1
		return i

	# Returns the greatest common divisor
	def gcd(self, x, y):
		if (x == 0):
			return y
		while (not (y == 0)):
			if(x > y):
				x = x - y
			else:
				y = y - x
		return x

  	# Returns a list of all triangle numbers upto a given number
  	# The n'th triangle number is given by Tn = n(n+1)/2
  	def triangleNumbers(self, upTo):
  		t = []
  		n = 0
  		next = 0
  		while(next <= upTo):
  			n = n + 1
  			next = (n * (n + 1)) / 2
  			if(next > upTo):
  				break
  			else:
  				t.append(next)
  		return t 
  	
