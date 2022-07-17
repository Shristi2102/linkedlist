class Node:
    def __init__(self, data):
        self.data = data
        self.ref = None

class linkedlist:
    def __init__(self):
        self.head = None

    def print_ll(self):

        if self.head is None:
            print("linked list is empty")

        else:
            n = self.head
            while n is not None:
                print(n.data ,"---", end = " ")
                n = n.ref

    def add_begin(self, data):
        new_node = Node(data)
        new_node.ref = self.head
        self.head = new_node

ll = linkedlist()
ll.add_begin(10)
ll.add_begin(60)
ll.add_begin(50)
ll.add_begin(40)
ll.add_begin(100)
ll.print_ll()
