import random

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

start = Node(False)
current_node = start
for i in range(random.randint(5,10)):
    new_node = Node(bool(random.getrandbits(1)))
    current_node.next = new_node
    current_node = new_node

# display linked list before joining
current_node = start
while current_node.next != None:
    print(current_node.data, end=" ")
    current_node = current_node.next

# join linked list
current_node.next = start

list_length = 0
start.data = True
current_node = start.next
while True:
    if current_node.data == True:
        current_node.data = False

    if start.data == False:
        break

    list_length += 1
    current_node = current_node.next

print(list_length)