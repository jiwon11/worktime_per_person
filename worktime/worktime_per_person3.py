import random


class Person:
    def __init__(self, person_name, person_work_time):
        self.name = person_name
        self.work_time = person_work_time

    def print_info(self):
        print("이름 : ",self.name)
        print("수직시간 : ",self.work_time)


def add_person():
    name = input("이름 : ")
    return name


def cal_ave_worktime(name_list):
    ave_worktime = int(50 / len(name_list))
    over_worktime = int(50 % len(name_list))
    print("명당 평균 수직시간은 {0}시간입니다.".format(ave_worktime))
    print("남은 수직시간은 {0}시간입니다.".format(over_worktime))
    return ave_worktime

def cal_over_worktime(name_list, worktime_list):
    over_worktime = int(50 % len(name_list))

    def rand_str(name_list, over_worktime):
        return random.sample(name_list, over_worktime)

    over_worker = rand_str(name_list, over_worktime)
    print(over_worker)
    for i, name_name in enumerate(name_list):
        for j, overwoker_name in enumerate(over_worker):
            if name_name == overwoker_name:
                print(name_name, "==", overwoker_name)
                turn = name_list.index(overwoker_name)
                NV = worktime_list[turn] + 1
                worktime_list[turn] = NV
                print(worktime_list)

def print_person(person_list):
    for person in person_list:
        person.print_info()


def print_menu():
    print("1. 인원 추가")
    print("2. 인원 검색")
    print("3. 명당 평균수직시간 계산")
    print("4. 명당 수직시간 저장")
    print("5. 종료")
    menu = input("메뉴선택: ")
    return int(menu)


def set_person(name, work_time):
    person_name = name
    person_work_time = work_time
    person = Person(person_name, person_work_time)
    return person


def run():
    person_list = []
    name_list = []
    work_time_list = []
    while 1:
        name = add_person()
        name_list.append(name)
        print("수직인원 : ", name_list)
        ave_worktime = cal_ave_worktime(name_list)
        work_time_list.clear()
        work_time_list.append(ave_worktime)
        chn_work_time_list = work_time_list * len(name_list)
        print(chn_work_time_list)
        cal_over_worktime(name_list, chn_work_time_list)


if __name__ == "__main__":
    run()
