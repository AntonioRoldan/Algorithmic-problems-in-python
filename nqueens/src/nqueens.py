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
                return has_left
            if ID > self.root.get_data():
                self.root.set_right(ID)
                has_right = True
                return has_right
            if has_right and has_left:
                return False #We are done with the

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
        self.birth_date = data[2]
        self.enrolment_date = data[3]
        self.course_ID = data[4]
        print(self.course_ID)
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
        self.db_students = {}
        self.IDs = []

    def new_student(self, ID, data):
        if self.initialise: #If we start the tree
            if self.new_subtree: #If we start a new subtree
                self.main_subtree = subtree()
                self.main_subtree.add_ID(ID, self.new_subtree)
                self.db_students[ID] = student(data) #Each node is a student ID
                self.new_subtree = False
                print(ID)
            elif self.main_subtree.add_ID(ID, self.new_subtree): #If the tree already has a parent and a children
                self.current_subtree = self.main_subtree #The main
                self.db_students[ID] = student(data)
                print(ID)
            else:
                self.db_students[ID] = self.new_student(self, data)
                self.db_students[ID] = student(data)
                self.IDs.append(self.current_subtree)
                self.initialise = False
                self.new_subtree = True #We set new subtree to true in case it can be
                self.tree = self.current_subtree
                print(ID)
        else: #The resulting option is to create a new subtree once the main subtree has been added
            if self.new_subtree == True:
                self.current_subtree = subtree()
                self.current_subtree.add_ID(ID, self.new_subtree)
                self.new_subtree = False
                self.db_students[ID] = student(data)
                print(ID)
            elif self.current_subtree.add_ID(ID, self.new_subtree):
                self.db_students[ID] = student(data)
                self.new_subtree = False
                print(ID)
            else: #If the subtree has already been filled
                self.db_students[ID] = student(data)
                self.IDs.append(self.current_subtree)
                self.new_subtree = True
                print(ID)

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
                student.info_update()
                break
            continue

    def display_data(self, data):
        for element in data:
            print(element)

    def list_lexicographic_order_by_class(self, course_ID):
        lexicographic_students = []
        for ID in self.db_students.keys():
            student = self.db_students[ID]
            if student.get_course_ID() == course_ID:
                lexicographic_students.append(student.get_name())
        lexicographic_students = sorted(lexicographic_students)
        self.display_data(lexicographic_students)

    def list_lexicographic_order_by_name(self):
        lexicographic_students = []
        for ID in self.db_students.keys():
            student = self.db_students[ID]
            lexicographic_students.append(student.get_name())
        lexicographic_students = sorted(lexicographic_students)
        self.display_data(lexicographic_students)

    def list_graduated_students(self):
        graduated_students = []
        for ID in self.db_students.keys():
            student = self.db_students[ID]
            if student.get_status() == "graduate":
                graduated_students.append(student.get_name())
                break
        graduated_students = sorted(graduated_students)
        self.display_data(graduated_students)

    def list_undergrad_students(self):
        undergrad_students = []
        for ID in self.db_students.keys():
            student = self.db_students[ID]
            if student.get_status() == "undergrad":
                undergrad_students.append(student.get_name())
                break
        undergrad_students = sorted(undergrad_students)
        self.display_data(undergrad_students)

    def delete_student_by_code(self, ID):
        for studentID in self.db_students.keys():
            if studentID == ID:
                student = self.db_students[ID]
                del self.db_students[ID]
                return

    def delete_all_graduates(self):
        undergrad_students = []
        for ID in self.db_students.keys():
            student = self.db_students[ID]
            if student.get_status() == "graduate":
                del self.db_students[ID]
                return
        self.display_data(undergrad_students)



if __name__ == '__main__':
    #For testing purposes we will have two elements of a specific class where one of the elements in the class with two students is graduate
    #That way we can test more quickly and easily
    student_registration = student_registration()
    student_registration.new_student(2000, ("David", "Dragon Alley 3 ", "09/11/2000", strftime("%d/%m/%Y"), "220CT", "undergrad"))
    student_registration.new_student(1117, ("Michael", "Dangerous hill 4", "07/08/1996", strftime("%d/%m/%Y"), "220CT", "graduate"))
    student_registration.new_student(1111, ("Antonio", "Albert Einstein 34", "02/10/1995", strftime("%d/%m/%Y"), "210CT", "undergrad"))
    print("In order by name: " + "\n")
    student_registration.list_lexicographic_order_by_name()
    print("\n")
    print("In order by name, group by class: " + "\n")
    student_registration.list_lexicographic_order_by_class("220CT")
    print("\n")
    print("Graduated students: " + "\n")
    student_registration.list_graduated_students()
    print("\n")
    print("Undergraduated_students: " + "\n")
    student_registration.list_undergrad_students()
    print("\n")
    print("Delete student by code")
    student_registration.delete_student_by_code(2000)
    print("\n")
    print("Resulting students: ")
    student_registration.list_lexicographic_order_by_name()
    print("\n")
    print("Delete all graduated students: ")
    student_registration.delete_all_graduates()
    print("\n")
    print("Resulting students: ")
    student_registration.list_lexicographic_order_by_name()
