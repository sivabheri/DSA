class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insertAtBegining(self, val):
        newnode = Node(val)
        newnode.next = self.head
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
            prev.next = newnode

    def deleteNode(self, pos):
        temp = self.head
        cur_pos = 0
        prev = None
        if pos == 0:
            self.head = temp.next
            return
        while temp is not None and cur_pos < pos:
            prev = temp
            temp = temp.next
            cur_pos += 1
        if temp is not None:
            prev.next = temp.next
            temp = None

    def show(self):
        temp = self.head
        if temp is None:
            print("The List is Empty!")
            return
        else:
            while temp:
                print(temp.data, end=" ")
                temp = temp.next

    def reverse(self):
    	temp = self.head
    	if temp is None or temp.next is None:
    		return temp
    	prev = None
    	nxt = None

    	while(temp):

    		nxt = temp.next
    		temp.next = prev
    		prev = temp
    		temp = nxt

    	self.head = prev


if __name__ == '__main__':
    LL = LinkedList()
    LL.insertAtBegining(1)
    LL.insertAtBegining(2)
    LL.insertAtAnyposition(3, 0)
    LL.reverse()
    LL.show()