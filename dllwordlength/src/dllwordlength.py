
class Node:

    def __init__(self, value=None, next=None, prev=None):
        self.value = value 
        self.next = next #We need a pointer to the next element of our list 
        self.prev = prev #and another pointing backwards 

    def set_value(self, value):
        self.value = value

    def get_value(self):
        return self.value

    def set_next(self, next): 
        self.next = next

    def get_next(self):
        return self.next

    def has_next(self):
        return self.next != None

    def set_prev(self, prev):
        self.prev = prev

    def get_prev(self):
        return self.prev

    def has_prev(self):
        return self.prev != None

    def __str__(self):
        return "None[value = %s]"

class DoubleLinkedList:
    def __init__(self): #A doubly linked list will always have a front and an end 
        self.front = None 
        self.end = None

    def insert(self, value): 
        if (self.front == None):
            self.front = Node(value)
            self.end = self.front
        else:
            cur = self.front
            while (cur.next != None):
                cur = cur.next
            cur.next = Node(value, None, cur)
            self.end = cur.next

    def insert_at_beginning(self, value):
        new_node = Node(value, None, None)
        if (self.front == None):  # To imply that if head == None
            self.front = self.end = new_node
        else:
            new_node.set_prev(None)
            new_node.set_next(self.front)
            self.front.set_prev(new_node)
            self.front = new_node

    def get_node(self, index):
        cur_node = self.front
        if cur_node == None:
            return None
        i = 0
        while i < index and cur_node.get_next() is not None:
            cur_node = cur_node.get_next()
            if cur_node == None:
                break
            i += 1
        return cur_node

    def insert_at(self, index, value):
        new_node = Node(value)
        if self.front == None or index == 0:
            self.insert_at_beginning(value)
        elif index > 0:
            temp = self.get_node(index)
            if temp == None or temp.get_next() == None:
                self.insert(value)
            else:
                next = temp.get_next()
                new_node.set_next(next)
                new_node.set_prev(temp)
                temp.get_next().setPrev(new_node)
                temp.set_next(new_node)

    def find(self, value):
        cur = self.front
        while cur != None:
            if cur.value == value:
                return True
            cur = cur.next
        return False

    def print_elements(self):
        cur = self.front
        if cur == None:
            print("No elements")
            return False
        while (cur != None):
            print(cur.value)
            cur = cur.next
        return True

def arrange_into_doubly_linked_list():
    len_to_word = {} 
    text_file = open('alicewonderland.txt', 'r')
    lines = text_file.readlines() 
    for line in lines: 
        for word in line.split(): 
            if len(word) not in len_to_word.keys(): 
                words_of_same_length = []
                for line in lines:
                    for particle in line.split():
                        if len(particle) == len(word):
                            words_of_same_length.append(particle)
                        continue
                len_to_word[len(word)] = list(set(sorted(words_of_same_length)))
            continue
    text_file.close()
    return len_to_word

def doubly_linked_list_words():
    len_to_word = arrange_into_doubly_linked_list()
    for len in len_to_word.keys():
        word_length = DoubleLinkedList()
        word_length.insert(str(len) + ": ")
        for word in len_to_word[len]:
            word_length.insert(word)
            word_length.insert("<->")
        word_length.print_elements()

if __name__ == '__main__':
    # Initializing list
    doubly_linked_list_words()



