import random


def cal_worktime(name_list):
    ave_worktime = int(50 / len(name_list))
    over_worker = int(50 % len(name_list))
    rdm_over_woker = random.sample(name_list, over_worker)
    for i in enumerate(name_list):
        if rdm_over_woker in name_list:
            over_worktime = ave_worktime + 1
            return over_worktime
        else:
            return ave_worktime


def cal_ave_worktime(name_list):
    ave_worktime = int(50 / len(name_list))
    over_worktime = int(50 % len(name_list))
    print("명당 평균 수직시간은 {0}시간입니다.".format(ave_worktime))
    print("남은 수직시간은 {0}시간입니다.".format(over_worktime))


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