from class_arranger import generate,arrange,to_txt

# check name, name must be unique
students, pairs, classes = generate("../statistics/data/150506315_0_壬寅年春季社团选课_58_58.xlsx", "B", "G", "I", "M", "N", "K:L")

x = arrange(students, pairs, classes)

with open('result.txt', 'w') as f:
    f.write(to_txt(x))