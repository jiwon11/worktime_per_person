import pickle
import pandas as pd

class Person:
	def __init__(self, person_name,person_part,person_work_time,person_wish_worktime):
		self.name = person_name
		self.part = person_part
		self.work_time = int(person_work_time)
		self.wish_worktime = int(person_wish_worktime)
		super(Person,self).__init__()

	def print_info(self):
		print("       name : ", self.name)
		print("       part : ",self.part)
		print("       work time : ", self.work_time)
		print("       wish work time : ",self.wish_worktime)

def set_person(person_list,name_list,part_list,ave_worktime,wish_worktime_list):
	for i in range(len(name_list)):
		person_name = name_list[i]
		person_part = part_list[i]
		person_wish_worktime = wish_worktime_list[i]
		if person_part in ave_worktime.keys():
			person_work_time = ave_worktime[person_part]
			person = Person(person_name,person_part,person_work_time,person_wish_worktime)
			person_list.append(person)

def print_person(person_list):
	print('-' * 10, 'employee list', '-' * 10)
	try:
		for person in person_list:
			person.print_info()
			print('\n')
	except AttributeError as err:
		print("There are no employees...")


def add_person():
	name = input("name : ")
	return name

def add_part():
	part = input("part : ")
	return part

def add_wish_worktime():
	wish_worktime = int(input("wish work time : "))
	return wish_worktime

def cal_ave_worktime(name_list, part_list, part_time_dic):
	name_part_list = list(zip(name_list,part_list))
	person_count_part = {}
	for i in part_time_dic.keys():
		count = 0
		for j in range(len(name_part_list)):
			if name_part_list[j][1] == i:
				count += 1
		person_count_part[i]=count
	print('total employees for each part :',person_count_part)

	part_time = list(part_time_dic.values())
	part_name = list(part_time_dic.keys())
	count_person_part = list(person_count_part.values())
	per_part_time_ave = {}
	per_part_time_ove = {}
	for i in range(len(part_time)):
		try:
			ave_worktime = int(int(part_time[i])/int(count_person_part[i]))
			over_worktime = int(int(part_time[i])%int(count_person_part[i]))
			per_part_time_ave[part_name[i]] = ave_worktime
			per_part_time_ove[part_name[i]] = over_worktime
		except ZeroDivisionError:
			print("There is no employees for {0} part .".format(part_name[i]))
			pass
	print("Average work time for each part is {0}.".format(per_part_time_ave))
	print("Remain work time for each part is {0}.".format(per_part_time_ove))
	return per_part_time_ave,per_part_time_ove


def set_part(name_list,replace_part,part_list,person_list):
	print('The part is divided like this',replace_part)
	part_time = input("Write the allocated work time for each part : ")
	part_time_dic = {}
	for i in range(len(replace_part)):
		part_time_dic[replace_part[i]] = part_time
	print(part_time_dic)
	ans = input("Do you want change employee's part?")
	if ans == 'yes':
		chn_part_name = input("change part employee's name :")
		for person in person_list:
			if chn_part_name == person.name:
				print("change",person.name,"'s part")
				chn_part = input("change part : ")
				if chn_part not in part_time_dic.keys():
					print(chn_part,"not in part list!!")
				else:
					person.part = chn_part
					person.print_info()
	else:
		pass
	return part_time_dic

def cal_over_worktime(person_list,ove_worktime,part_list,ave_worktime):
	for person in person_list:
		if ove_worktime[person.part] == 0:
			continue
		if person.wish_worktime > person.work_time:
			person.work_time += 1
			print('For part',person.part,person.name, "'s work time exceeded from",ave_worktime[person.part],'to',person.work_time)
			ove_worktime[person.part] -= 1
	print(ove_worktime)
	for i in person_list:
		print(i.name)

def store_person(person_list):
	f = open("C:/Users/jiwon/Documents/GitHub/code package/DSA_teampl/person_db.txt", "wt", encoding='utf8')
	for person in person_list:
		f.write(person.name + '\n')
		f.write(str(person.work_time) + '\n')
		f.write(person.part + '\n')
		f.write(str(person.wish_worktime) + '\n')
		print(person.name, "is stored.")
	f.close()# 파일 닫음.


def load_person_db(person_list,name_list,part_list, work_time_list,wish_worktime_list):
	f = open("C:/Users/jiwon/Documents/GitHub/code package/DSA_teampl/person_db.txt", "rt")
	lines = f.readlines()
	num = len(lines) / 4
	num = int(num)

	for i in range(num):
		person_name = lines[4 * i].rstrip('\n')
		person_work_time= lines[4 * i + 1].rstrip('\n')
		person_part = lines[4 * i +2].rstrip('\n')
		person_wish_worktime = lines[4 * i + 3].rstrip('\n')
		name_list.append(person_name)
		work_time_list.append(person_work_time)
		part_list.append(person_part)
		wish_worktime_list.append(person_wish_worktime)
		person = Person(person_name, person_part, person_work_time, person_wish_worktime)
		person_list.append(person)
	f.close()


