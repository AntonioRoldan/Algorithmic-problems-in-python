class Node():

    def __init__(self, data):
        self.left = None
        self.data = data
        self.right = None

    def get_data(self):
        return self.data

    def set_right(self, ID):
        self.right = ID

    def set_left(self, ID):
        self.left = ID

    def has_right(self):
        if self.right:
            return True
        return False

    def has_left(self):
        if self.left:
            return True
        return False

class subtree():
    """A subtree consists of a root and its two children"""

    def __init__(self):
        self.root = None

    def add_ID(self, ID, new_subtree):
        if new_subtree:
            self.root = Node(ID) #We add the root
            return True
        else:
            if self.root.has_right():
                self.root.set_left(ID)
                return True
            elif self.root.has_left():
                self.root.set_right(ID)
            else:
                return False

class binary_search_tree():

    def __init__(self):
        self.main_subtree = None
        self.current_subtree = None
        self.initialise = True
        self.new_subtree = True
        self.tree = []

    def add_ID(self, ID):
        if self.initialise: #If we start the tree
            if self.new_subtree: #If we start a new subtree
                self.main_subtree = subtree()
                self.main_subtree.add_ID(ID, self.new_subtree)
                print(ID)
                self.new_subtree = False
            elif self.main_subtree.add_ID(ID, self.new_subtree): #If the tree already has a parent and a children
                self.current_subtree = self.main_subtree #The main
            else:
                self.tree.append(self.current_subtree)
                self.initialise = False
                self.new_subtree = True #We set new subtree to true in case it can be
        else: #The resulting option is to create a new subtree once the main subtree has been added
            if self.new_subtree == True:
                self.current_subtree = subtree()
                self.new_subtree = False
            elif self.current_subtree.add_ID(ID, self.new_subtree):
                self.new_subtree = False
            else:
                self.tree.append(self.current_subtree)
                self.new_subtree = True

if __name__ == '__main__':
    def test():
        registration = binary_search_tree()
        registration.add_ID(1111)

    test()