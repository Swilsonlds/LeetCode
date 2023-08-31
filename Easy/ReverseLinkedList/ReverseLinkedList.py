# Given the head of a singly linked list, reverse the list, and return the reversed list.

# Linked list node to be used in the problem
class LinkedListNode():
    def __init__(self, value):
        self.value = value
        self.next = None

def ReverseLinkedList(head: LinkedListNode):
    previous = None
    current = head

    while current:
        temp = current.next
        current.next = previous
        previous = current
        current = temp
    return previous


