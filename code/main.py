import pandas as pd
import course
import student
import pair

def start(txt_path,xlsx_path,num_of_courses,columns_in_xlsx):
    
    # [1] read xlsx to standard data frame
    # starndard data frame:
    # time | name | id | selected course | learned course | pair name | pair id
    # 0    | 1    | 2  | 3                   | 4              | 5         | 6
    raw_data = pd.read_excel(xlsx_path,engine='openpyxl',usecols=columns_in_xlsx)
    shape = raw_data.shape

    # [2] begin generate course, student and pair objects
    courses = []
    students = []
    pairs = []

    students_name = []
    students_id = []
    students_candidate_class = []
    students_finish_time = []

    pair_name1 = []
    pair_id1 = []
    pair_name2 = []
    pair_id2 = []
    pair_candidate_class = []
    pair_finish_time = []
    
    # [2.1] get information from course_info.txt and generate course objects
    # format for course_info.txt:
    # course difficulty max_students_number(-1 means no limitation) frequency
    # example:
    # courseA 2 -1
    # courseB 4 20
    # ......
    with open(txt_path,'r') as course_info:
        lines = [i.rstrip('\n') for i in course_info.readlines()]
    for i in lines:
        courses.append(course.Course(i.split(' ')[0],int(i.split(' ')[1]),int(i.split(' ')[2]),int(i.split(' ')[3])))

    #[2.2] generate pair objects