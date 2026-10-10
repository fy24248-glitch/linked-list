class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def prepend(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def delete(self, value):
        current = self.head
        prev = None
        while current:
            if current.value == value:
                if prev is None:
                    self.head = current.next
                else:
                    prev.next = current.next
                return True
            prev = current
            current = current.next
        return False

    def find(self, value):
        current = self.head
        while current:
            if current.value == value:
                return True
            current = current.next
        return False

    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    def to_list(self):
        result = []
        current = self.head
        while current:
            result.append(current.value)
            current = current.next
        return result

    def __len__(self):
        return len(self.to_list())

    def __str__(self):
        return " -> ".join(str(v) for v in self.to_list())


if __name__ == "__main__":
    ll = LinkedList()
    for v in [1, 2, 3, 4]:
        ll.append(v)

    print("List:", ll.to_list())
    print("Length:", len(ll))
    print("Found 3?", ll.find(3))

    ll.delete(2)
    print("After deleting 2:", ll.to_list())

    ll.reverse()
    print("Reversed:", ll.to_list())
