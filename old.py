#!/usr/bin/python3
try:
    old = int(input("Введите свой возвраст: "))
except:
    print("Вы ввели что-то другое")
    exit(0)
if 0 <= old <= 6: 
    print("Ты должен учиться в детском саду")
if 7 <= old <= 17:
    print("Ты должен учиться в школе")
if 18 <= old <= 23:
    print("Ты должен учиться в ВУЗе")
elif old > 23:
    print("Ты должен работать")