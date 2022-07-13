import unittest

from k1 import ForLoopsConditions
from k1 import Functionings
from k1 import Recursionings

# 5 tests
class TestK1( unittest.TestCase ):
    def setUp( self ):
        self.printed_tests = {
            "helloWorld": "Hello World", 
            "upTo25": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25", 
            "oddTo30": "1,3,5,7,9,11,13,15,17,19,21,23,25,27,29", 
            "fizzbuzz": "Fizz,1,2,Fizz,4,Buzz,Fizz,7,8,Fizz,Buzz,11,Fizz,13,14,Fizz,16,17,Fizz,19,Buzz,Fizz,22,23,Fizz,Buzz,26,Fizz,28,29,Fizz,31,32,Fizz,34,Buzz,Fizz,37,38,Fizz,Buzz,41,Fizz,43,44,Fizz,46,47,Fizz,49" 
        }
        self.first = ForLoopsConditions()

    def test_hello_world( self ):
        self.assertEqual( self.first.helloWorld(), self.printed_tests[ 'helloWorld' ] )
        
    def test_numbers_to_25( self ):
        self.assertEqual( self.first.numbersGoUp( 25 ), self.printed_tests[ 'upTo25' ] )

    def test_odd_to_30( self ):
        self.assertEqual( self.first.oddNums( 30 ), self.printed_tests[ 'oddTo30' ] )

    def test_fizzbuzz( self ):        
        self.assertEqual( self.first.fizzbuzz(), self.printed_tests[ 'fizzbuzz'] )

    def test_fizzbuzz_second( self ):
        self.assertEqual( self.first.fizzbuzzNot(), self.printed_tests[ 'fizzbuzz' ] )

# 2 tests
class TestK2( unittest.TestCase ):
    def setUp( self ):
        self.nums_arr = [ 1, -2, -1, -5, 2, 18, 4, 11, 6, 4, 8, -2, 3, -111, 1 ]
        self.nums_arr_deux = [ 47, 5, 88, 54, -11, 73, 90, 13, -57, 0, 66, 43, -2 ]
        self.second = Functionings()

    def test_max_num( self ):
        self.assertEqual( self.second.maxNum( self.nums_arr ), 18 )
        self.assertEqual( self.second.maxNum( self.nums_arr_deux ), 90 )    

    def test_max_num_index( self ):
        self.assertEqual( self.second.maxNumIndex( self.nums_arr ), 5 )
        self.assertEqual( self.second.maxNumIndex( self.nums_arr_deux ), 6 )

# 3 tests
class TestK3( unittest.TestCase ):
    def setUp( self ):
        self.third = Recursionings()
        self.fact = {
            '5': 120, 
            '15': 1307674368000, 
            '20': 2432902008176640000 
        }

    def test_factorial( self ):
        self.assertEqual( self.third.factorial( 5 ), self.fact[ '5' ] )
        self.assertEqual( self.third.factorial( 15 ), self.fact[ '15' ] )
        self.assertEqual( self.third.factorial( 20 ), self.fact[ '20' ] )

    def test_factorial_ternary( self ):
        self.assertEqual( self.third.factorial_ternary( 5 ), self.fact[ '5' ] )
        self.assertEqual( self.third.factorial_ternary( 15 ), self.fact[ '15' ] )
        self.assertEqual( self.third.factorial_ternary( 20 ), self.fact[ '20' ] )

    def test_fibonacci( self ):
        fib = {
            '32': 2178309, 
            '38': 39088169, 
            '40': 102334155
        }
        
        # self.assertEqual( self.third.fib_bad( 32 ), fib[ '32' ] ) # slow - half a second
        # self.assertEqual( self.third.fib_bad( 38 ), fib[ '38' ] ) # real slow -- 10 seconds
        # self.assertEqual( self.third.fib_bad( 40 ), fib[ '40' ] ) # now getting SUPER slow

        # linear O(n)
        self.assertEqual( self.third.fib( 32 ), fib[ '32' ] )
        self.assertEqual( self.third.fib( 38 ), fib[ '38' ] )
        self.assertEqual( self.third.fib( 40 ), fib[ '40' ] )

if __name__ == '__main__':
    unittest.main()
