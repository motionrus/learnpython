#!/usr/bin/python3
def compare_line(first, second):
    if type(first) != str or first == "":
        return "first is incorrect"
    if type(second) != str or second == "":
        return "second is incorrect"
    if first == second:
        return 1
    if second == "learn":
        return 3
    if len(first) > len(second):
        return 2

print(compare_line("example", "learn"))