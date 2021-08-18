class Course:
    def __init__(self,name,max_num,frequency):
        self.name=name
        self.students=[]
        self.pairs=[]
        self.current_num=0
        self.max_num=max_num
        self.frequency=frequency
    def add_student(self,student):
        if  self.max_num==None or self.current_num<self.max_num:
            self.students.append(student)
            self.current_num+=1
            return True
        else:
            return False
    def add_pair(self,pair):
        if self.max_num==None or self.current_num<(self.max_num-1):
            self.pairs.append(pair)
            self.current_num+=2
            return True
        else:
            return False