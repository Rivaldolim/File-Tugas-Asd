class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data): #data yang akan di masuukan
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def hapus(self): # Untuk Menghapus List Barang
        if self.head is None:
            
            print("Linked List Kosong")
        else:
            self.head = self.head.next
  
    def print_list(self):
        current_node = self.head
        while current_node:
            print(current_node.data)
            current_node = current_node.next

car_list = LinkedList

car_list = LinkedList()
car_list.insert("Honda Brio")
car_list.insert("Toyota All new")
car_list.insert("Daihatsu Sigra")
car_list.insert("Wuling Confero")
car_list.insert("Hyundai Stragezer")
car_list.insert("Kia Sorento")
car_list.insert("Suzuki carry")
car_list.insert("Suzuki carimun")
car_list.insert("Toyota All new RUSh")
car_list.insert("All new Toyota Yaris GR")
car_list.insert("Honda BRV")
car_list.insert("honda CRV")
car_list.insert("Mitshubisi Xpander cross")
car_list.insert("Mitshubisi Xpander ultimate")
car_list.insert("Honda Moblio")
car_list.insert("Toyota Carya")
car_list.insert("Daihatsu Granmax")
car_list.insert("Daihatsu Sigra")
car_list.insert("Mazda cx2")
car_list.insert("Mazda cx3")
car_list.insert("Toyota fortuner")
car_list.insert("Kia RIo")
car_list.insert("Kia Seltos") 
car_list.insert("Mitshubisi Pajero")
car_list.insert("Nissan Serena")
car_list.hapus()
print("List of Popular Cars:")
car_list.print_list()