def run_per_person():
	work_time_list = []
	name_list = []
	person_list = []
	part_list = []
	wish_worktime_list = []
	load_person_db(person_list,name_list,part_list, work_time_list,wish_worktime_list)
	print_person(person_list)
	for uu in person_list:
		part_list.append(uu.part)
	non_over_lab_part_list = list(set(part_list))
	ans = input("Do you want to change the part?")
	replace_part=[]
	if ans == 'yes' or non_over_lab_part_list == []:
		answ = input("Do you want to add the part?")
		if answ == 'yes':
			input_part = input("Input the part : ")
			replace_part = input_part.split(',')
			print(replace_part)
		elif answ == 'no':
			replace_part = non_over_lab_part_list
	elif ans == 'no':
		replace_part = non_over_lab_part_list
	part_time_dic = set_part(name_list, replace_part, part_list,person_list)
	while 1:  # 무한루프
		print("--------------------------------------------------")
		input_person_ans = input("Do you want to write employees?")
		if input_person_ans == 'yes':
			name = add_person()
			name_list.append(name)
			part = add_part()
			if part not in replace_part:
				print("None of the part is written.")
				break
			part_list.append(part)
			wish_worktime = add_wish_worktime()
			wish_worktime_list.append(wish_worktime)
			print("Employee's name : ", name_list,"The total number of employees is {0}.".format(len(name_list)))
			ave_worktime,ove_worktime = cal_ave_worktime(name_list,part_list,part_time_dic)
			person_list.clear()
			set_person(person_list,name_list,part_list,ave_worktime,wish_worktime_list)
			cal_over_worktime(person_list, ove_worktime, part_list, ave_worktime)
			print_person(person_list)
			if input("Do you want to save as textfile? ") == '네' or 'yes':
				store_person(person_list)
			else:
				pass
		else:
			store_person(person_list)
			break
		print("--------------------------------------------------")
time = ['am9~am10','am10~am11','am11~pm12','pm12~pm1','pm1~pm2','pm2~pm3','pm3~pm4','pm4~pm5','pm5~pm6','pm6~pm7','pm7~pm8','pm8~pm9']
days = ['   Mon   ','   Tus   ','   Wed   ','   Thu   ','   Fri   ']

class User(Person):
	def __init__(self,user_name,user_part,user_work_time,user_wish_worktime,user_timetable):
		super().__init__(user_name,user_part,user_work_time,user_wish_worktime)
		self.timetable = user_timetable

	def print_timetable(self):
		print("    {0}'s possible work-hour time table   (0 = impossible and 1 = possible) ".format(self.name))
		print(pd.DataFrame(self.timetable,index=time,columns=days))

class OverWorkerError(Exception):
	def __init__(self):
		super().__init__("The worker per hour was exceeded")

basic_timetable = [[0] * 5 for z in range(12)]

def set_timetable(name_list,user_name,work_time_list):
	user_timetable = [[0] * 5 for x in range(12)]
	turn = name_list.index(user_name)
	count = int(work_time_list[turn])
	print("Enter your empty time for work {0} times.".format(count))
	i = 1
	while (i <= count):
		day = input("Input the day (mon~fri) : ")
		period = int(input("Input the hour (1~12) : ")) - 1
		if (day == "mon"):
			user_timetable[period][0] = 1
		elif (day == "tue"):
			user_timetable[period][1] = 1
		elif (day == "wed"):
			user_timetable[period][2] = 1
		elif (day == "thr"):
			user_timetable[period][3] = 1
		elif (day == "fri"):
			user_timetable[period][4] = 1
		print("{0} times left.".format(count - i))
		i = i + 1
	return user_timetable

def set_user_name(name_list):
	user_name = input("Enter name: ")
	for i, name in enumerate(name_list):
		if (user_name == name):
			print("start")
			return user_name

def set_name_table(user, basic_timetable, name_table,sat_user_name_list,copy_sat,user_list):
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
						if j==0:day="mon"
						elif j == 1: day = "tue"
						elif j == 2: day = "wed"
						elif j == 3: day = "thr"
						elif j == 4:day = "fri"
						print(day+"day",str((i+1))+"hour","'s worker are exceeded.")
						print("Enter another empty time for work.")
						return name_table

			j=j+1
		i=i+1
	return name_table

def print_user(user_list,user_name):
	for i, user in enumerate(user_list):
		if user.name==user_name:
			user.print_timetable()

def store_name_table(name_table):
	f = open("C:/Users/jiwon/Documents/GitHub/code package/DSA_teampl/name_table_db.txt", "wb")
	pickle.dump(name_table,f)
	print("The work time table is stored.")
	f.close()

