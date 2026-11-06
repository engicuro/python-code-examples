"""Program to reverse a linked list."""

class Node:
    """Node class for a singly linked list."""
    def __init__(self, data):
        self.data = data
        self.next = None

def reverse_a_linked_list():
    """Reverse a singly linked list."""
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)

    def print_list(head):
        current = head
        elements = []
        while current:
            elements.append(str(current.data))
            current = current.next
        print(" -> ".join(elements))

    print("Original linked list:")
    print_list(head)

    prev = None
    current = head
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    head = prev

    print("Reversed linked list:")
    print_list(head)
    return head

if __name__ == "__main__":
    reverse_a_linked_list()
