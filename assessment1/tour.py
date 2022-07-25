from node import Node

class Tour:
    ###
    # Basics
    ###

    # create an empty tour
    def __init__( self ):
        self.head = None

    def get_head( self ):
        return self.head
    
    def is_empty( self ):
        if self.get_head() is None:
            return True
        else:
            return False

    # number of points on tour
    def size( self ):
        return self.count


    ###
    # Looping
    ###

    def toString( self ):
        if self.is_empty():
            return ''
        # init, first run
        curr = self.get_head()
        full_string = curr.point.toString() + '\n '
        # rest
        while curr.next != self.head:
            curr = curr.next
            full_string += curr.point.toString() + '\n '
                
        return full_string

    # draw the tour to standard draw
    def draw( self ):
        if self.is_empty():
            return False

        curr = self.get_head()
        curr.point.drawTo( curr.next.point )
        while curr.next != self.get_head():
            # curr.point.draw()
            curr = curr.next    
            curr.point.drawTo( curr.next.point )
        
    # return the total distance of the tour
    def distance( self ):
        if self.is_empty():
            return 0
        # init, first run
        curr = self.get_head()
        total = curr.point.distanceTo( curr.next.point )
        # rest
        while curr.next != self.get_head():
            curr = curr.next
            total += curr.point.distanceTo( curr.next.point )
        return total
    

    ###
    # Heuristics
    ###

    def initial_insert( self, p ):
        new_node = Node( p )
        self.head = new_node
        new_node.next = self.head
        self.count += 1

    # insert p using nearest neighbor heuristic
    def insertNearest( self, p ):
        if self.is_empty():
            self.initial_insert( p )
        elif self.size() == 1:
        else:
            # init
            curr, new_node = self.get_head(), Node( p )
            least_node, least_distance = self.get_head(), float( 'inf' )

        for looping_through_nodes in range( self.size() ):
            # difference between the two inserts
            distance_difference = new_node.point.distanceTo( current_node.point )
            # checking
            if least_distance is None:
                least_distance = distance_difference
            elif distance_difference < least_distance:
                least_distance = distance_difference
                least_node = current_node
            current_node = current_node.next
        # insert the new node
        new_node.next = least_node.next
        least_node.next = new_node
    

    # insert p using smallest increase heuristic
    # insert the new node after every node. subtract distance between the original and original next node
    # add distance of original node to new node + new node to original next node
    def insertSmallest( self, p ):
        if self.is_empty():
            self.initial_insert( p )
        elif self.size() == 1:
        else:
            for looping_through_nodes in range( self.size() ):
                # difference between the two inserts
                # subtract original distance
                original_distance = current_node.point.distanceTo( current_node.next.point )
                # add 2 new distances
                new_first_distance = current_node.point.distanceTo( new_node.point )
                new_next_distance = new_node.point.distanceTo( current_node.next.point )
                # diff distance math
                distance_difference = new_first_distance + new_next_distance - original_distance
                if least_distance is None:
                    least_distance = distance_difference
                elif distance_difference < least_distance:
                    # checking
                    if ( distance_difference < least_distance ):
                        least_distance = distance_difference
                        least_node = current_node
                current_node = current_node.next
            # init
            curr, new_node = self.get_head(), Node( p )
            least_node, least_distance = self.get_head(), float( 'inf' )
            # insert the new node
            new_node.next = least_node.next
            least_node.next = new_node