def load_user_db(user_list):
	f = open("C:/Users/jiwon/Documents/GitHub/code package/DSA_teampl/user_db.txt", "r")
	lines = f.readlines()
	num = len(lines) / 5
	num = int(num)

	for i in range(num):
		user_name = lines[5 * i].rstrip('\n')
		user_part = lines[5 * i + 1].rstrip('\n')
		user_work_time = int(lines[5 * i + 2].rstrip('\n'))
		user_wish_worktime = int(lines[5 * i + 3].rstrip('\n'))
		try:
			global user_timetable
			user_timetable = pickle.load(lines[5 * i + 4].rstrip('\n'),'user_timetable_db.txt')
		except EOFError:
			pass
		user = User(user_name,user_part,user_work_time,user_wish_worktime,user_timetable)
		user_list.append(user)
	f.close()

def load_name_table_db(name_table):
	try:
		f = open("C:/Users/jiwon/Documents/GitHub/code package/DSA_teampl/name_table_db.txt", "rb")
		name_table = pickle.load(f)
		f.close()
	except EOFError:
		pass
	return name_table

def delete_user(user_list, name):
	for i, user in enumerate(user_list):
		if user.name == name:
			del user_list[i]

def print_menu():
	print("1. Calculate the work time table\n2. Delete the employee \n3. Save \n4. Exit")
	menu = input("Selcet the menu: ")
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
			return user

def store_user_timetable(user_list):
	try:
		f = open("C:/Users/jiwon/Documents/GitHub/code package/DSA_teampl/user_timetable_db.txt", "wb")
		for user in user_list:
			pickle.dump(user.timetable,f)
		print(user.name,"'s time table is stored.")
		f.close()
	except:
		pass

def del_user(user_list,chn_name_table):
	print_person(user_list)
	del_name = input("The name you want to erase : ")
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
			user_list.remove(del_user)
			print(del_user.name, "'s delete.")

def load_del_user(person_list,load_name_table):
	print_person(person_list)
	del_name = input("The name you want to erase : ")
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
				person_list.remove(del_user)
				print(del_name, "'s delete.")
	return load_name_table

def run_timetable():
	load_person_db(person_list, name_list, part_list, work_time_list, wish_worktime_list)
	global chn_name_table_frame
	user_list = []
	name_table = [[{} for h in range(5)] for u in range(12)]
	sat_user_name_list = []
	copy_sat = sat_user_name_list.copy()
	load_name_table = load_name_table_db(name_table)
	load_user_db(user_list)
	while True:
		menu = print_menu()
		if menu == 1:
			global chn_name_table
			user = set_user(person_list,user_list)
			sat_user_name_list.append(user.name)
			chn_name_table=set_name_table(user, basic_timetable, load_name_table,sat_user_name_list,copy_sat,user_list)
			chn_name_table_frame = pd.DataFrame(chn_name_table, index=time, columns=days)
			print("        -----Time Table-----        ")
			print(chn_name_table_frame)

		elif menu == 2:
			global del_load_name_table
			del_load_name_table = load_del_user(person_list,load_name_table)
			del_load_name_table_frame = pd.DataFrame(del_load_name_table, index=time, columns=days)
			print("      -----TimeTable-----      ")
			print(del_load_name_table_frame)
			store_name_table(del_load_name_table)

		elif menu == 3:
			store_name_table(chn_name_table)
			if len(person_list) == len(user_list):
				pass
			else:
				store_person(person_list)
			store_user_timetable(user_list)

		elif menu == 4:
			break

def print_title():
	print("1. Recall the data")
	print("2. show Time Table")
	print("3. Input employees")
	print("4. Change Time Table - add or delete")
	print("5. Exit")
	title = input("Selcet the title: ")
	return int(title)
print("==================================================================")
work_time_list = []
name_list = []
person_list = []
part_list = []
wish_worktime_list = []
name_table = [[{} for h in range(5)] for u in range(12)]
load_name_table = load_name_table_db(name_table)
print("               Make TimeTable for employment          ")
print("                                       -Team bonobono-")
print("==================================================================")
while True:
	title = print_title()
	if title == 1:
		load_person_db(person_list,name_list,part_list, work_time_list,wish_worktime_list)
		print("I recalled the data.")
	elif title == 2:
		load_name_table_frame = pd.DataFrame(load_name_table, index=time, columns=days)
		print(load_name_table_frame)
	elif title == 3:
		run_per_person()
	elif title == 4:
		run_timetable()
	elif title == 5:
		break

'''
데이터셋 증가 --> 런타임 측정
part를 수정했을 경우 다른 part의 employee들의 part를 수정할 것인지 물어보고
yes일 경우 수정한 part와 다른 employee들을 보여준 후 input을 요구.
'''