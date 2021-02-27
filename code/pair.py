class pair:
    def __init__(self,name1,id1,name2,id2,candidate_class,finish_time):
        self.name1=name1
        self.id1=id1
        self.name2=name2
        self.id2=id2
        self.candidate_class=candidate_class
        self.finish_time=finish_time
        self.DF=len(candidate_class)