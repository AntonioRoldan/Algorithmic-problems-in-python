
class Node():

    def __init__(self, data=None):
        self.left = None
        self.right = None
        self.data = data

    def set_right(self, data):
        self.right = data

    def set_left(self, data):
        self.left = data

    def get_right(self):
        return self.right

    def get_left(self):
        return self.left

    def get_data(self):
        return self.data

    def has_children(self):
        return self.right != None and self.left != None

class BST():

    def __init__(self, data):
        self.root = Node(data)

    def insert(self, value):
        cur = self.root
        while(True):
            if value > cur.data:
                if cur.right is None:
                    cur.right = Node(value)
                    return
                else:
                    cur = cur.right
            elif value < cur.get_data():
                if cur.left is None:
                    cur.left = Node(value)
                    return
                else:
                    cur = cur.left()

    def print_tree(self):
        while(True):
            cur = self.root
            if cur.data is not None:
                self.left_middle_right(cur)

    def left_middle_right(self, node):
        print(node.right)
        print("\n")
        print(node.data)
        print("\n")
        print(node.right)
        print("\n")

def fill_tree(tree):
    from random import randint
    for _ in range(100):
        tree.insert(randint(0, 100))
    return tree


def main():
    tree = BST(1111)
    fill_tree(tree)
    tree.print_tree()





if __name__ == '__main__':
    #For testing purposes we will have two elements of a specific class where one of the elements in the class with two students is graduate
    #That way we can test more quickly and easily
    main()

