### MathstuffPermutations.py
# A collection of functions for handling pythagorean triplets

### Permutations and Rotations
class mathstuffPermutations:
	
	# Returns a list of all the rotations of the digits in a given number
	def rotations(self, x):
		d = self.digits(x)[::-1]
		r = []
		n = len(d)
		for i in range (0, n):
			rr = 0
			for j in range(0, n):
				rr = rr + (d[(i + j) % n] * (10**j))
			r.append(rr)
		return r

	# Return a list of all the permutations of the given sequence
	def permutations(self, iterable):
		return list(set(self.doPermutations(iterable)))
	
	# Generate permutations (NB! From itertools.permutations !)
	def doPermutations(self, iterable, r=None):
    		pool = tuple(iterable)
    		n = len(pool)
    		if(r is None):
    			r = n
    		if r > n:
        		return
    		indices = range(n)
    		cycles = range(n, n-r, -1)
    		yield tuple(pool[i] for i in indices[:r])
    		while n:
        		for i in reversed(range(r)):
            			cycles[i] -= 1
            			if cycles[i] == 0:
               				indices[i:] = indices[i+1:] + indices[i:i+1]
                			cycles[i] = n - i
            			else:
                			j = cycles[i]
                			indices[i], indices[-j] = indices[-j], indices[i]
                			yield tuple(pool[i] for i in indices[:r])
                			break
        		else:
            			return
		
