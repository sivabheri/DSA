class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insertAtBegining(self, val):
        newnode = Node(val)
        if self.head is not None:
            newnode.next = self.head
            self.head.prev = newnode
        self.head = newnode

    def insertAtAnyposition(self, val, pos):
        newnode = Node(val)
        if pos == 0:
            return self.insertAtBegining(val)
        temp = self.head
        prev = None
        cur_pos = 0
        while temp is not None and cur_pos < pos:
            prev = temp
            temp = temp.next
            cur_pos += 1
        if prev is not None:
            newnode.next = temp
            newnode.prev = prev
            prev.next = newnode
            if temp is not None:
                temp.prev = newnode

    def deleteNode(self, pos):
        temp = self.head
        cur_pos = 0
        if pos == 0 and temp is not None:
            self.head = temp.next
            if self.head is not None:
                self.head.prev = None
            return
        prev = None
        while temp is not None and cur_pos < pos:
            prev = temp
            temp = temp.next
            cur_pos += 1
        if temp is not None:
            prev.next = temp.next
            if temp.next is not None:
                temp.next.prev = prev

    def show(self):
        temp = self.head
        if temp is None:
            print("The List is Empty!")
            return
        while temp:
            print(temp.data, end=" ")
            temp = temp.next

    def reverse(self):
        temp = self.head
        if temp is None or temp.next is None:
            return 
        prev = None
        
        while(temp):
            next_node = temp.next
            temp.next = prev
            temp.prev = next_node 
            prev = temp
            temp = next_node
            
        self.head = prev

if __name__ == '__main__':
    LL = LinkedList()
    LL.insertAtBegining(1)
    LL.insertAtBegining(2)
    LL.insertAtAnyposition(3, 0)
    LL.reverse()
    LL.show()