#!/usr/bin/python3
print("task 1")
list_lines = [x for x in range(10)]
for list_line in list_lines:
    print(list_line)

print("task 2")
strings = input("Введите строку: ")
for string in strings:
    print(string)

print("task 3")
school_lists = [{'school_class': '4a', 'scores': [3,4,4,5,2]}, 
        {'school_class': '5a', 'scores': [3,4,3,5,2]},
        {'school_class': '6a', 'scores': [3,5,4,5,2]},
        {'school_class': '7a', 'scores': [3,4,4,2,2]},
        {'school_class': '8a', 'scores': [3,3,4,5,2]},
        {'school_class': '9a', 'scores': [3,5,4,5,2]}]
middle_lists = []
for school_list in school_lists:
    middle = sum(school_list['scores'])/len(school_list['scores'])
    print("average in class {}: {}".format(school_list["school_class"], middle))
    middle_lists.append(middle)
middle_school = sum(middle_lists)/len(middle_lists)
print("middle for school: {}".format(middle_school))