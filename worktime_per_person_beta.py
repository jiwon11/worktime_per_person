import random


class Person:
    def __init__(self, person_name, person_work_time):
        self.name = person_name
        self.work_time = person_work_time

    def print_info(self):
        print("이름 : ", self.name)
        print("수직시간 : ", self.work_time)


def set_person(name_list, chn_work_time_list, person_list):
    for i, person_name in enumerate(name_list):
        for j, person_work_time in enumerate(chn_work_time_list):
            if i == j:
                person = Person(person_name, person_work_time)
                person_list.append(person)

def print_person(person_list):
    try:
        for person in person_list:
            person.print_info()
    except AttributeError as err:
        print("수직인원 객체가 없습니다...")


def add_person():
    name = input("이름 : ")
    return name


def cal_ave_worktime(name_list):
    ave_worktime = int(50 / len(name_list))
    over_worktime = int(50 % len(name_list))
    print("명당 평균 수직시간은 {0}시간입니다.".format(ave_worktime))
    print("남은 수직시간은 {0}시간입니다.".format(over_worktime))
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


def store_contact(person_list):
    f = open("person_db.txt", "wt",encoding='utf8')
    for person in person_list:
        f.write(person.name + '\n')
        f.write(str(person.work_time) + '\n')
    f.close()

def load_person_db(person_list, work_time_list, name_list):
    f = open("person_db.txt", "rt")
    lines = f.readlines()
    num = len(lines) / 2
    num = int(num)

    for i in range(num):
        person_name = lines[2*i].rstrip('\n')
        person_work_time = lines[2*i+1].rstrip('\n')
        name_list.append(person_name)
        work_time_list.append(person_work_time)
        person = Person(person_name, person_work_time)
        person_list.append(person)
    f.close()

def run():
    work_time_list = []
    name_list = []
    person_list = []
    load_person_db(person_list, work_time_list, name_list)
    while 1:
        print(name_list)
        print(work_time_list)
        name = add_person()
        name_list.append(name)
        print("수직인원 : ", name_list)
        ave_worktime = cal_ave_worktime(name_list)
        work_time_list.clear()
        work_time_list.append(ave_worktime)
        ave_work_time_list = work_time_list * len(name_list)
        print(ave_work_time_list)
        chn_work_time_list = cal_over_worktime(name_list, ave_work_time_list)
        print(chn_work_time_list)
        person_list.clear()
        set_person(name_list, chn_work_time_list, person_list)
        print(name_list)
        print(chn_work_time_list)
        print_person(person_list)
        if input("DB에 저장하시겠습니까? ") == '네' or 'yes':
            store_contact(person_list)
        else:
            pass
        print("--------------------------------------------------")


if __name__ == '__main__':
    run()

    # 완성
    # 깃허브로 공유중
