import Worktime_Per_Person
import pprint
import pickle
import pandas as pd

time = ['am9~am10','am10~am11','am11~pm12','pm12~pm1','pm1~pm2','pm2~pm3','pm3~pm4','pm4~pm5','pm5~pm6','pm6~pm7','pm7~pm8','pm8~pm9']
days = ['   Mon   ','   Tus   ','   Wed   ','   Thu   ','   Fri   ']

class User(worktime_per_person.Person):
	def __init__(self,user_name,user_part,user_work_time,user_wish_worktime,user_timetable):
		super().__init__(user_name,user_part,user_work_time,user_wish_worktime)
		self.timetable = user_timetable

	def print_timetable(self):
		print("    {0}의 수직 가능 시간표".format(self.name))
		print(pd.DataFrame(self.timetable,index=time,columns=days))

class OverWorkerError(Exception):
    def __init__(self):
        super().__init__("시간당 수직자가 초과하였습니다.")

basic_timetable = [[0] * 5 for z in range(12)]

def set_timetable(name_list,user_name,work_time_list):
	user_timetable = [[0] * 5 for x in range(12)]
	turn = name_list.index(user_name)
	count = int(work_time_list[turn])
	print("공강 시간을 {0}회 입력하세요.".format(count))
	i = 1
	while (i <= count):
		day = input("요일을 입력하세요(월~금) : ")
		period = int(input("교시를 입력하세요(1~12) : ")) - 1
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
		f.write(user.part + '\n')
		f.write(str(user.work_time) + '\n')
		f.write(str(user.wish_worktime) + '\n')
		print(user.name,"의 정보가 저장되었습니다.")
	f.close()


def set_name_table(user, basic_timetable, name_table,sat_user_name_list,copy_sat,user_list):
	#print("copy_sat : ",copy_sat)
	# 리스트에 추가는 밖에서 하고 if문을 통해 관계가 없는 것을 remove한다.
	i=0
	while i<12:
		j = 0
		while j<5:
			if user.timetable[i][j] == 1:
				if name_table[i][j] == {}:
					name_table[i][j][user.part] = [user.name]
				else:
					if user.part in name_table[i][j].keys():
						name_table[i][j][user.part].append(user.name)
					else:
						name_table[i][j][user.part] = [user.name]
					if len(name_table[i][j][user.part])>2:
						if j==0:day="월"
						elif j == 1: day = "화"
						elif j == 2: day = "수"
						elif j == 3: day = "목"
						elif j == 4:day = "금"
						print(day+"요일",str((i+1))+"교시","시간의 시간당 수직자가 초과하였습니다.")
						print("다른 공강 시간을 입력해주세요.")
						return name_table

			j=j+1
		i=i+1
	return name_table

def print_user(user_list,user_name):
	for i, user in enumerate(user_list):
		if user.name==user_name:
			user.print_timetable()

def store_name_table(name_table):
    f = open("name_table_db.txt", "wb")
    pickle.dump(name_table,f)
    print("수직시간표가 저장되었습니다.")
    f.close()

def load_user_db(user_list):  # 텍스트파일로 저장된 person 객체를 불러오는 함수
    f = open("user_db.txt", "r")
    lines = f.readlines()  # 파일을 줄단위로 읽은 후
    num = len(lines) / 5  # 2줄 단위로 되어있는 이름과 수직시간을 하나로 분류
    num = int(num)

    for i in range(num):  # 순회하며 분류되어 있는 객체에 맞는 이름을 지정
        user_name = lines[5 * i].rstrip('\n')  # 첫줄은 객체 이름
        user_part = lines[5 * i + 1].rstrip('\n')  # 둘째줄은 객체 수직시간
        user_work_time = int(lines[5 * i + 2].rstrip('\n'))
        user_wish_worktime = int(lines[5 * i + 3].rstrip('\n'))
        try:
            user_timetable = pickle.load(lines[5 * i + 4].rstrip('\n'),'user_timetable_db.txt')
        except EOFError:
            pass
        user = User(user_name,user_part,user_work_time,user_wish_worktime,user_timetable)  # 줄 단위로 읽은 객체 이름과 수직시간을 맵핑
        user_list.append(user)  # 업무자 리스트에 모든 객체 추가
    f.close()

def load_name_table_db(name_table):  # 텍스트파일로 저장된 person 객체를 불러오는 함수
    try:
        f = open("name_table_db.txt", "rb")
        name_table = pickle.load(f)
        f.close()
    except EOFError:
	    pass
    return name_table

