#With.py
#ver 0.3
#추가된 기능
#1. 같은 이름 예외처리
#2. 프로그램 종료 후 다시시작 가능
#3. 삭제 시 삭제 안내문구 추가(예정)
#회의에 따라 기능이 추가될 수 있음.
class Contact: 
    def __init__(self, name, phone_number):
        self.name = name
        self.phone_number = phone_number

    def print_info(self):
        print("Name: ", self.name)
        print("Phone Number: ", self.phone_number)
#클래스 인스턴스를 생성할 때 이름, 전화번호를 입력받을 수 있게 생성자를 선언
#인스턴스 변수에 저장된 정보를 화면에 출력하기 위해 print_info라는 메서드도 정의

class SameNameError(Exception):
    def __init__(self):
        super().__init__("이미 저장되어 있는 이름입니다.")
        
def set_contact(contact_list):
    name = input("Name(같은 이름은 입력할 수 없습니다.) : ")
    for i, contact in enumerate(contact_list):                  
        if contact.name == name: #예외처리는 제대로 작동, but 이 조건문에 따라 제대로 된 기능이 구현됨.(해결)
            raise SameNameError() 
            #에러가 일어나면서 기존의 리스트에 있던 연락처만 다시 호출되는 문제를 해결하여야 함.(해결)
        else:
            pass
    phone_number = input("Phone Number: ")
    contact = Contact(name, phone_number)
    return contact
#사용자로부터 데이터를 입력받는 함수인 set_contact() 함수를 새로 정의
#run() 함수에서 set_contact() 함수를 호출
#set_contact() 함수의 마지막 두 줄에서 Contact 클래스의 인스턴스를 생성하고 이를 반환

def print_contact(contact_list): #Contact 인스턴스를 저장하고 있는 리스트를 인자를 입력받은 후 
    for contact in contact_list: #for 문을 이용해 리스트에 저장된 인스턴스를 순회
        contact.print_info() #이때 각 인스턴스에서 print_info() 메서드를 호출

def delete_contact(contact_list, name): #이 함수는 연락처 리스트와 삭제할 이름을 인자로 입력받음.
    for i, contact in enumerate(contact_list): #i번 순회하여
        if contact.name == name: #만약 i번째 인스턴스의 이름과 입력받은 이름이 같을 경우
            del contact_list[i] #i번째 인스턴스을 삭제함.

def print_menu():
    print("1. 연락처 추가")
    print("2. 연락처 검색")
    print("3. 연락처 삭제")
    print("4. 연락처 저장")
    print("5. 종료")
    menu = input("메뉴선택: ")
    return int(menu)

def store_contact(contact_list): #contact_list라는 리스트를 입력받은 후 해당 리스트에 있는 Contact 인스턴스를 순회하면서 데이터를 파일로 저장
    f = open("contact_db.txt", "wt")
    for contact in contact_list: #contact_list를 순회하면서 각 인스턴스의 정보를 write 함수를 통해 출력
        f.write(contact.name + '\n') # 출력되는 각 정보가 파일에서 각 라인 단위로 저장되도록 '\n'을 사용
        f.write(contact.phone_number + '\n')
    f.close()

def load_contact(contact_list): #contact_list를 인자로 받음.
    f = open("contact_db.txt", "rt")#함수 내부에서 'contact_db.txt' 파일을 연다.
    lines = f.readlines() #해당 파일을 라인 단위로 저장된
    num = len(lines) / 2 #(연락처 하나당 2줄의 데이터가 존재하므로 파일에서 읽어들인 전체 라인 수를 2로 나누어 몇 개의 데이터가 존재하는지 확인)
    num = int(num)

    for i in range(num):
        name = lines[2*i].rstrip('\n')
        phone = lines[2*i+1].rstrip('\n')
        contact = Contact(name, phone) #이름, 전화번호로 읽어 들여 Contact 클래스의 인스턴스를 생성
        contact_list.append(contact) #그런 다음 생성한 인스턴스를 contact_list에 추가
    f.close()

def run():
    contact_list = []
    load_contact(contact_list)
    while True: #무한루프
        menu = print_menu()
        if menu == 1:
            try:
                contact = set_contact(contact_list) #set_contact() 함수는 사용자로부터 연락처를 입력받을 때 사용하는 함수
                contact_list.append(contact) #사용자가 '1. 연락처 입력' 메뉴를 선택했을 때 run() 함수에서 set_contact() 함수를 호출
            except SameNameError as err:
                print("오류가 발생했습니다. {0}".format(err))
                break
        elif menu == 2:
            print_contact(contact_list)
        elif menu == 3:
            name = input("Name: ")
            delete_contact(contact_list, name)
        elif menu == 4:
            store_contact(contact_list)
        elif menu == 5:
            break

if __name__ == "__main__":
    run()
    while True:
        print("연락처를 다시 시작하려면 '다시시작'을 입력하세요...")
        if input() == "다시시작":
            run()
        else:
            print("종료")
            break