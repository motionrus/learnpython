#!/usr/bin/python3
answeres = {
    "привет": "привет",
    "что нового": "ничего",
    "что старого": "спроси еще что нибудь"
}
#task2
names = ["Вася", "Маша", "Петя", "Валера", "Саша", "Даша"]
def find_person(name):
    while True:
        if names[-1] == name:
            break
        if len(names) == 1:
            return "{} не нашелся".format(name)
        names.pop()
    return "{} нашелся".format(name)

print (find_person("Петя"))

#task4
def get_answer(key, answeres):
    return answeres.get(key)

#task3
def ask_user(name = ""):
    while True:
        try:
            key = input("Спроси что-нибудь: ")
            if key == "Пока!":
                break
            answer = get_answer(key, answeres)
            print(answer)
        except KeyboardInterrupt:
            print("Вы нажали Ctrl + C программа будет завершена, всего доброго")
            break
ask_user()