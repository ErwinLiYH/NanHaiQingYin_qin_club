import pandas as pd
#import pickle
import time
import random
from student import Student
from pair import Pair
from course import Course

def generate(xlsx_path, time_column, name_column, id_column, pairName_column, pairID_column, class_column):
    student_list = []
    class_list = []
    pair_list = []

    time_series = pd.read_excel(xlsx_path, engine='openpyxl', 
    usecols=time_column, squeeze=True)

    index_series = list(range(len(time_series)))
    
    name_series = pd.read_excel(xlsx_path, engine='openpyxl', 
    usecols=name_column, squeeze=True)

    # check duplicate
    flag = name_series.duplicated()
    if flag.any() == True:
        du = ''
        for i in name_series.loc[flag]:
            du+=(i+' ')
        raise Exception("Exists duplicate name, %s"%du)

    id_series = pd.read_excel(xlsx_path, engine='openpyxl', 
    usecols=id_column, squeeze=True)
    
    pairName_series = pd.read_excel(xlsx_path, engine='openpyxl', 
    usecols=pairName_column, squeeze=True)
    
    pairID_series = pd.read_excel(xlsx_path, engine='openpyxl', 
    usecols=pairID_column, squeeze=True)

    class_frame = pd.read_excel(xlsx_path, engine='openpyxl', 
    usecols=class_column)

    class_series = []
    
    for i in range(class_frame.shape[0]):
        for j in range(class_frame.shape[1]):
            c = class_frame.iloc[i,j].strip()
            if c != "(跳过)":
                class_series.append(c)

    # standard dataframe
    data = pd.DataFrame(
        data = {
            "index": index_series,
            "time": time_series,
            "name":name_series,
            "id":id_series,
            "pairName":pairName_series,
            "pairID":pairID_series,
            "candidate_class":class_series
        }
    )

    # generate students and pairs
    index = []
    for i in range(data.shape[0]):
        if i not in index:
            if data.iloc[i]["pairName"].strip() == "(空)": # 未选同修
                classes = data.iloc[i]["candidate_class"].strip().split("┋")
                final_time = time.mktime(time.strptime(data.iloc[i]["time"],'%Y/%m/%d %H:%M:%S'))
                Astudent = Student(
                    data.iloc[i]["name"].strip(),
                    data.iloc[i]["id"].strip(),
                    classes,
                    final_time
                )
                student_list.append(Astudent)
                index.append(i)
            elif data.iloc[i]['name'].strip() == data.iloc[i]['pairName'].strip(): #选的同修是自己
                classes = data.iloc[i]["candidate_class"].strip().split("┋")
                final_time = time.mktime(time.strptime(data.iloc[i]["time"],'%Y/%m/%d %H:%M:%S'))
                Astudent = Student(
                    data.iloc[i]["name"].strip(),
                    data.iloc[i]["id"].strip(),
                    classes,
                    final_time
                )
                student_list.append(Astudent)
                index.append(i)
            elif data.loc[data["name"] == data.iloc[i]["pairName"]].shape[0] == 0: #选的人不存在
                classes = data.iloc[i]["candidate_class"].strip().split("┋")
                final_time = time.mktime(time.strptime(data.iloc[i]["time"],'%Y/%m/%d %H:%M:%S'))
                Astudent = Student(
                    data.iloc[i]["name"].strip(),
                    data.iloc[i]["id"].strip(),
                    classes,
                    final_time
                )
                student_list.append(Astudent)
                index.append(i)
            else:
                pair_temp = data.loc[data["name"] == data.iloc[i]["pairName"]]
                pair_index = int(pair_temp["index"].iloc[0])
                pair = data.iloc[pair_index]
                if pair_temp.shape[0] != 1:
                    raise Exception("name must be unique, %s is not unique"%pair["name"])
                #print(pair["pairName"].strip(),data.iloc[i]["name"].strip())
                if pair["pairName"].strip() == data.iloc[i]["name"].strip():
                    # generate pair
                    classes1 = set(data.iloc[i]["candidate_class"].strip().split("┋"))
                    classes2 = set(pair["candidate_class"].strip().split("┋"))
                    classes = list(classes1&classes2)
                    final_time1 = time.mktime(time.strptime(data.iloc[i]["time"],'%Y/%m/%d %H:%M:%S'))
                    final_time2 = time.mktime(time.strptime(data.iloc[i]["time"],'%Y/%m/%d %H:%M:%S'))
                    if final_time1<final_time2:
                        final_time = final_time2
                    else:
                        final_time = final_time1
                    Apair = Pair(
                        data.iloc[i]["name"],
                        data.iloc[i]["id"],
                        pair["name"],
                        pair["id"],
                        classes,
                        final_time
                    )
                    pair_list.append(Apair)
                    index.append(i)
                    index.append(pair_index)
                else: # 未互选
                    classes = data.iloc[i]["candidate_class"].strip().split("┋")
                    final_time = time.mktime(time.strptime(data.iloc[i]["time"],'%Y/%m/%d %H:%M:%S'))
                    Astudent = Student(
                        data.iloc[i]["name"].strip(),
                        data.iloc[i]["id"].strip(),
                        classes,
                        final_time
                    )
                    student_list.append(Astudent)
                    index.append(i)
        else:
            pass
    # with open('data.p', 'wb') as f:
    #     pickle.dump({'data':data,'student':student_list,'pair':pair_list},f)
    
    # generate classes
    temp_class = []
    for i in range(data.shape[0]):
        for j in data["candidate_class"][i].strip().split("┋"):
            temp_class.append(j)

    class_data = pd.Series(temp_class).value_counts()

    for name,freq in class_data.items():
        Aclass = Course(
            name,
            None,
            freq
        )
        class_list.append(Aclass)
    return student_list, pair_list, class_list
    
def find_object(object_list,key,by):
    index = []
    for i in range(len(object_list)):
        if object_list[i].__dict__[by] in key:
            index.append(i)
        else:
            pass
    return index

def arrange(students, pairs, classes):
    students = sorted(students,key=lambda x:(x.DF,x.finish_time))
    pairs = sorted(pairs,key=lambda x:(x.DF,x.finish_time))
    for i in pairs:
        index_list = find_object(classes,i.candidate_class,'name')
        
        class_list = [classes[j] for j in index_list]
        random.shuffle(class_list)
        class_list = sorted(class_list,key=lambda x:x.frequency)
        final_class = class_list[0].name
        
        index = find_object(classes,final_class,'name')
        classes[index[0]].add_pair(i)
    for i in students:
        index_list = find_object(classes,i.candidate_class,'name')
        
        class_list = [classes[j] for j in index_list]
        random.shuffle(class_list)
        class_list = sorted(class_list,key=lambda x:x.frequency)
        final_class = class_list[0].name
        
        index = find_object(classes,final_class,'name')
        classes[index[0]].add_student(i)

    return students, pairs, classes

def to_txt(classes):
    str = ""
    for i in classes:
        str+=('\n****************************\n%s\n被选次数: %d, 人数:%d\n'%(i.name,i.frequency,i.current_num))
        for j in i.students:
            str+=('%s\n'%j.name)
        for j in i.pairs:
            str+=('%s\t%s\n'%(j.name1,j.name2))
    return str