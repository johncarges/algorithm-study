from linked_list import LinkedList, LL

def reverse_list(ll: LinkedList):
    current, previous = ll.head, None
    
    while current:
        next = current.next
        current.next = previous

        current, previous = next, current

    return LinkedList(previous)

print(LL)
new_LL = reverse_list(LL)
print(new_LL)