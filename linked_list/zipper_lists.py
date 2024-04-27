from linked_list import LinkedList, Node

n10 = Node(10)
n9 = Node(9, n10)
n8 = Node(8)#, n9)
n7 = Node(7, n8)
n6 = Node(6, n7)

ll2 = LinkedList(n6)

n5 = Node(5)
n4 = Node(4, n5)
n3 = Node(3, n4)
n2 = Node(2, n3)
n1 = Node(1, n2)

ll1 = LinkedList(n1)


def zipper_lists(ll1: LinkedList, ll2: LinkedList)-> LinkedList:
    current1 = ll1.head
    current2 = ll2.head

    while current1 and current2:
        next = current1.next
        current1.next = current2
        
        current1 = current2
        current2 = next

    return ll1


# print(zipper_lists(ll1,ll2))
print(zipper_lists(ll1,ll2))