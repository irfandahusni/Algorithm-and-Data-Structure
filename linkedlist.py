class Element(object):
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList(object):
    def __init__(self, head = None):
        self.head = head #Contains Element Object

    def append(self, new_element):
        current = self.head
        if self.head : 
            while current.next:
                current = current.next
            current.next = new_element
        else : 
            self.head = new_element
    
    def get_position(self, position):
        """Get an element from a particular position.
        Assume the first position is "1".
        Return "None" if position is not in the list."""
        if position == 1 :
            return self.head
        else :
            current_position = self.head
            try :
                for i in range(1,position):
                    current_position = current_position.next
                return current_position
            except :
                return None 

    def insert(self, new_element, position):
        if position == 1 :
            self.head = new_element
            element_in_pos = self.get_position(position)
            self.head.next = element_in_pos
        else : 
            if self.get_position == None :
                element_before_pos = self.get_position(position-1)
                element_before_pos.next = new_element 
                
            else : 
                element_in_pos = self.get_position(position)
                element_before_pos = self.get_position(position-1)
                element_before_pos.next = new_element
                new_element.next = element_in_pos
        
# Test cases
# Set up some Elements
e1 = Element(1)
e2 = Element(2)
e3 = Element(3)
e4 = Element(4)

# Start setting up a LinkedList
ll = LinkedList(e1)
ll.append(e2)
ll.append(e3)

# # Test get_position
# # Should print 3
# print(ll.head.next.next.value)
# # Should also print 3
# print(ll.get_position(3).value)

# Test insert
ll.insert(e4,2)
# Should print 4 now
print(ll.get_position(3).value)
