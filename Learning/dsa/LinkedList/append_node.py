class Node():
    def __init__(self, val):
        self.val = val
        self.next = None

class LinkedList():
    def __init__(self):
        self.head = None

    def append(self, data):
        newNode = Node(data)

        if self.head is None:
            self.head = newNode
            return

        current = self.head
        while current.next:
            current = current.next
        current.next = newNode

    def display(self):
        current = self.head
        while current:
            print(current.val, end=" -> ")
            current = current.next
        print(None)




if __name__ == "__main__":
    ll1 = LinkedList()
    ll1.append(7)
    ll1.append(6)
    ll1.append(4)
    ll1.append(5)
    ll1.append(9)
    ll1.display()

    ll2 = LinkedList()
    ll2.append(3)
    ll2.append(7)
    ll2.append(3)
    ll2.append(2)
    ll2.display()
