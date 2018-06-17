# worktime_per_person module
# 이 모듈에서 계산된 명당 수직시간과 랜덤추가수직시간배정을 계산함.
# 팀원들의 이해를 돕기 위해 한줄 단위로 주석을 달았습니다...
# 불편하시다면 죄송하고 보고 이해 안되신다면 말씀해주세요...
# 중간중간 약간 쓸데 없는 print문이 들어가 있는데 이는 안에 리스트의 내용이 변경 및 삭제되고 계산결과등을 수시로 보면서
# 좀 더 작동방식을 쉽게 이해시켜 드리고자 넣었습니다.
# 그리고 나중에 프론트엔드 파트에서 print문을 보면서 UI를 작성할 때 좀 더 쉬울 수도 있습니다.

class Person:  # person클래스 생성
    def __init__(self, person_name,person_part,person_work_time,person_wish_worktime):
        self.name = person_name
        self.part = person_part
        self.work_time = int(person_work_time)
        self.wish_worktime = int(person_wish_worktime)
        super(Person,self).__init__()

    def print_info(self):  # 추후 객체들의 이름과 수직시간을 보여주기 위한 메소드
        print("       이름 : ", self.name)
        print("       직무 : ",self.part)
        print("       수직시간 : ", self.work_time)
        print("       희망 근로 시간 : ",self.wish_worktime)

# 수직시간 계산의 경우 수직인원에 따라 수직시간에 변하기 때문에 이름과 수직시간을 동시에 입력하여 클래스를 생성할 수 없음.
# 따라서 이름 입력과 수직시간 계산을 다른 함수에서 정의한 후 매개변수로 받아 새로운 함수에서 클래스를 생성해야 함.

def set_person(name_list,person_list,part_list,ave_worktime,wish_worktime_list):  # 다른 함수에서 정의된 이름과 수직시간을 통해 클래스를 생성하는 함수
    for i in range(len(name_list)):  # 이름의 리스트를 한 원소씩 받고(i는 리스트의 순서)
        person_name = name_list[i]
        person_part = part_list[i]
        person_wish_worktime = wish_worktime_list[i]
        if person_part in ave_worktime.keys():
            person_work_time = ave_worktime[person_part]
            person = Person(person_name,person_part,person_work_time,person_wish_worktime)  # person클래스 생성
            person_list.append(person)  # 그후 모든 객체를 순회를 통해 person_list에 추가

def print_person(person_list):  # 수직인원의 이름과 수직시간을 보여주기 위한 함수
    print('-' * 10, '근로자 명단', '-' * 10)
    try:
        for person in person_list:  # person_list를 순회하여 모든 객체의 print_info()메소드를 실행
            person.print_info()
            print('\n')
    except AttributeError as err:  # 만약 person_list의 원소가 없을 경우 에러를 발생시킴.
        print("수직인원이 없습니다...")


def add_person():  # 수직인원을 추가하는 함수
    name = input("이름 : ")
    return name

def add_part():
    part = input("직무 : ")
    return part

def add_wish_worktime():
    wish_worktime = int(input("희망 근로 시간 : "))
    return wish_worktime

def cal_ave_worktime(name_list, part_list, part_time_dic):  # 평균 수직시간 계산 함수
    name_part_list = list(zip(name_list,part_list))
    person_count_part = {}
    for i in part_time_dic.keys():
        count = 0
        for j in range(len(name_part_list)):
            if name_part_list[j][1] == i:
                count += 1
        person_count_part[i]=count
    print('직무 당 사람 수 :',person_count_part)

    part_time = list(part_time_dic.values())
    part_name = list(part_time_dic.keys())
    count_person_part = list(person_count_part.values())
    per_part_time_ave = {}
    per_part_time_ove = {}
    for i in range(len(part_time)):
        try:
            ave_worktime = int(int(part_time[i])/int(count_person_part[i]))  # 평균 수직시간 계산식
            over_worktime = int(int(part_time[i])%int(count_person_part[i]))
            per_part_time_ave[part_name[i]] = ave_worktime
            per_part_time_ove[part_name[i]] = over_worktime
        except ZeroDivisionError:
            print("{0} 직무에는 아직 수직인원이 없습니다.".format(part_name[i]))
            pass
    print("직무별 명당 평균 수직시간은 {0}입니다.".format(per_part_time_ave))
    print("직무별 남은 수직시간은 {0}입니다.".format(per_part_time_ove))
    return per_part_time_ave,per_part_time_ove  # 랜덤 추가수직시간 배정을 위한 함수를 위해 평균 수직시간 결과를 반환함.


