class Student:
    def __init__(self,name,id,candidate_class,finish_time):
        self.name=name
        self.id=id
        self.candidate_class=candidate_class
        self.finish_time=finish_time
        self.DF=len(candidate_class)