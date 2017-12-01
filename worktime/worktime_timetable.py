# worktime_timetable 모듈
# 명당 수직시간을 바탕으로 수직 가능 시간표에 사람을 배정하는 모듈
# 2차원 배열을 사용
# 사는용자 별 가능 공강시간을 1, 불가능 시간을 0
# 모든 원소는 0으로 시작해서 명당 수직시간을 -1씩 분배
# 사용자의 가능 시간을 현재 모듈로서 알 수 없기 때문에 수작업으로 할 예정
# 예) 공강이 언제입니까? 월4 입력 시, 1*4번째 배열을 1로 지정
# 그후 basic_time_table은 전부 0으로 설정 후 시간별 basic_time_table의 시간==사용자의 시간을
# 통해 다르면 해당 시간 칸에 사용자 이름을 입력
import worktime_per_person
import pprint
import pickle


class User():
	def __init__(self, user_name, user_timetable):
		self.name = user_name
		self.timetable = user_timetable

	def print_timetable(self):
		print("    {0}의 수직 가능 시간표".format(self.name))
		pprint.pprint(self.timetable)

class OverWorkerError(Exception):
    def __init__(self):
        super().__init__("시간당 수직자가 초과하였습니다.")

basic_timetable = [[0] * 5 for z in range(10)]

def set_timetable(name_list,user_name,work_time_list):
	user_timetable = [[0] * 5 for x in range(10)]
	turn = name_list.index(user_name)
	count = int(work_time_list[turn])
	print("공강 시간을 {0}회 입력하세요.".format(count))
	i = 1
	while (i <= count):
		day = input("요일을 입력하세요(월~금) : ")
		period = int(input("교시를 입력하세요(1~10) : ")) - 1
		if (day == "월"):
			user_timetable[period][0] = 1
		elif (day == "화"):
			user_timetable[period][1] = 1
		elif (day == "수"):
			user_timetable[period][2] = 1
		elif (day == "목"):
			user_timetable[period][3] = 1
		elif (day == "금"):
			user_timetable[period][4] = 1
		print("{0}번 남았습니다.".format(count - i))
		i = i + 1
	return user_timetable

def set_user_name(name_list):
	user_name = input("이름을 입력하세요: ")
	for i, name in enumerate(name_list):
		if (user_name == name):
			print("start")
			return user_name

def store_user(user_list):
	f = open("user_db.txt", "wt")
	for user in user_list:
		f.write(user.name + '\n')
		f.write(str(user.timetable) + '\n')
	f.close()


def set_name_table(user, basic_timetable, name_table,sat_user_name_list,copy_sat,user_list):
	#print("copy_sat : ",copy_sat)
	# 리스트에 추가는 밖에서 하고 if문을 통해 관계가 없는 것을 remove한다.
	i=0
	while i<10:
		j = 0
		while j<5:
			if user.timetable[i][j] == 1:
				if name_table[i][j] == "NONE":
					name_table[i][j]=[user.name]
				else:
					if len(name_table[i][j])==2:
						if j==0:day="월"
						elif j == 1: day = "화"
						elif j == 2: day = "수"
						elif j == 3: day = "목"
						elif j == 4:day = "금"
						print(day+"요일",str((i+1))+"교시","시간의 시간당 수직자가 초과하였습니다.")
						print("다른 공강 시간을 입력해주세요.")
						return name_table
					else:
						name_table[i][j].append(user.name)
					if name_table[i][j].count(user.name)>1:
						try:name_table[i][j].remove(user.name)
						except ValueError:pass
			else:
				if name_table[i][j] != "NONE":
					try:
						name_table[i][j].remove(user.name)
					except ValueError:
						pass
			j=j+1
		i=i+1
	return name_table

def print_user(user_list,user_name):
	for i, user in enumerate(user_list):
		if user.name==user_name:
			user.print_timetable()

