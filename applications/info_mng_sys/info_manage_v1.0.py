# 函数区


def add_stu(stu_lst):
    """
    增加学生信息
    """
    stu_dict = {}  # 储存单个学生信息
    try:
        id = input("请输入要录入的学生的学号：")
        for i in range(len(stu_lst)):
            if stu_lst[i]['id'] == id:
                print("您输入的学号已经存在！")
            return

        name = input("请输入要录入的学生的姓名：")
        age = input("请输入要录入的学生的年龄：")
        stu_dict['id'] = id
        stu_dict['name'] = name
        stu_dict['age'] = age

        stu_lst.append(stu_dict)  # 添加学生信息到数据库
        print("添加成功！")
    except BaseException:
        print("发生异常， 不能正常添加！")


def lookup_stu(stu_lst):
    """
    查询学生信息
    """
    try:
        id = input("请输入要查询学生的学号：")
        if id == "all":
            print("当前学生信息如下： ", stu_lst)
            return
        for i in range(len(stu_lst)):
            if stu_lst[i]['id'] == id:
                print("您查询的学生信息如下：", stu_lst[i])
                return
        print("没有找到你要查询的信息")
        return
    except BaseException:
        print("发生异常，查询失败")
        return


def modify_stu(stu_lst):
    """
    修改学生信息
    """
    try:
        id = input("请输入要修改的学生学号：")
        for i in range(len(stu_lst)):
            if stu_lst[i]['id'] == id:
                name = input("请输入修改后的姓名：")
                age = input("请输入修改后的年龄：")
                stu_lst[i]['id'] = name
                stu_lst[i]['age'] = age
                print("修改成功！")
                return
        print("找不到该学号，不能进行修改！")
    except BaseException:
        print("发生异常，修改失败！")


def del_stu(stu_lst):
    """
    删除学生信息
    """
    try:
        id = input("请输入要删除的学号：")
        for i in range(len(stu_lst)):
            if stu_lst[i]['id'] == id:
                del stu_lst[i]
                return 0
            return 1
    except BaseException:
        return 2


# 运行区
if __name__ == '__main__':

    print("--*--" * 10)
    print(" " * 10, "欢迎使用学生信息管理系统v1.0")
    print(" " * 15, "1 添加学生信息")
    print(" " * 15, "2 查询学生信息")
    print(" " * 15, "3 修改学生信息")
    print(" " * 15, "4 删除学生信息")
    print(" " * 15, "5 退出系统")
    print("--*--" * 10)

    flag = 0
    stu_lst = []  # 保存所有学生信息的列表

    while flag != 1:

        step = input("请输入操作：")
        try:
            step = int(step)
        except BaseException:
            print("发生异常，请您检查输入是否是数字类型")
            continue

        if step == 1:
            add_stu(stu_lst)
            print("当前学生信息如下：", stu_lst)

        elif step == 2:
            # 查询信息
            lookup_stu(stu_lst)

        elif step == 3:
            # 修改
            modify_stu(stu_lst)
            print("当前学生信息：", stu_lst)

        elif step == 4:
            rst = del_stu(stu_lst)
            if rst == 0:
                print("删除成功！")
            elif rst == 1 or rst == 2:
                print("删除失败")
            print("当前学生信息如下：", stu_lst)

        else:
            flag = 1

print("退出系统成功！")
