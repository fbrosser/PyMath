# Test.py \/ /\ \\

from Mathstuff import mathstuff

M = mathstuff()

"""
print M.PythagoreanTripletsBySum(1000) == [(200, 375, 425)]
print M.sumOfDigits(4) == 4
print M.sumOfDigits(40) == 4
print M.sumOfDigits(44) == 8
print M.sumOfDigits(123) == 6
print M.sumOfDigits(55558) == 28
print M.sumOfDigits(-4) == 4
print M.digits(4) == [4]
print M.digits(523412) == [5, 2, 3, 4, 1, 2]
print M.isPandigital(13, 3) == False
print M.isPandigital(132, 4) == False
print M.isPandigital(12348756, 8) == True
print M.isPandigital(1, 1) == True
print M.permutations([1,0,0]) == [(1,0,0), (0,1,0), (0,0,1)]
print M.digits(197) == [1, 9, 7]
print M.rotations(197) == [197, 719, 971]
print M.circularPrimes(100) == [2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, 97]
print M.nCircularPrimes(100) == 13
print M.nCircularPrimes(1000000) == 55

print M.fib(100)
print M.sumOfDigits(2**1000)
print sorted(M.permutations(range(10)))[999999]
"""

Matrix = [[1,2,3],
	  [1,2,3],
	  [1,2,3]]

print M.eliminate(Matrix, 3)

#print M.triangleNumbers(55)
