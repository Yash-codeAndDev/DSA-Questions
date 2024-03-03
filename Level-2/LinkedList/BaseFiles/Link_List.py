class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insertAtBegin(self, data =-1):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        else:
            new_node.next = self.head
            self.head = new_node

    def insertAtIndex(self, data, index):
        new_node = Node(data)
        current_node = self.head
        position = 0
        if position == index:
            self.insertAtBegin(data)
        else:
            while (current_node != None and position + 1 != index):
                position = position + 1
                current_node = current_node.next

            if current_node != None:
                new_node.next = current_node.next
                current_node.next = new_node
            else:
                print("Index not present")

    # Method to add a node at the end of LL

    def insertAtEnd(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return

        current_node = self.head
        while (current_node.next):
            current_node = current_node.next

        current_node.next = new_node

    # Update node of a linked list
    # at given position
    def updateNode(self, val, index):
        current_node = self.head
        position = 0
        if position == index:
            current_node.data = val
        else:
            while (current_node != None and position != index):
                position = position + 1
                current_node = current_node.next

            if current_node != None:
                current_node.data = val
            else:
                print("Index not present")

    # Method to remove first node of linked list

    def remove_first_node(self):
        if (self.head == None):
            return

        self.head = self.head.next

    # Method to remove last node of linked list
    def remove_last_node(self):

        if self.head is None:
            return

        current_node = self.head
        while (current_node.next.next):
            current_node = current_node.next

        current_node.next = None

    # Method to remove at given index
    def remove_at_index(self, index):
        if self.head == None:
            return

        current_node = self.head
        position = 0
        if position == index:
            self.remove_first_node()
        else:
            while (current_node != None and position + 1 != index):
                position = position + 1
                current_node = current_node.next

            if current_node != None:
                current_node.next = current_node.next.next
            else:
                print("Index not present")

    # Method to remove a node from linked list
    def remove_node(self, data):
        current_node = self.head

        if current_node.data == data:
            self.remove_first_node()
            return

        while (current_node != None and current_node.next.data != data):
            current_node = current_node.next

        if current_node == None:
            return
        else:
            current_node.next = current_node.next.next

    # Print the size of linked list
    def sizeOfLL(self):
        size = 0
        if (self.head):
            current_node = self.head
            while (current_node):
                size = size + 1
                current_node = current_node.next
            return size
        else:
            return 0

    # print method for the linked list
    def printLL(self):
        current_node = self.head
        while (current_node):
            print(current_node.data)
            current_node = current_node.next


if __name__ == "__main__":
    linked_list = LinkedList()

    # Append elements to the linked list with values
    linked_list.insertAtEnd(1)
    linked_list.insertAtEnd(2)
    linked_list.insertAtEnd(3)

    # Display the linked list
    linked_list.printLL()

    # Append elements to the linked list without values
    linked_list.insertAtEnd()
    linked_list.insertAtEnd("Hello")

    linked_list.printLL()