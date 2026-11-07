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


# class Solution:
#     def mergeTwoLists(self, list1, list2):
#         dummy = Node(None)
#
#         while list1 and list2:
#             if list1.val < list2.val:
#                 node.next = list1
#                 list1 = list1.next
#             else:
#                 node.next = list2
#                 list2 = list2.next
#             node = node.next
#
#         node.next = list1 or list2
#
#         return dummy.next

class Solution:
    def mergeTwoLists(self, list1, list2):
        if list1 is None:
            return list2
        if list2 is None:
            return list1
        if list1.val <= list2.val:
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1
        else:
            list2.next = self.mergeTwoLists(list1, list2.next)
            return list2


if __name__ == "__main__":
    ll1 = LinkedList()
    ll1.append(5)
    ll1.append(7)
    ll1.append(8)
    ll1.append(11)
    ll1.append(15)
    ll1.display()

    ll2 = LinkedList()
    ll2.append(3)
    ll2.append(5)
    ll2.append(9)
    ll2.append(12)
    ll2.display()

    sol = Solution()
    merged_head = sol.mergeTwoLists(ll1.head, ll2.head)

    current = merged_head
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print(None)

