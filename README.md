# Nanhaiqinyin Qin club course arranger

automatically arrange course base on the questionnaire

## Questionnaire format

Questionnaire must contain name, ID, candidate courses, pair name and pair id.

Candidate courses should satisfy the students capacity, I use number of songs learnt of students as the measurement of capacity, the rule can be change later.

The sample questionnaire:

![qrcode](C:\Users\Kylis\Desktop\NanHaiQingYin_qin_club\statistics\img\qrcode.jpg)

## Usage

There are two main function in course_arranger.py,namely, generate and arrange. Generate function use the excel file base on the questionnaire to generate students object list, pairs object list and the classes object list(before arrange). Arrange function use the three list before to generate the final classes object list(after arrange). At last, I use to_txt function to show the result.

You can clone the repository, check and run  the sample.py in ultimate_code folder. The excel data used in the sample is in ./statistics/data/test0.xlsx