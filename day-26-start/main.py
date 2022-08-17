# #For Loop

# numbers = [1, 2, 3]
# new_list = []
# for n in numbers:
#     add_1 = n + 1
#     new_list.append(add_1)

# #List Comprehension
# new_list = [n + 1 for n in numbers]

# #String as List
# name = "Angela"
# letters_list = [letter for letter in name]

# #Range as List
# range_list = [n * 2 for n in range(1, 5)]

# #Conditional List Comprehension
names = ["Alex", "Beth", "Caroline", "Dave", "Elanor", "Freddie"]
import random
student_scores = {name: random.randint(1,100) for name in names}

passed_students = {name:score for name,score in student_scores.items() if score > 70}
print(passed_students)



# upper_case_names = [name.upper() for name in names if len(name) > 4]