def delete_user(user_list, name): #이 함수는 연락처 리스트와 삭제할 이름을 인자로 입력받음.
    for i, user in enumerate(user_list): #i번 순회하여
        if user.name == name: #만약 i번째 인스턴스의 이름과 입력받은 이름이 같을 경우
            del user_list[i]

def print_menu():
	print("1. 시간표 보기\n2. 수직시간표 계산\n3. 사람 삭제\n4. 저장\n5. 종료")
	menu = input("메뉴선택: ")
	return int(menu)

def set_user(person_list,user_list):
	user_name = set_user_name(name_list)
	user_timetable = set_timetable(name_list, user_name, work_time_list)
	for person in person_list:
		if person.name == user_name:
			user_work_time = person.work_time
			user_part = person.part
			user_wish_worktime = person.wish_worktime
			user = User(user_name, user_part, user_work_time, user_wish_worktime, user_timetable)
			user.print_timetable()
			user_list.append(user)
			return user

def store_user_timetable(user_list):
	f = open("user_timetable_db.txt", "wb")
	for user in user_list:
		pickle.dump(user.timetable,f)
		print(user.name,"의 시간표가 저장되었습니다.")
	f.close()

def del_user(user_list,chn_name_table):
	del_name = input("삭제할 이름 : ")
	for del_user in user_list:
		if del_name == del_user.name:
			i = 0
			while i < 12:
				j = 0
				while j < 5:
					if del_user.part in chn_name_table[i][j].keys():
						if del_user.name in chn_name_table[i][j][del_user.part]:
							chn_name_table[i][j][del_user.part].remove(del_user.name)
							if chn_name_table[i][j][del_user.part] == []:
								del chn_name_table[i][j][del_user.part]
					else:
						pass
					j = j + 1
				i = i + 1

def load_del_user(person_list,load_name_table):
	del_name = input("삭제할 이름 : ")
	print(person_list)
	for del_user in person_list:
		if del_name == del_user.name:
			i = 0
			while i < 12:
				j = 0
				while j < 5:
					if del_user.part in load_name_table[i][j].keys():
						if del_user.name in load_name_table[i][j][del_user.part]:
							load_name_table[i][j][del_user.part].remove(del_user.name)
							if load_name_table[i][j][del_user.part] == []:
								del load_name_table[i][j][del_user.part]
					else:
						pass
					j = j + 1
				i = i + 1
	return load_name_table

def run():
	worktime_per_person.load_person_db(person_list, work_time_list, name_list, part_list, wish_worktime_list)
	global chn_name_table_frame
	user_list = []
	name_table = [[{} for h in range(5)] for u in range(12)]
	sat_user_name_list=[]
	copy_sat = sat_user_name_list.copy()
	load_name_table=load_name_table_db(name_table)
	#load_user_db(user_list)
	while True:  # 무한루프
		menu = print_menu()
		if menu == 1:
			load_name_table_frame = pd.DataFrame(load_name_table, index=time, columns=days)
			print(load_name_table_frame)

		elif menu == 2:
			user=set_user(person_list,user_list)
			sat_user_name_list.append(user.name)
			chn_name_table=set_name_table(user, basic_timetable, load_name_table,sat_user_name_list,copy_sat,user_list)
			chn_name_table_frame = pd.DataFrame(chn_name_table, index=time, columns=days)
			print("        -----수직시간표-----        ")
			print(chn_name_table_frame)



		elif menu == 3:
			try:
				del_user(user_list, chn_name_table)
				print("      -----수직시간표-----      ")
				print(chn_name_table_frame)
				store_name_table(chn_name_table)
			except:
				del_load_name_table = load_del_user(user_list,load_name_table)
				del_load_name_table_frame = pd.DataFrame(del_load_name_table, index=time, columns=days)
				print("      -----수직시간표-----      ")
				print(del_load_name_table_frame)
				store_name_table(del_load_name_table)

		elif menu == 4:
			store_user(user_list)
			store_user_timetable(user_list)
			store_name_table(chn_name_table)

		elif menu == 5:
			break


print("==================================================================")
work_time_list = []
name_list = []
person_list = []
part_list = []
wish_worktime_list = []
worktime_per_person.load_person_db(person_list, work_time_list, name_list,part_list,wish_worktime_list)
worktime_per_person.print_person(person_list)
print("==================================================================")
run()

'''
추노 함수 추가
'''