XING_PROBLEM_LIST = []

with open('data/兴趣爱好与日常活动.txt', encoding='utf-8', mode='r') as file:
    # 使用 for循环逐行读取文件
    for line in file:
        # 打印每一行的内容
        XING_PROBLEM_LIST.append(line.replace("\n", ""))

XUE_PROBLEM_LIST = []

with open('data/学校生活与学术讨论.txt', encoding='utf-8', mode='r') as file:
    # 使用 for循环逐行读取文件
    for line in file:
        # 打印每一行的内容
        XUE_PROBLEM_LIST.append(line.replace("\n", ""))

WEI_PROBLEM_LIST = []

with open('data/未来规划与职业发展.txt', encoding='utf-8', mode='r') as file:
    # 使用 for循环逐行读取文件
    for line in file:
        # 打印每一行的内容
        WEI_PROBLEM_LIST.append(line.replace("\n", ""))

KUA_PROBLEM_LIST = []

with open('data/跨文化交流与观点分享.txt', encoding='utf-8', mode='r') as file:
    # 使用 for循环逐行读取文件
    for line in file:
        # 打印每一行的内容
        KUA_PROBLEM_LIST.append(line.replace("\n", ""))

PROBLEM_LIST = []

PROBLEM_LIST = XUE_PROBLEM_LIST + XING_PROBLEM_LIST + KUA_PROBLEM_LIST + WEI_PROBLEM_LIST
