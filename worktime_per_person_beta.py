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
        if name_list.count(person_name) > 1:
            name_list.remove(person_name)
        for j, person_work_time in enumerate(chn_work_time_list):
            if i == j:
                person = Person(person_name, person_work_time)
                person_list.append(person)
                for k, person in enumerate(person_list):
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
    f = open("person_db.txt", "wt")
    for person in person_list:
        f.write(person.name + '\n')
        f.write(str(person.work_time) + '\n')
    f.close()


def run():
    work_time_list = []
    name_list = []
    person_list = []
    while 1:
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
        set_person(name_list, chn_work_time_list, person_list)
        print_person(person_list)
        store_contact(person_list)


if __name__ == '__main__':
    run()

    # 문제점 1
    # 현재 인원 추가에 따른 수직시간이 바뀔때마다 클래스가 계속 생성됨.--> 이전 클래스를 삭제할 필요 있음.
    # 이를 해결할 필요성 있음.
    # 해결법 1
    # 클래스 생성자 person = Person(person_name, person_work_time)에서 조건문을 통해 이미 클래스가 있을 경우 이전 클래스를
    # 삭제하고 없을 경우 pass한 후 클래스를 생성
    # 위 문제와 파일 불러오기만 입력하면 완성됨.
    # 2017.10.부터 개발 재개할 예정
    # 깃허브로 공유중
