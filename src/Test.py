# Test.py \/ /\ \\
from Bcolors import bcolors

B = bcolors("mathstuff")

B.check( "PythagoreanTripletsBySum(1000) == [(200, 375, 425)]" )
B.check( "sumOfDigits(4) == 4" )
B.check( "sumOfDigits(40) == 4" )
B.check( "sumOfDigits(44) == 8" )
B.check( "sumOfDigits(123) == 6" )
B.check( "sumOfDigits(55558) == 28" )
B.check( "sumOfDigits(-4) == 4" )
B.check( "digits(4) == [4]" )
B.check( "digits(523412) == [5, 2, 3, 4, 1, 2]" )
B.check( "isPandigital(13, 3) == False" )
B.check( "isPandigital(132, 4) == False" )
B.check( "isPandigital(12348756, 8) == True" )
B.check( "isPandigital(1, 1) == True" )
B.check( "permutations([1,0,0]) == [(1,0,0), (0,1,0), (0,0,1)]" )
B.check( "digits(197) == [1, 9, 7]" )
B.check( "rotations(197) == [197, 719, 971]" )
B.check( "circularPrimes(100) == [2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, 97]" )
B.check( "nCircularPrimes(100) == 13" )
B.check( "circularPrimes(100) == [2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, 97]" )
