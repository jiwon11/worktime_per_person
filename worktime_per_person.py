# worktime_per_person module
# 이 모듈에서 계산된 명당 수직시간과 랜덤추가수직시간배정을 계산함.
# 팀원들의 이해를 돕기 위해 한줄 단위로 주석을 달았습니다...
# 불편하시다면 죄송하고 보고 이해 안되신다면 말씀해주세요...
# 중간중간 약간 쓸데 없는 print문이 들어가 있는데 이는 안에 리스트의 내용이 변경 및 삭제되고 계산결과등을 수시로 보면서
# 좀 더 작동방식을 쉽게 이해시켜 드리고자 넣었습니다.
# 그리고 나중에 프론트엔드 파트에서 print문을 보면서 UI를 작성할 때 좀 더 쉬울 수도 있습니다.

import random


class Person:  # person클래스 생성
    def __init__(self, person_name, person_work_time):
        self.name = person_name
        self.work_time = person_work_time

    def print_info(self):  # 추후 객체들의 이름과 수직시간을 보여주기 위한 메소드
        print("이름 : ", self.name)
        print("수직시간 : ", self.work_time)


# 수직시간 계산의 경우 수직인원에 따라 수직시간에 변하기 때문에 이름과 수직시간을 동시에 입력하여 클래스를 생성할 수 없음.
# 따라서 이름 입력과 수직시간 계산을 다른 함수에서 정의한 후 매개변수로 받아 새로운 함수에서 클래스를 생성해야 함.

def set_person(name_list, chn_work_time_list, person_list):  # 다른 함수에서 정의된 이름과 수직시간을 통해 클래스를 생성하는 함수
    for i, person_name in enumerate(name_list):  # 이름의 리스트를 한 원소씩 받고(i는 리스트의 순서)
        for j, person_work_time in enumerate(chn_work_time_list):  # 수직시간의 리스트를 한 원소씩 받는다.(j는 리스트의 순서)
            if i == j:  # 이름 리스트의 원소와 수직시간 리스트의 원소의 순서가 같을 경우 (이름 수직시간을 매핑)
                person = Person(person_name, person_work_time)  # person클래스 생성
                person_list.append(person)  # 그후 모든 객체를 순회를 통해 person_list에 추가


def print_person(person_list):  # 수직인원의 이름과 수직시간을 보여주기 위한 함수
    try:
        for person in person_list:  # person_list를 순회하여 모든 객체의 print_info()메소드를 실행
            person.print_info()
    except AttributeError as err:  # 만약 person_list의 원소가 없을 경우 에러를 발생시킴.
        print("수직인원이 없습니다...")


def add_person():  # 수직인원을 추가하는 함수
    name = input("이름 : ")
    return name


def cal_ave_worktime(name_list):  # 평균 수직시간 계산 함수
    ave_worktime = int(50 / len(name_list))  # 평균 수직시간 계산식
    over_worktime = int(50 % len(name_list))  # 추가로 수직을 서야 하는 사람 수
    print("명당 평균 수직시간은 {0}시간입니다.".format(ave_worktime))
    print("남은 수직시간은 {0}시간입니다.".format(over_worktime))
    return ave_worktime  # 랜덤 추가수직시간 배정을 위한 함수를 위해 평균 수직시간 결과를 반환함.


def cal_over_worktime(name_list, ave_work_time_list):  # 랜덤 추가수직시간 배정 함수
    over_worktime = int(50 % len(name_list))

    def rand_str(name_list, over_worktime):  # 전체 이름 중에서 추가로 수직을 서야 하는 사람 수만큼을 랜덤으로 반환하는 함수
        return random.sample(name_list, over_worktime)

    over_worker = rand_str(name_list, over_worktime)  # 추가 수직배정자
    for i, name_name in enumerate(name_list):  # 전체 이름리스트를 순회하고
        for j, overwoker_name in enumerate(over_worker):  # 추가 수직배정자를 순회하여
            if name_name == overwoker_name:  # 전체 이름리스트 중에서 추가 수직배정자를 찾으면
                print(name_name, "==", overwoker_name)
                turn = name_list.index(overwoker_name)  # 추가 수직 배정자의 이름 리스트내 순서를 받아
                new_work_time = ave_work_time_list[turn] + 1  # 추가 수직 배정자의 이름 순서에 맞는 수직시간에 1을 더해줌.
                ave_work_time_list[turn] = new_work_time  # 더한 수직시간을 다시 수직시간 리스트 원소에 수정
    return ave_work_time_list  # 바뀐 수직시간 리스트를 반환


def store_contact(person_list):  # 저장된 person 객체를 텍스트 파일에 저장
    f = open("person_db.txt", "wt", encoding='utf8')
    for person in person_list:  # 모든 person리스트를 순회하여
        f.write(person.name + '\n')  # person.name을 입력하고
        f.write(str(person.work_time) + '\n')  # person.work_time을 입력하고
    f.close()  # 파일 닫음.


def load_person_db(person_list, work_time_list, name_list):  # 텍스트파일로 저장된 person 객체를 불러오는 함수
    f = open("person_db.txt", "rt")
    lines = f.readlines()  # 파일을 줄단위로 읽은 후
    num = len(lines) / 2  # 2줄 단위로 되어있는 이름과 수직시간을 하나로 분류
    num = int(num)

    for i in range(num):  # 순회하며 분류되어 있는 객체에 맞는 이름을 지정
        person_name = lines[2 * i].rstrip('\n')  # 첫줄은 객체 이름
        person_work_time = lines[2 * i + 1].rstrip('\n')  # 둘째줄은 객체 수직시간
        name_list.append(person_name)  # 새로 계산되는 수직시간에 업무자의 수가 바뀌어야 되므로 이름 리스트에 추가
        work_time_list.append(person_work_time)  # 새로 계산되는 수직시간에 수직시간이 수정되야 하므로 추가
        person = Person(person_name, person_work_time)  # 줄 단위로 읽은 객체 이름과 수직시간을 맵핑
        person_list.append(person)  # 업무자 리스트에 모든 객체 추가
    f.close()


def run():
    work_time_list = []
    name_list = []
    person_list = []
    load_person_db(person_list, work_time_list, name_list)  # 텍스트파일로 저장된 person 객체를 불러오기
    while 1:  # 무한루프
        print_person(person_list)
        print("--------------------------------------------------")
        name = add_person()
        name_list.append(name)
        print("수직인원 : ", name_list)
        ave_worktime = cal_ave_worktime(name_list)
        work_time_list.clear()
        work_time_list.append(ave_worktime)
        ave_work_time_list = work_time_list * len(name_list)
        # 평균 수직시간은 리스트에 한개의 원소로 밖에 저장이 안되므로 이름 수 만큼 복사하여 저장해야 함.
        print(ave_work_time_list)
        chn_work_time_list = cal_over_worktime(name_list, ave_work_time_list)
        print(chn_work_time_list)  # 추가 수직시간으로 수정된 수직시간 리스트
        person_list.clear()
        # 기존에 있던 person객체는 수정 전의 수직시간을 가지고 있으므로 모두 삭제하여야 함.
        set_person(name_list, chn_work_time_list, person_list)
        print(name_list)
        print(chn_work_time_list)
        print_person(person_list)
        if input("텍스트 파일로 저장하시겠습니까? ") == '네' or 'yes':  # 'yes'혹은 '네' 라고 입력할 경우 텍스트 파일로 저장
            store_contact(person_list)
        else:  # 그 외에는 넘어가 처음으로 돌아감.
            pass
        print("--------------------------------------------------")


if __name__ == '__main__':
    run()

    # 완성
    # 깃허브로 공유중
