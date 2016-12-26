class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


    def __repr__(self):
        return str(self.data)


class LinkedList:

    def __init__(self):
        self.head = None
        self.size = 0


    def add(self, data):
        if self.head is None:
            self.head = Node(data)
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = Node(data)
        self.size += 1


    def remove(self, data):
        if self.head.data == data:
            self.head = self.head.next
        else:
            prev = self.head
            curr = self.head.next
            while curr is not None:
                if curr.data == data:
                    break
                prev = curr
                curr = curr.next
            prev.next = curr.next
        self.size -= 1


    def search(self, data):
        temp = self.head
        while temp is not None and temp.data != data:
            temp = temp.next
        return False if temp is None else True
