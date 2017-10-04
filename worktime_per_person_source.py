import random


class Person:
    def __init__(self, name, worktime):
        self.name = name
        self.worktime = worktime

    def print_info(self):
        print("이름 : ", self.name)
        print("수직시간 :  ", self.worktime)

def add_person(person_list):
    name = input("이름 : ")
    person_list.append(name)
    return name

def count_person(person_list):
    num = len(person_list)
    print("수직인원은 {0}명 입니다.", format(num))


def set_person():
    name = input("이름 : ")
    person = Person(name)
    return person

def cal_worktime(person_list):
    ave_worktime = int(50 / len(person_list))
    over_worker = int(50 % len(person_list))
    rdm_over_woker = random.sample(person_list, over_worker)
    for i, name in enumerate(person_list):
        if rdm_over_woker == name.name:
            over_worktime = ave_worktime + 1
            return over_worktime
        else:
            return ave_worktime


def store_contact(person_list):
    f = open("person_db.txt", "wt")
    for person in person_list:
        f.write(person.name + '\n')
        f.write(person.worktime + '\n')
    f.close()

def load_contact(person_list):
    f = open("person_db.txt", "rt")
    lines = f.readlines()
    num = len(lines) / 2
    num = int(num)

    for i in range(num):
        name = lines[2*i].rstrip('\n')
        worktime = lines[2*i+1].rstrip('\n')
        person = Person(name, worktime)
        person_list.append(person)
    f.close()

def print_menu():
    print("1. 인원 추가")
    print("2. 인원 검색")
    print("3. 명당 수직시간 계산")
    print("4. 명당 수직시간 저장")
    print("5. 종료")
    menu = input("메뉴선택: ")
    return int(menu)

def run():
    person_list = []
    name = add_person(person_list)
    worktime = cal_worktime(person_list)
    person = Person(name,worktime)