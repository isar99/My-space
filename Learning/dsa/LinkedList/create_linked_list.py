class Node():
    def __init__(self, data):
        self.data = data
        self.next = None



# create nodes
node1 = Node(7)
node2 = Node(3)
node3 = Node(4)



#link nodes
node1.next = node2
node2.next = node3



# print linked list
current_node = node1
while current_node is not None:
    print(current_node.data, end=" -> ")
    current_node = current_node.next
print("None")



