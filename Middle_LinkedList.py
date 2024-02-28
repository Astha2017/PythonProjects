class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def find_middle_node(head):
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    return slow

# Example usage:
# Create a linked list: 1 -> 2 -> 3 -> 4 -> 5
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

middle_node = find_middle_node(head)
if middle_node:
    print("Middle node value:", middle_node.val)
else:
    print("Empty list")
