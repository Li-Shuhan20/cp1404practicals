def question_1():
    file = open("name.txt", "w")
    name = input("Name: ")
    print(name, file=file)
    file.close()


def question_2():
    file = open("name.txt", "r")
    name = file.read().strip()
    print(f"Hi {name}!")
    file.close()


def question_3():
    total = 0
    with open("numbers.txt", "r") as file:
        for i in range(0, 2):
            number = file.readline()
            total += int(number)
        print(total)
    file.close()


def question_4():
    total = 0
    with open("numbers.txt", "r") as file:
        lines = file.readlines()
        for line in lines:
            number = int(line.strip())
            total += number
    print(total)
    file.close()


question_1()
question_2()
question_3()
question_4()
