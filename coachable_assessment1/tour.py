from node import Node
import stdio

class Tour:
    # create an empty tour
    def __init__( self ):
        self.head = None
        self.count = 0

    def get_head( self ):
        return self.head
    
    def is_empty( self ):
        if self.get_head() is None:
            return True
        else:
            return False

    def toString( self ):
        fullString = ''
        current_node = self.head

        while current_node is not self.head.next:
            fullString += current_node.point.toString() + '\n '
            current_node = current_node.next
        return fullString
    
    # draw the tour to standard draw
    def draw( self ):
        if self.is_empty():
            return False

        current_node = self.head
        while current_node is not self.head.next:
            current_node.point.draw()
            current_node.point.drawTo( current_node.next.point )

            current_node = current_node.next

    # number of points on tour
    def size( self ):
        if self.is_empty():
            return 0

        # count = 1
        # head_node = current_node = self.get_head()
        # while current_node is not head_node.next:
        #     count += 1
        #     current_node = current_node.next
        # return count
        count = 0
        current_node = self.head
        while True:
            count += 1
            current_node = current_node.next
            if current_node == self.head:
                break
        return count

         
    # return the total distance of the tour
    def distance( self ):
        if self.is_empty():
            return 0

        total_distance = 0
        head_node = current_node = self.get_head()
        while current_node is not head_node.next:
            total_distance += current_node.point.distanceTo( 
                current_node.next.point 
            )
            current_node = current_node.next
        return total_distance

    # def insert_core( self, p ):
    #     new_node = Node( p )

    #     if self.is_empty():
    #         self.head = new_node
    #         new_node.next = self.get_head()
    #         return False
    
    #     least_distance = None
    #     least_node = current_node = self.get_head()

    #     if self.size() == 1:
    #         current_node.next = new_node
    #         new_node.next = current_node
    #         return False
                
    #     return [ new_node, current_node, least_node, least_distance ]

    # insert p using nearest neighbor heuristic
    def insertNearest( self, p ):
        self.count += 1
        stdio.writeln( p.toString() )
        # results = self.insert_core( p )
        # if results is False:
        #     return True
        # else:
        #     new_node, current_node, least_node, least_distance = results
        new_node = Node( p )

        if self.is_empty() is True:
            stdio.writeln( '1st' )
            self.head = new_node
            new_node.next = self.head
            # return True    
        elif self.size() == 1:
            stdio.writeln( '2nd' )
            self.head.next = new_node
            new_node.next = self.head
            # return True
        else:
            stdio.writeln( '3rd' )
            stdio.writef( "size: %d\n", self.size() )
            least_distance = None
            # least_node = current_node = self.head
            current_node = self.head
            least_node = current_node
            for looping_through_nodes in range( self.size() ):
                stdio.writeln( '--- --- ---' )
                # only difference between the two inserts
                distance_difference = new_node.point.distanceTo( current_node.point )
                stdio.writef( "distance = %.4f\n", distance_difference )
                # checking
                if least_distance is None:
                    stdio.writeln( 'first if' )
                    least_distance = distance_difference
                elif distance_difference < least_distance:
                    stdio.writeln( '2nd if' )
                    least_distance = distance_difference
                    least_node = current_node
                current_node = current_node.next
                stdio.writeln( 'current_node: ' + current_node.point.toString() )

            # insert the new node
            new_node.next = least_node.next
            least_node.next = new_node
            stdio.writeln( '-- it got here right --' )
            # return True
        stdio.writeln( '--FULL NODE: BEG--' )
        stdio.writeln( self.toString() )
        stdio.writeln( '--FULL NODE: END--' )
    

    # insert p using smallest increase heuristic
    def insertSmallest( self, p ):
        new_node, current_node, least_node, least_distance = self.insert_core( p )

        # insert the new node after every node. subtract distance between the original and original next node
        # add distance of original node to new node + new node to original next node
        for looping_through_nodes in range( self.size() ):
            # only difference between the two inserts
            # subtract original distance
            original_distance = current_node.point.distanceTo( current_node.next.point )
            # add 2 new distances
            new_first_distance = current_node.point.distanceTo( new_node.point )
            new_next_distance += new_node.point.distanceTo( current_node.next.point )
            # diff distance math
            distance_difference = new_first_distance + new_next_distance - original_distance
            # checking
            if ( distance_difference < least_distance ):
                least_distance = distance_difference
                least_node = current_node
            current_node = current_node.next
        
        # insert the new node
        new_node.next = least_node.next
        least_node.next = new_node
        return True
