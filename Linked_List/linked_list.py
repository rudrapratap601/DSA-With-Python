class Node:

    def __init__(self, data):

        self.data = data
        self.next = None

# Creating Nodes
node1 = Node(20)
node2 = Node(97)
node3 = Node(21)
node4 = Node(87)

# assigning next values
node1.next = node2
node2.next = node3
node3.next = node4


# Printing the Linked list
def print_ll(head):
    current = head

    while current is not None:

        print(current.data, end = " -> ")
        current = current.next

    print("None")

# Count the number of nodes in a Linked List

def ll_length(head):
    count = 0
    current = head
    while current is not None:
        count += 1
        current = current.next
    return count

def sum_of_node(head):
    current = head
    sum_ = 0

    while current is not None:
        sum_ += current.data
        current = current.next

    return sum_

head = node1

print_ll(head)
print(f"Lenght of linked list = {ll_length(head)}")
print(f"Sum of node values  = {sum_of_node(head)}")


