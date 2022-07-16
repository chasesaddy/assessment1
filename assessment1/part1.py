class ForLoopsConditions:
    def helloWorld( self ):
        return 'Hello World';

    def numbersGoUp( self, toNum ):
        theStr = ''
        makeInclusive = toNum + 1
        for i in range( 1, makeInclusive ):
            theStr += str( i ) + ','
        return theStr[ 0:-1 ]

    def oddNums( self, toNum ):
        arr = []
        for i in range( 1, toNum ):
            if i % 2 == 1:
                arr.append( i )
        theStr = ''
        for i in arr:
            theStr += str( i ) + ','
        return theStr[ 0:-1 ]

    def fizzbuzz( self ):
        theStr = ''
        for i in range( 50 ):
            if i % 3 == 0:
                theStr += 'Fizz'
            elif i % 5 == 0:
                theStr += 'Buzz'
            elif i % 15 == 0:
            # elif i % 3 == 0 and i % 5 == 0:
                theStr += 'FizzBuzz'
            else:
                theStr += str( i )
            
            theStr += ','
        return theStr[ 0:-1 ]

    def fizzbuzzNot( self ):
        theStr = '';
        for i in range( 50 ):
            if not i % 3:
                theStr += 'Fizz'
            elif not i % 5:
                theStr += 'Buzz'
            elif not i % 15:
            # elif not i % 3 and not i % 5:
                theStr += 'FizzBuzz'
            else:
                theStr += str( i )

            theStr += ','
        return theStr[ 0:-1 ]

class Functionings:
    def maxNum( self, arr ):
        max = arr[ 0 ]
        for i in range( 1, len( arr ) ):
            if arr[ i ] > max:
                max = arr[ i ]
        return max

    def maxNumIndex( self, arr ):
        temp = arr[ 0 ]
        max = 0
        for i in range( 1, len( arr ) ):
            if arr[ i ] > temp:
                temp = arr[ i ]
                max = i
        return max

class Recursionings:
    def factorial( self, num ):
        if int( num ) <= 1:
            return 1
        return num * self.factorial( num - 1 )

    def factorial_ternary( self, num ):
        return num * self.factorial_ternary( num - 1 ) if num > 1 else 1

    # the princeton site brought up this being inefficient. Makes sense. 
    # the number of tries is always squaring the fibonacci number.
    # So exponentially growing/exponential O
    def fib_bad( self, num ):
        if num == 1:
            return 1
        elif num == 0:
            return 0
        return self.fib_bad( num - 1 ) + self.fib_bad( num - 2 )

    def fib( self, num, curr = 1, before = 0 ):
        if ( num == 1 ):
            return curr
        elif ( num == 0 ):
            return before
        
        new_curr = curr + before
        new_num = num - 1
        return self.fib( new_num, new_curr, curr )
