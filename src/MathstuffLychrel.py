### MathstuffLychrel.py
# A collection of functions for handling lychrel numbers

### Lychrel Numbers
# A number that never forms a palindrome through reversing and adding to itself
# repeatedly (here: up to a set number of iterations) is called a Lychrel number.
class mathstuffLychrel:

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
		
