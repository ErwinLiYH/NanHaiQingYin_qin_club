class student:#没有选同修,也没有被选为同修的学生
    name = ''
    choosen_leassons = []
    def __init__(self,leassons_list):
        self.choosen_leassons = leassons_list
    def get_num(self)->int:
        return len(self.choosen_leassons)

class student_combination:#选了同修的同学与被选同学组成的学生对
    name_pair = None
    communal_lessons = []
    def __init__(self,student1,student2):
        self.name_pair = (student1.name,student2.name)
        self.communal_lessons = [i for i in student1.choosen_leassons if i in student2.choosen_leassons]
    def get_num(self)->int:
        return len(self.communal_lessons)

class leasson:
    students_list = []
    def __init__(self):
        pass
    def add_student(self,student):
        self.students_list.append(student.name)
    def minus_student(self,student):
        self.students_list.remove(student.name)
    def add_student_combination(self,student_combination):
        self.students_list.append(student_combination.name_pair[0])
        self.students_list.append(student_combination.name_pair[1])
    def minus_student_combination(self,student_combination):
        self.students_list.remove(student_combination.name_pair[0])
        self.students_list.remove(student_combination.name_pair[1])