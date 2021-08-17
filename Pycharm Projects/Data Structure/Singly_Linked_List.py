class Node():
    def __init__(self,data):
        self.data = data
        self.next = None

class Singly_Linked_List():
    def __init__(self):
        self.head = None
        self.counter = 0

    def create(self):
        while(True):
            myChoice = input("Do you want to add node in linked list (y/n) : ")
            if myChoice == "y" or myChoice == "Y":
                myData = int(input("Enter data for the  node : "))
                newnode = Node(myData)
                if self.head == None:
                    self.head = newnode
                    current = newnode
                else:
                    current.next = newnode
                    current = current.next
                self.counter += 1

            if myChoice == "n" or myChoice == "N":
                break

    def display(self):
        if self.head == None:
            print("Linked list is empty")
        else:
            current = self.head
            while current != None:
                print(current.data)
                current = current.next

    def myCount(self):
        print(f"Total count of all nodes is : {self.counter}")

    def insertFirst(self):
        myData = int(input("Enter data to insert : "))
        newnode = Node(myData)
        if self.head == None:
            self.head = newnode
            self.counter += 1
        else:
            newnode.next = self.head
            self.head = newnode
            self.counter += 1


    def insertLast(self):
        if self.head == None:
            self.insertFirst()
        else:
            current = self.head
            while current.next != None:
                current = current.next
            myData = int(input("Enter data to insert : "))
            newnode = Node(myData)
            current.next = newnode
            self.counter += 1


    def insertAfter(self):
        position = int(input("Enter position after which you want to insert node : "))
        if position > self.counter or position < 0:
            print("Invalid position")
        elif position == self.counter:
            self.insertLast()
        elif position == 0:
            self.insertFirst()
        else:
            i = 1
            current = self.head
            while i < position :
                current = current.next
                i += 1
            myData = int(input("Enter data to insert after given position : "))
            newnode = Node(myData)
            newnode.next = current.next
            current.next = newnode
            self.counter += 1


    def insertBefore(self):
        position = int(input("Enter position before which you want to insert a node : "))
        if position == 1:
            self.insertFirst()
        elif position < 1 or position > self.counter+1:
            print("Invalid position")
        elif position == self.counter + 1:
            self.insertLast()
        else:
            current = self.head
            i = 1
            while i < (position-1):
                current = current.next
                i += 1
            myData = int(input("Enter data to insert before given position : "))
            newnode = Node(myData)
            newnode.next = current.next
            current.next = newnode
            self.counter += 1


    def deleteFirst(self):
        if self.head == None:
            print("List is empty")
        else:
            current = self.head
            self.head = current.next
            self.counter -= 1



    def deleteLast(self):
        if self.head == None:
            print("List is empty")
        elif self.counter == 1:
            self.head = None
            self.counter -= 1
        else:
            current = self.head
            prev = None
            while current.next != None:
                prev = current
                current = current.next
            prev.next = None
            self.counter -= 1


    def deletePosition(self):
        if self.head == None:
            print("List is empty")
        else:
            position = int(input("Enter position to delete : "))
            if position < 1 or position > self.counter:
                print("Invalid position")
            elif position == 1:
                self.deleteFirst()
            else:
                current = self.head
                i = 1
                prev = None
                while i < position:
                    prev = current
                    current = current.next
                    i += 1
                prev.next = current.next
                self.counter -= 1



    def reverse(self):
        if self.head == None:
            print("List is empty")
        elif self.counter == 1:
            pass
        else:
            nextnode = self.head
            current = self.head
            prev = None
            while nextnode != None:
                nextnode = nextnode.next
                current.next = prev
                prev = current
                current = nextnode
            self.head = prev


if __name__ == "__main__":
    sll = Singly_Linked_List()
    while(True):
        print("\n")
        print("Select one choice : \n")
        print("Create Singly Linked List : 1")
        print("Display : 2")
        print("Count : 3")
        print("Insert at begineeing : 4")
        print("Insert at end : 5")
        print("Insert after given position : 6")
        print("Insert before given position : 7")
        print("Delete first : 8")
        print("Delete last : 9")
        print("Delete given position : 10")
        print("Reverse : 11")
        print("Quit : 100\n")
        choice = int(input("Enter your choice : "))
        print("\n")
        if choice == 1 :
            sll.create()
        if choice == 2:
            sll.display()
        if choice == 3:
            sll.myCount()
        if choice == 4:
            sll.insertFirst()
        if choice == 5:
            sll.insertLast()
        if choice == 6:
            sll.insertAfter()
        if choice == 7:
            sll.insertBefore()
        if choice == 8:
            sll.deleteFirst()
        if choice == 9:
            sll.deleteLast()
        if choice == 10:
            sll.deletePosition()
        if choice == 11:
            sll.reverse()
        if choice == 100:
            print("\nThank You!!!\n")
            break

