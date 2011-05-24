### MathstuffPythagorean.py
# A collection of functions for handling pythagorean triplets

### Pythagorean Triplets
# A set of three natural numbers a<b<c, for which a^2 + b^2 = c^2 
class mathstuffPythagorean:
	
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

	# Returns a list of all Pythagorean Triplets for which a,b,c are in 	[lo,hi]			
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
		
