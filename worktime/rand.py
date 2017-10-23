import random
name_list = []
work_time_list = []
person_list = []
class Person:
    def __init__(self, person_name, person_work_time):
        self.name = person_name
        self.work_time = person_work_time

    def print_info(self):
        print("이름 : ",self.name)
        print("수직시간 : ",self.work_time)

def set_person(name_list,chn_work_time_list):
    for i,person_name in enumerate(name_list):
        if name_list.count(person_name) > 1:
            name_list.remove(person_name)
        for j,person_work_time in enumerate(chn_work_time_list):
            if i == j:
                person = Person(person_name,person_work_time)
                person_list.append(person)
                for k,person in enumerate(person_list):
                    if person_list.count(person.name) > 1:
                        del person_list[k]

def print_person(person_list):
    for person in person_list:
        person.print_info()

def add_person():
    name = input("이름 : ")
    return name

def cal_ave_worktime(name_list):
    ave_worktime = int(50 / len(name_list))
    over_worktime = int(50 % len(name_list))
    return ave_worktime

def cal_over_worktime(name_list, ave_work_time_list):
    over_worktime = int(50 % len(name_list))

    def rand_str(name_list, over_worktime):
        return random.sample(name_list, over_worktime)

    over_worker = rand_str(name_list, over_worktime)
    for i, name_name in enumerate(name_list):
        for j, overwoker_name in enumerate(over_worker):
            if name_name == overwoker_name:
                print(name_name, "==", overwoker_name)
                turn = name_list.index(overwoker_name)
                new_work_time = ave_work_time_list[turn] + 1
                ave_work_time_list[turn] = new_work_time
    return ave_work_time_list

while 1:
    name = add_person()
    name_list.append(name)
    ave_worktime = cal_ave_worktime(name_list)
    work_time_list.clear()
    work_time_list.append(ave_worktime)
    ave_work_time_list = work_time_list*len(name_list)
    print(name_list)
    print(ave_work_time_list)
    chn_work_time_list = cal_over_worktime(name_list, ave_work_time_list)
    set_person(name_list,chn_work_time_list)
    print_person(person_list)
