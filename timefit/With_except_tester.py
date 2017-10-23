import os, sys, time
class Contact: 
    def __init__(self, name, phone_number):
        self.name = name
        self.phone_number = phone_number

    def print_info(self):
        print("Name: ", self.name)
        print("Phone Number: ", self.phone_number)

class SameNameError(Exception):
      def __init__(self):
          super().__init__("이미 저장되어 있는 이름입니다.")

def set_contact(contact_list):
    name = input("Name: ")
    phone_number = input("Phone Number: ")
    contact = Contact(name, phone_number)
    for i in enumerate(contact_list):
        if contact.name == name:
            raise SameNameError()
        else:
            pass
    return contact

def print_contact(contact_list):
    for contact in contact_list:
        contact.print_info()

def restart():  
    executable = sys.executable
    args = sys.argv[:]
    args.insert(0, sys.executable)

    time.sleep(1)
    os.execvp(executable, args)

def run():
      contact_list = []
      while True:
          try:
              contact = set_contact(contact_list)
              contact_list.append(contact)
          except SameNameError as err:
              print("오류가 발생했습니다. {0}".format(err))
              del contact_list[contact]
          print("--------------------------")
          print_contact(contact_list)
          print("--------------------------")

run()
#SamaNameError가 제대로 작동되는지를 먼저 테스트해봐야됨. (V1.0)
#예외 처리는 제대로 작동 but 새로운 이름을 입력을 하지 못함. (V1.1)
#새로운 이름을 입력하는 방법을 찾지 못하여 break문을 통해 함수를 중단하는 걸로 임시방편을 새움.(V1.2)
