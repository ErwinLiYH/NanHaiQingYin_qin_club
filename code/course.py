class Course:
    def __init__(self,name,difficulty,max_num,frequency):
        self.name=name
        self.difficulty=difficulty
        self.students=[]
        self.pairs=[]
        self.current_num=0
        self.max_num=max_num
        self.frequency=frequency
    def add_student(self,student):
        if self.current_num<self.max_num:
            self.students.append(student)
            self.current_num+=1
            return True
        else:
            return False
    def add_pair(self,pair):
        if self.current_num<(self.max_num-1):
            self.pairs.append(pair)
            self.current_num+=2
            return True
        else:
            return False