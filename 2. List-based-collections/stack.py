from linkedlist import Element, LinkedList
class Stack(object):
    def __init__(self, top = None):
        self.ll = LinkedList(top)
    
    def push(self, new_element):
        "Ddd a new element onto the top of the stack"
        self.ll.insert_first(new_element)

    def pop(self):
        "Remove the first element off the top of the stack and return it"
        return self.ll.delete_first()