def set_part(name_list,replace_part,part_list):
    print('직무는 다음과 같습니다.',replace_part)
    part_time = input("각각의 직무에 할당할 시간을 입력하세요 : ")
    part_time_dic = {}
    for i in range(len(replace_part)):
        for i in range(len(replace_part)):
            part_time_dic[replace_part[i]] = part_time
    print(part_time_dic)
    return part_time_dic

def cal_over_worktime(person_list,ove_worktime,part_list,ave_worktime):  # 추가수직시간 배정 함수
    for person in person_list:
        if ove_worktime[person.part] == 0:
            continue
        if person.wish_worktime > person.work_time:
            person.work_time += 1
            print(person.part,'직무인',person.name, "의 수직시간이",ave_worktime[person.part],'에서',person.work_time,"으로 1시간 변경되었습니다.")
            ove_worktime[person.part] -= 1
    print(ove_worktime)
    for i in person_list:
        print(i.name)

def store_contact(person_list):  # 저장된 person 객체를 텍스트 파일에 저장
    f = open("person_db.txt", "wt", encoding='utf8')
    for person in person_list:  # 모든 person리스트를 순회하여
        f.write(person.name + '\n')  # person.name을 입력하고
        f.write(str(person.work_time) + '\n')  # person.work_time을 입력하고
        f.write(person.part + '\n')
        f.write(str(person.wish_worktime) + '\n')
        print(person.name, "을 저장했습니다.")
    f.close()# 파일 닫음.


def load_person_db(person_list, work_time_list, name_list,part_list,wish_worktime_list):  # 텍스트파일로 저장된 person 객체를 불러오는 함수
    f = open("person_db.txt", "rt")
    lines = f.readlines()  # 파일을 줄단위로 읽은 후
    num = len(lines) / 4  # 3줄 단위로 되어있는 이름과 수직시간을 하나로 분류
    num = int(num)

    for i in range(num):  # 순회하며 분류되어 있는 객체에 맞는 이름을 지정
        person_name = lines[4 * i].rstrip('\n')  # 첫줄은 객체 이름
        person_part = lines[4 * i + 1].rstrip('\n')  # 둘째줄은 객체 수직시간
        person_work_time = lines[4 * i +2].rstrip('\n')
        person_wish_worktime = lines[4 * i + 3].rstrip('\n')
        name_list.append(person_name)  # 새로 계산되는 수직시간에 업무자의 수가 바뀌어야 되므로 이름 리스트에 추가
        work_time_list.append(person_work_time)  # 새로 계산되는 수직시간에 수직시간이 수정되야 하므로 추가
        part_list.append(person_part)
        wish_worktime_list.append(person_wish_worktime)
        person = Person(person_name,person_part,person_work_time,person_wish_worktime)  # 줄 단위로 읽은 객체 이름과 수직시간을 맵핑
        person_list.append(person)  # 업무자 리스트에 모든 객체 추가
    f.close()


def run():
    work_time_list = []
    name_list = []
    person_list = []
    part_list = []
    wish_worktime_list = []
    load_person_db(person_list, work_time_list, name_list,part_list,wish_worktime_list)# 텍스트파일로 저장된 person 객체를 불러오기
    print_person(person_list)
    input_part = input("직무를 입력하세요 : ")
    replace_part = input_part.split(' ')
    print(replace_part)
    part_time_dic = set_part(name_list, replace_part, part_list)
    while 1:  # 무한루프
        print("--------------------------------------------------")
        name = add_person()
        name_list.append(name)
        part = add_part()
        if part not in replace_part:
            print("입력한 직무는 없습니다.")
            break
        part_list.append(part)
        wish_worktime = add_wish_worktime()
        wish_worktime_list.append(wish_worktime)
        print("수직인원 : ", name_list,"수직인원은 {0}명입니다.".format(len(name_list)))
        ave_worktime,ove_worktime = cal_ave_worktime(name_list,part_list,part_time_dic)
        person_list.clear()
        set_person(name_list, person_list, part_list, ave_worktime, wish_worktime_list)
        cal_over_worktime(person_list, ove_worktime, part_list, ave_worktime)
        print_person(person_list)
        if input("텍스트 파일로 저장하시겠습니까? ") == '네' or 'yes':  # 'yes'혹은 '네' 라고 입력할 경우 텍스트 파일로 저장
            store_contact(person_list)
        else:  # 그 외에는 넘어가 처음으로 돌아감.
            pass
        print("--------------------------------------------------")

if __name__ == '__main__':
    run()