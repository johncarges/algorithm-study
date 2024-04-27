class Node:

    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class LinkedList:

    def __init__(self, head):
        self.head = head
    
    def to_array(self) -> list:
        current = self.head
        out = []
        while current:
            out.append(current.val)
            current = current.next
        return out
    
    def __repr__(self):
        return str(self.to_array())

    def insert_val(self, val, index=0):
        if index == 0:
            self.head = Node(next=self.head, val=val)
            return
        current = self.head
        for _ in range(index-1):
            if not current.next:
                break
            current = current.next
            print(current.val)
        
        new_node = Node(next=current.next, val=val)
        current.next = new_node

    def find_value(self, val):
        current = self.head
        while current:
            if current.val == val:
                return True
            current = current.next
        return False

    def from_index(self, index):
        current = self.head

        while index > 0:
            current = current.next
            if not current:
                return None
            index -=1
        return current.val

n0 = Node(0, None)
n1 = Node(1, n0)
n2 = Node(2, n1)
n3 = Node(3,n2)

LL = LinkedList(n3)

# print(LL)

# LL.insert_val(val=4,index=10)

# print(LL)

# print(LL.find_value(3))

# print(LL.from_index(4))