def store_name_table(chn_name_table):
    f = open("name_table_db.txt", "wb", encoding='utf8')
    pickle.dump(chn_name_table,f)
    f.close()

def load_user_db(user_list, user_name_list):  # 텍스트파일로 저장된 person 객체를 불러오는 함수
    f = open("user_db.txt", "r")
    lines = f.readlines()  # 파일을 줄단위로 읽은 후
    num = len(lines) / 2  # 2줄 단위로 되어있는 이름과 수직시간을 하나로 분류
    num = int(num)

    for i in range(num):  # 순회하며 분류되어 있는 객체에 맞는 이름을 지정
        user_name = lines[2 * i].rstrip('\n')  # 첫줄은 객체 이름
        user_timetable = lines[2 * i + 1].rstrip('\n')  # 둘째줄은 객체 수직시간
        name_list.append(user_name)  # 새로 계산되는 수직시간에 업무자의 수가 바뀌어야 되므로 이름 리스트에 추가
        user = User(user_name, user_timetable)  # 줄 단위로 읽은 객체 이름과 수직시간을 맵핑
        user_list.append(user)  # 업무자 리스트에 모든 객체 추가
    f.close()

def load_name_table_db(name_table):  # 텍스트파일로 저장된 person 객체를 불러오는 함수
    try:
        f = open("name_table_db.txt", "rb")
        name_table = pickle.load(f)
        f.close()
    except EOFError:
	    pass

def delete_user(user_list, name): #이 함수는 연락처 리스트와 삭제할 이름을 인자로 입력받음.
    for i, user in enumerate(user_list): #i번 순회하여
        if user.name == name: #만약 i번째 인스턴스의 이름과 입력받은 이름이 같을 경우
            del user_list[i]

def print_menu():
    print("1. 수직시간표 계산")
    print("2. 사람 삭제")
    print("3. 연락처 저장")
    print("4. 종료")
    menu = input("메뉴선택: ")
    return int(menu)

def run():
	user_list = []
	name_table = [["NONE"] * 5 for h in range(10)]
	sat_user_name_list=[]
	copy_sat = sat_user_name_list.copy()
	#load_name_table_db(name_table)
	#load_user_db(user_list,user_name_list)
	while True:  # 무한루프
		menu = print_menu()
		if menu == 1:
			user_name=set_user_name(name_list)
			user_timetable = set_timetable(name_list, user_name, work_time_list)
			user = User(user_name, user_timetable)
			user.print_timetable()
			user_list.append(user)
			sat_user_name_list.append(user.name)
			chn_name_table=set_name_table(user, basic_timetable, name_table,sat_user_name_list,copy_sat,user_list)
			name_table=chn_name_table
			print("-----수직시간표-----")
			pprint.pprint(name_table)
		elif menu == 2:
			name=input("삭제할 이름 : ")
			delete_user(user_list,name)
			i = 0
			while i < 10:
				j = 0
				while j < 5:
					try:
						if name in name_table[i][j]:
							name_table[i][j].remove(name)
							if name_table[i][j]==[]:
								name_table[i][j]="NONE"
					except TypeError:
						pass
					j=j+1
				i=i+1
			print("-----수직시간표-----")
			pprint.pprint(name_table)
		elif menu == 3:
			pass
		elif menu == 4:
			break
		#if input("텍스트 파일로 저장하시겠습니까? ") == '네' or 'yes':  # 'yes'혹은 '네' 라고 입력할 경우 텍스트 파일로 저장
			#store_user(user_list)
			#store_name_table(chn_name_table)
		#else:  # 그 외에는 넘어가 처음으로 돌아감.
			#pass


print("==================================================================")
work_time_list = []
name_list = []
person_list = []
worktime_per_person.load_person_db(person_list, work_time_list, name_list)
worktime_per_person.print_person(person_list)
print("==================================================================")
run()

'''
사용자 삭제 메뉴 추가
그럴 경우 수직시간표에서도 사용자의 이름을 삭제하여야 함.
'''