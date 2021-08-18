# 南海清音古琴社自动化选课后台程序规划

问卷星制作问卷->导出为xlsx文件,作为原始数据(按选项文本导出)->数据清洗,计算班级频数(说明见3.3), 输出处理后的数据->排课->输出课表为json文件(方便后续处理,如后期建立图形界面)

编程语言: python

## 1.问卷示例

见二维码所指问卷:

<img src="./statistics/img/qrcode.jpg" style="zoom:50%;" />

## 2.输入数据示例

![]()

K,L,M,N,O,P列为第四题(所选的曲目课程课程), 分别代表所学曲目数量决定的可选课程

## 3.排课逻辑

基于自由度, 问卷填写时间, 班级频数进行排课.

### 3.1.自由度

自由度分为个人自由度与同修自由度(一般只存在于开指班选课)

个人自由度: 当没有选同修时, 所选择的课程数量即为个人自由度. 如A同学选了课程一和课程二且没有选择同修,其个人自由度为2.

同修自由度: 当两人互相选择对方为同修时, 双方会被绑定为一对, 双方所选的重叠的课程的数目为同修自由度. 如A同学选了课程一与二, 且选了B为同修, B同学选了课程二与三, 且选了A为同修. A与B会被绑定为一对, 且其同修自由度为1.

### 3.2.班级频数

统计每个课程被选次数, 此次数即为班级频数.

### 3.4.排课过程

1. 计算班级频数
2. 对所有同学按个人自由度与问卷填写时间由早到晚(自由度优先)从低到高为他们安排课程. 若某一同学有一个以上的候选课程,则优先分入频数低的班, 若频数相等,则随机分配.
3. 若排课结果极度不平衡, 如某些班人特少, 某些特多, 则尝试人工换课. 若经常有此情况发生后续版本会考虑加入此功能.

## 5.面向对象设计

程序结构设计

### 5.1.course类(course.py)

属性Property:

1. 课程名(name: name, type: str)
2. 难度(name: difficulty , type: int)
3. 学生(name: students, type: list)
4. 同修对(name: pairs, type: list)
5. 当前学生数量(name: current_num, type: int)
6. 最大学生数量(name: max_num: , type: int, None代表无限制)

方法method:

1. 添加学生(def add_student(student))
2. 添加同修对(def add_pair(pair))

### 5.2.pair类(pair.py)

属性Property:

1. 第一人名字(name: name1, type: str)
2. 第一人学号(name: id1, type: str)
3. 第二人名字(name: name2, type: str)
4. 第二人学号(name: id2, type: str)
5. 候选课程(name: candidate_class, type: list)
6. 填写时间(name: finish_time, type: str)
7. 自由度(name: DF, type: int)

### 5.3.student类(student.py)

属性Property:

1. 姓名(name: name, type: str)
2. 学号(name: id, type: str)
3. 候选课程(name: candidate_class, type: list)
4. 填写时间(name: finish_time, type: str)
5. 自由度(name: DF, type: int)

### 5.4.Functions(in class_arranger.py)

1. generate函数: 根据excel数据生成student object, pair object 和 class object

```python
generate(xlsx_path, time_column, name_column, id_column, pairName_column, pairID_column, class_column)

# return velue:
# student objects list
# pairs object list
# class object list

# sample:
students, pairs, classes = generate("../statistics/data/test0.xlsx", "B", "G", "I", "Q", "R", "K:P")
```

2. arrange函数: 使用student object list, pair object list 和 class object list排课

```python
arrange(students, pairs, classes)

# return velue:
# class object list

# sample:
x = arrange(students, pairs, classes)
```

3. to_txt函数: 将排课后的课程信息写入文本

4. find_object函数: 在对象列表中查找满足条件的对象并返回他们的序号