class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinarySearchTree:

    def __init__(self):
        self.root = None
        self.size = 0


    def insert(self, val):
        if self.root is None:
            self.root = Node(val)
        else:
            self.root = self.__insert(self.root, val)


    def contains(self, val):
        return self.__contains(self.root, val)


    def remove(self, val):
        initial_size = self.size
        self.root = self.__remove(self.root, val)
        return initial_size != self.size


    def display(self):
        self.__display(self.root)


    def __insert(self, node, val):
        if node is None:
            self.size += 1
            return Node(val)
        else:
            if val < node.data:
                node.left = self.__insert(node.left, val)
            if val > node.data:
                node.right = self.__insert(node.right, val)
            return node


    def __contains(self, node, val):
        if node is None:
            return False
        if val == node.data:
            return True
        if val < node.data:
            return self.__contains(node.left, val)
        if val > node.data:
            return self.__contains(node.right, val)


    def __remove(self, node, val):
        if node is None:
            return node
        if val < node.data:
            node.left = self.__remove(node.left, val)
        if val > node.data:
            node.right = self.__remove(node.right, val)
        if val == node.data:
            self.size -= 1
            if node.left is None and node.right is None:
                node = None
            elif node.right is None:
                node = node.left
            elif node.left is None:
                node = node.right
            else:
                self.size += 1
                temp = node.left
                while temp is not None:
                    temp = temp.right
                node.data = temp.data
                node.left = self.__remove(node.left, node.data)
        return node


    def __display(self, node):
        if node is not None:
            self.__display(node.left)
            print(node.data)
            self.__display(node.right)
