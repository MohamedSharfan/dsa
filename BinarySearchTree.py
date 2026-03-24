class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, data):
        #node already exists
        if data == self.data:
            return

        if data < self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = Node(data)

        if data > self.data:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = Node(data)



    def search(self, data):
        if self.data == data:
            return True

        if data < self.data:
            if self.left:
                return self.left.search(data)
            else:
                return False
        if data > self.data:
            if self.right:
                return self.right.search(data)
            else:
                return False

    def inorder(self):
        elements = []
        if self.left:
            elements += self.left.inorder()

        elements.append(self.data)

        if self.right:
            elements += self.right.inorder()

        return elements

    def find_min(self):
        if self.left:
            return self.left.find_min()
        else:
            return self.data

    def find_max(self):
        if self.right:
            return self.right.find_max()
        else:
            return self.data

    def calculate_sum(self):
        sum = 0
        if self.left:
            sum += self.left.calculate_sum()

        sum += self.data

        if self.right:
            sum += self.right.calculate_sum()
        return sum

    def preorder(self):
        elements = []

        elements.append(self.data)
        if self.left:
            elements += self.left.preorder()

        if self.right:
            elements += self.right.preorder()
        return elements

    def postorder(self):
        elements = []
        if self.left:
            elements += self.left.postorder()
        if self.right:
            elements += self.right.postorder()
        elements.append(self.data)
        return elements


def build_tree(elements):
    root = Node(elements[0])
    for i in range(1, len(elements)):
        root.add_child(elements[i])
    return root



if __name__ == '__main__':
    elements = [2,3,1,43,12,43]
    root = build_tree(elements)
    print(root.inorder())
    print(root.search(4))
    print(root.find_min())
    print(root.find_max())
    print(root.calculate_sum())
    print(root.preorder())
    print(root.postorder())
