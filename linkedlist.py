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
        """Insert a new node at the given position.
        Assume the first position is "1".
        Inserting at position 3 means between
        the 2nd and 3rd elements."""

        if position == 1 :
            new_element.next = self.head
            self.head = new_element
        else : 
            if self.get_position == None : #end of list
                element_before_pos = self.get_position(position-1)
                element_before_pos.next = new_element 
                
            else : 
                element_in_pos = self.get_position(position)
                element_before_pos = self.get_position(position-1)
                element_before_pos.next = new_element
                new_element.next = element_in_pos

    def delete(self, value):
        """Delete the first node with a given value."""
        current_position = self.head
        position = 1
        while current_position.next:
            if current_position.value == value:
                if current_position == self.head:
                    self.head = current_position.next
                    break

                elif current_position.next == None :
                    before_position = self.get_position(position-1)
                    before_position.next = None
                    break
                else : 
                    before_position = self.get_position(position-1)
                    after_position = self.get_position(position+1)
                    before_position.next = after_position
                    break

            position = position + 1
            current_position = current_position.next


    def insert_first(self, new_element):
        "Insert new element as the head of the LinkedList"
        self.insert(new_element,1)
    
    def delete_first(self):
        if self.head:
            deleted_element = self.head
            temp = deleted_element.next
            self.head = temp
            return deleted_element
        else:
            return None
