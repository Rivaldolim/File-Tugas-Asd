class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def print_list(self):
        current_node = self.head
        while current_node:
            print(current_node.data)
            current_node = current_node.next

car_list = LinkedList()
car_list.insert("Honda Brio")
car_list.insert("Toyota All new")
car_list.insert("Daihatsu Sigra")
car_list.insert("Wuling Confero")

print("List of Popular Cars:")
car_list.print_list()