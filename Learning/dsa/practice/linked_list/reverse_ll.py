class Node():
    def __init__(self, data):
        self.data = data
        self.next = None

# Create Linked list
node1 = Node(7)
node2 = Node(3)
node1.next = node2
node3 = Node(5)
node2.next = node3
node4 = Node(9)
node3.next = node4

# print linked list
current_node = node1
while current_node is not None:
    print(current_node.data, end=" -> ")
    current_node = current_node.next
print("None")

# Reverse LL.
prev = None
curr = node1
while curr != None:
    tmp = curr.next
    curr.next = prev
    prev = curr
    curr = tmp
node1 = prev


class Solution:
    def reverseList(self, head):
        if not head:
            return None

        newHead = head
        if head.next:
            newHead = self.reverseList(head.next)
            head.next.next = head
        head.next = None

        return newHead

if __name__ == "__main__":
    # Create Linked list
    node1 = Node(7)
    node2 = Node(3)
    node1.next = node2
    node3 = Node(5)
    node2.next = node3
    node4 = Node(9)
    node3.next = node4
    sol = Solution()
    sol.reverseList(node1)

# print reversed list
current = node1
while current is not None:
    print(current.data, end=" -> ")
    current = current.next
print("None")
