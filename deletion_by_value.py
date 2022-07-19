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
                print(n.data, "---", end=" ")
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

    def after_node(self, data, x):
        n = self.head
        while n is not None:
            if x == n.data:
                break
            n = n.ref
        if n is None:
            print("node is not present in ll")

        else:
            new_node = Node(data)
            new_node.ref = n.ref
            n.ref = new_node

    def add_before(self, data, x):
        if self.head is None:
            print("ll is empty")
            return
        if self.head.data == x:
            new_node = Node(data)
            new_node.ref = self.head
            self.head = new_node
            return
        n = self.head
        while n.ref is not None:
            if n.ref.data == x:
                break
            n = n.ref
        if n.ref is None:
            print("node not found")
        else:
            new_node = Node(data)
            new_node.ref = n.ref
            n.ref = new_node

   
    def delete_by_value(self, x):
        if self.head is None:
            print("linkedlist is empty")
            return
        if x == self.head.data:
            self.head = self.head.ref
            return
        n = self.head
        while n.ref is not None:
            if x == n.ref.data:
                break
            n = n.ref
        if n.ref is None:
            print("node is not present")
        else:
            n.ref = n.ref.ref


ll = linkedlist()

while (True):
    val = int(input("enter the data of nodes"))
    e = int(input("Enter the 1 to insert at begin 2 at end 3 to insert after the node 4 to insert before node"))

    if e == 1:
        ll.add_begin(val)

    elif e == 2:
        ll.add_end(val)

    elif e == 3:
        x = int(input("tell which node after"))
        ll.after_node(val, x)

    elif e == 4:
        x = int(input("tell which node before"))
        ll.add_before(val, x)

    else:
        x = int(input("which node is to be deleted"))
        ll.delete_by_value(x)

    ll.print_ll()
