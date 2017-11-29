from time import strftime


class Node():

    def __init__(self, data):
        self.left = None
        self.parent = data
        self.right = None

    def get_data(self):
        return self.parent

    def set_right(self, ID):
        self.right = ID

    def get_parent(self):
        return self.parent

    def get_left_child(self):
        return self.left

    def get_right_child(self):
        return self.right

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
        has_right = False
        has_left = False
        if new_subtree:
            self.root = Node(ID) #We add the root
            return True
        else:
            if ID < self.root.get_data():
                self.root.set_left(ID)
                has_left = True
                return True
            if ID > self.root.get_data():
                self.root.set_right(ID)
                has_right = True
            if has_right and has_left:
                return False

    def get_parent(self): #It will only work when a value has already been added else will return None
        return self.root.get_parent() #The program constraints won't let that happen

    def get_left_child(self):#It will only work when a value has already been added else will return None
        return self.root.get_left_child()#The program constraints won't let that happen

    def get_right_child(self):#It will only work when a value has already been added else will return None
        return self.root.get_right_child()#The program constraints won't let that happen

    def merge_right(self, tree_to_be_updated, tree_to_be_merged):
        """We merge subtrees a good way of thinking of it is by imagining some grapes
           it is like plucking a grape and replacing it by one or more grapes"""
        tree_to_be_updated.set_right = tree_to_be_merged #and replace it by another grape
        #Taking advantage of dynamic typing we can reset what  was an integer value by a subtree object
    def merge_left(self, tree_to_be_updated, tree_to_be_merged):
        """We merge subtrees a good way of thinking of it is by imagining some grapes
                   it is like plucking a grape and replacing it by one or more grapes"""
        tree_to_be_updated.set_left = tree_to_be_merged #and replace it by another grape


class student():

    def __init__(self, data):
        self.name = data[0]
        self.home_address = data[1]
        self.course_ID = data[2]
        self.birth_date = data[3]
        self.enrolment_date = data[4]
        self.status = data[5]

    def display_data(self):
        print("Name: " + self.name + "\n" + "Course ID: " + self.course_ID + "\n" + "Birth date: " + self.birth_date + "\n" +
              "Enrolment date: " + self.enrolment_date + "\n" + "Status: " + self.status + "\n")

    def set_home_address(self, home_address):
        self.home_address = home_address

    def set_name(self, name):
        self.name = name

    def set_ID(self, ID):
        self.ID = ID

    def set_birth_date(self, birth_date):
        self.birth_date = birth_date

    def set_course_ID(self, courseID):
        self.course_ID = courseID

    def set_enrolment_date(self, enrolment):
        self.enrolment_date = enrolment

    def set_status(self, status):
        self.status = status

    def info_update(self, index):
        index -= 1
        update = input("Type in the information")
        if index == 0:
            self.set_ID(update)
        if index == 1:
            self.set_birth_date(update)
        if index == 2:
            self.set_course_ID(update)
        if index == 3:
            self.set_birth_date(update)
        if index == 4:
            self.set_enrolment_date(update)
        if index == 5:
            self.set_status()

    def get_home_address(self):
        return self.home_address

    def get_name(self):
        return self.name

    def get_ID(self):
        return self.ID

    def get_birth_date(self):
        return self.birth_date

    def get_course_ID(self):
        return self.course_ID

    def get_enrolment_date(self):
        return self.enrolment_date

    def get_status(self):
        return self.status

class student_registration():
    """The BST implementation is fully integrated in the system, and works as a way of storing each student's unique ID
    """
    def __init__(self):
        self.tree = None
        self.main_subtree = None
        self.current_subtree = None
        self.initialise = True
        self.new_subtree = True
        self.db_students = []
        self.IDs = []

    def new_student(self, ID, data):
        if self.initialise: #If we start the tree
            if self.new_subtree: #If we start a new subtree
                self.main_subtree = subtree()
                self.main_subtree.add_ID(ID, self.new_subtree)
                self.db_students[ID] = data
                self.new_subtree = False
            elif self.main_subtree.add_ID(ID, self.new_subtree): #If the tree already has a parent and a children
                self.current_subtree = self.main_subtree #The main
                self.db_students[ID] = student(data)
            else:
                self.db_students[ID] = self.new_student(self, data)
                self.db_students[ID] = student(data)
                self.IDs.append(self.current_subtree)
                self.initialise = False
                self.new_subtree = True #We set new subtree to true in case it can be
                self.tree = self.current_subtree
        else: #The resulting option is to create a new subtree once the main subtree has been added
            if self.new_subtree == True:
                self.current_subtree = subtree()
                self.current_subtree.add_ID(ID, self.new_subtree)
                self.new_subtree = False
                self.db_students[ID] = student(data)
            elif self.current_subtree.add_ID(ID, self.new_subtree):
                self.db_students[ID] = student(data)
                self.new_subtree = False
            else: #If the subtree has already been filled
                self.db_students[ID] = student(data)
                self.IDs.append(self.current_subtree)
                self.new_subtree = True

    def update_info(self, student):
        to_be_updated = 0
        while(True):
            print("\n")
            print("1) Student name")
            print("\n")
            print("2) Birth date")
            print("\n")
            print("3) Home address")
            print("\n")
            print("4) Class ID")
            print("\n")
            print("5) Date of enrolment")
            print("\n")
            print("6) Status")
            to_be_updated = input("Update information by typing in number: ")
            break
        student.info_update(to_be_updated)

    def lookup(self, ID):
        for student_ID in self.IDs:
            if student_ID.get_parent() == ID or student_ID.get_left() == ID or student_ID.get_right():
                student = self.db_students[ID]
                student.display_data()
                break
            continue

    def display_data(self, data):
        for i in range(len(data)):
            print(data[i])
            print("\n")

    def list_lexicographic_order_by_class(self, course_ID):
        lexicographic_students = []
        for ID in self.IDs:
            student = self.db_students[ID]
            if student.get_course_ID() == course_ID:
                lexicographic_students.append(student.get_name())
        lexicographic_students = sorted(lexicographic_students)
        self.display_data(lexicographic_students)

    def list_lexicographic_order_by_name(self):
        lexicographic_students = []
        for ID in self.IDs:
            student = self.db_students[ID]
            lexicographic_students.append(student.get_name())
        lexicographic_students = sorted(lexicographic_students)
        self.display_data(lexicographic_students)

    def list_graduated_students(self):
        graduated_students = []
        for ID in self.IDs:
            student = self.db_students[ID]
            if student.get_status() == "graduate":
                graduated_students.append(student.get_name())
                break
        graduated_students = sorted(graduated_students)
        self.display_data(graduated_students)

    def list_undergrad_students(self):
        undergrad_students = []
        for ID in self.IDs:
            student = self.db_students[ID]
            if student.get_status() == "graduate":
                undergrad_students.append(student.get_name())
                return
        undergrad_students = sorted(undergrad_students)
        self.display_data(undergrad_students)

    def delete_student_by_code(self, ID):
        for studentID in self.IDs:
            if studentID == ID:
                student = self.db_students[ID]
                self.db_students.remove(student)
                return

    def delete_all_graduates(self, ID):
        undergrad_students = []
        for ID in self.IDs:
            student = self.db_students[ID]
            if student.get_status() == "graduate":
                self.db_students.remove(student)
                return
        self.display_data(undergrad_students)

if __name__ == '__main__':
