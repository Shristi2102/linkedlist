class Node:
    def __init__(self, data):
        self.data = data
        self.ref = None

class linkedlist:
    
    def __init__(self):
        self.head = None

    def add_begin(self, data):
        new_node = Node(data)
        new_node.ref = self.head
        self.head = new_node
        return

    def print_ll(self):
        if self.head is None:
            print("linked list is empty")

        else:
            n = self.head
            while n is not None:
                print(n.data, "---")
                n = n.ref

    def add_end(self, data):

        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            n = self.head
            while n.ref is not None:
                n = n.ref
            n.ref = new_node


ll = linkedlist()

while (True):
    val = int(input("enter the data of nodes"))
    e = int(input("Enter the 1 to insert at begin 2 at end 3 to quit"))

    if e == 1:
        ll.add_begin(val)

    elif e == 2:
        ll.add_end(val)
        break

    else:
        print("you quit")
        break
    ll.print_ll()
