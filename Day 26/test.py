"""
numbers = [1, 2, 3]
name = "Suresh"
print(list(name))
increased = [chr(ord(x) + 1) for x in name]
print(increased)
lyst = [x * 2 for x in range(1, 5)]
print(lyst)
names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
short_names = [name if len(name) <= 4 else "Robert" for name in names]
print(short_names)
long_names = [name.upper() for name in names if len(name) >= 5]
print(long_names)
"""

"""
import random
names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
student_scores = {name : random.randint(0, 100) for name in names}
print(student_scores)
# passed_students = [name for name in student_scores.keys() if student_scores[name] >= 60]
passed_students = {name : score for name, score in student_scores.items() if score >= 60}
print(passed_students)
"""
import pandas

student_dict = {
    "student" : ["Angela", "James", "Lily"],
    "score" : [56, 76, 98]
}

df = pandas.DataFrame(student_dict)
"""
for key, value in df.items():
    print(value)
"""
for index, row in df.iterrows():
    print(row["student"])