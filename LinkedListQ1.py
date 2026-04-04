class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        new_node.prev = None

    def insert_at_end(self, data):
        new_node = Node(data)

        if self.head == None:
            self.head = new_node
            return
        current = self.head
        while current.next != None:
            current = current.next
        current.next = new_node

    def delete(self, key):
        current = self.head

        while current:
            if current.data == key:

                if current.prev is None:
                    self.head = current.next
                    if self.head:
                        self.head.prev = None

                else:
                    current.prev.next = current.next
                    if current.next:
                        current.next.prev = current.prev
                return
        current = current.next
    print("value not found")

    def display(self):
        current = self.head
        while current:
            print(current.data, end="-->")
            current = current.next
        print("None")

ll = LinkedList()
ll.insert_at_beginning(10)
ll.insert_at_beginning(5)
ll.insert_at_end(20)
ll.insert_at_end(30)

ll.display()



