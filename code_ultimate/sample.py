from class_arranger import generate,arrange,to_txt

# check name, name must be unique
students, pairs, classes = generate("../statistics/data/test0.xlsx", "B", "G", "I", "Q", "R", "K:P")

x = arrange(students, pairs, classes)

with open('result.txt', 'w') as f:
    f.write(to_txt(x))