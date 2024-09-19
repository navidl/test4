class Node:
    ''' 
    An object for storing a single Node of a linked list model to attribute/data and the link to the next note in the list
    '''
    data= None
    next_node = None
    def __init__(self,data):
        self.data= data

    def __repr__(self):
        return "<Node data: %s >" %self.data

class Linkedlist:
    """
    Singly link list
   """

    def __init__(slef):
        self.head=None
    def is_empty(Self):
        return self.head == None
    def size (self):
        # Return the number of note -takes O(n) time
        current= self.head
        count= 0
        while current :
            count += 1 
            current = current.next_node
        return count
    def add(self,data):
        # add a new node containing data at the head of the list
        new_node = Node(data)
        new_node.next_node = self.head
        self.head = new_node

