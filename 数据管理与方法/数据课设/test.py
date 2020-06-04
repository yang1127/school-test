import copy
#界面设计
# -*- coding:utf-8 -*-
from tkinter import *

HEIGHT = 5000
WIDTH = 5000
root = Tk()
root.title('私家车车辆使用管理系统')
root.geometry('900x800')

#此处为各个标题的设计
lb1 = Label(root,text='成员编号',font=('黑体',16,'bold'))
lb1.place(relx=0.05,rely=0.02)
lb2 = Label(root,text='姓名',font=('黑体',16,'bold'))
lb2.place(relx=0.17,rely=0.02)
lb3 = Label(root,text='性别',font=('黑体',16,'bold'))
lb3.place(relx=0.29,rely=0.02)
lb4 = Label(root,text='成员状态',font=('黑体',16,'bold'))
lb4.place(relx=0.41,rely=0.02)

#frame = Frame(root,bg='#80c1ff',bd=5)
flag = 1
t = 0
#显示/刷新操作
def Show():
    fr = open("私家车.txt", 'r+')
    s1 = fr.read()
    if len(s1):
        note = eval(s1)  # 读取的str转化为字典
        notes1 = copy.deepcopy(note)
    else:
        notes1={}
    fr.close()
    global t
    global flag
    if flag == 0:
        t = t + 1
    else:
        flag = 0
    for i in notes1.keys():
        label = Label(root, text='%s' % i, font=('宋体',14))
        label.place(relx=0.05, rely=0.06 + 0.03 * t)
        label = Label(root, text='%s' % notes1[i]['姓名'], font=('宋体', 14))
        label.place(relx=0.17, rely=0.06 + 0.03 * t)
        label = Label(root, text='%s' % notes1[i]['性别'], font=('宋体', 14))
        label.place(relx=0.29, rely=0.06 + 0.03 * t)
        label = Label(root, text='%s' % notes1[i]['成员状态'], font=('宋体', 14))
        label.place(relx=0.41, rely=0.06 + 0.03 * t)
        t = t+1
    label1 = Label(root,text='_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ ' '_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _' '_ _ _ _以上为最新纪录',font=0.5)
    label1.place(relx=0.05,rely=0.06+0.03*t)

#子窗体设计
#插入 _add 子窗体
def newwind_add():
    winNew = Toplevel(root)
    winNew.geometry('320x240')
    winNew.title('插入')
    #各个录入提示
    lb_1 = Label(winNew,text='请按以下要求依次输入!')
    lb_1.place(relx=0.29,rely=0.05)
    lb_1_1 = Label(winNew,text='成员编号：')
    lb_1_1.place(relx=0.08,rely=0.18)
    lb_1_2 = Label(winNew, text='成员姓名：')
    lb_1_2.place(relx=0.08, rely=0.3)
    lb_1_3 = Label(winNew, text='成员性别：')
    lb_1_3.place(relx=0.08, rely=0.42)
    lb_1_4 = Label(winNew, text='成员状态：')
    lb_1_4.place(relx=0.08, rely=0.54)
    #各个录入条框
    e1 = StringVar()
    entry1 = Entry(winNew,textvariable=e1)
    entry1.place(relx=0.3,rely=0.18)
    e2 = StringVar()
    entry2 = Entry(winNew, textvariable=e2)
    entry2.place(relx=0.3, rely=0.3)
    e3 = StringVar()
    entry3 = Entry(winNew, textvariable=e3)
    entry3.place(relx=0.3, rely=0.42)
    e4 = StringVar()
    entry4 = Entry(winNew, textvariable=e4)
    entry4.place(relx=0.3, rely=0.54)
    def add():      #插入成员函数
        fr = open("私家车.txt",'r+')
        s1 = fr.read()
        if len(s1):
            note = eval(s1)   #读取的str转化为字典
            notes1 = copy.deepcopy(note)
        else:
            notes1 = {}
        fr.close()
        id = e1.get()
        if id in notes1:
            lb_1_8 = Label(winNew, text='车内已有该成员！')
            lb_1_8.place(relx=0.5, rely=0.9)
        else:
            name = e2.get()
            sex = e3.get()
            status = e4.get()
            label = {'成员姓名': name, '成员性别': sex, '成员状态': status, }
            notes1[id] = label
            lb_1_7 = Label(winNew, text='录入成功!')
            lb_1_7.place(relx=0.5, rely=0.9)
            fw = open("私家车.txt","w+")
            fw.write(str(notes1))    #把字典转化为str
            fw.close()
    #录入按钮设计
    btAdd = Button(winNew,text='录入',command=add)
    btAdd.place(relx=0.4,rely=0.9)
    #退出按钮设计
    btClose=Button(winNew,text='退出',command=winNew.destroy)
    btClose.place(relx=0.88,rely=0.9)

#删除成员子窗体
def newwind_del():
    fr = open("私家车.txt", 'r+')
    s1 = fr.read()
    if len(s1):
        note = eval(s1)  # 读取的str转化为字典
        notes1 = copy.deepcopy(note)
    else:
        notes1={}
    fr.close()
    DelNew = Toplevel(root)
    DelNew.geometry('600x240')
    DelNew.title('删除')
    lb_2_1 = Label(DelNew, text='请输入要删除成员编号：')
    lb_2_1.pack()
    e7 = StringVar()
    entry1 = Entry(DelNew,textvariable=e7)
    entry1.pack()
    lb_2_2 = Label(DelNew, text= '请输入要删除成员姓名：')
    lb_2_2.pack()
    e8 = StringVar()
    entry2 = Entry(DelNew,textvariable=e8)
    entry2.pack()
    def mydel():    #为防止误删，此处用姓名与学号同时锁定对象
        id = e7.get()
        name = e8.get()
        if id in notes1:
            if name == notes1[id]['成员姓名']:
                e = notes1.pop(id)
                lb_2_3 = Label(DelNew, text='删除成功！')
                lb_2_3.pack()
                fw = open("私家车.txt", "w+")
                fw.write(str(notes1))  # 把字典转化为str
                fw.close()
            else:
                lb_2_3 = Label(DelNew, text='成员编号与成员姓名不匹配！')
                lb_2_3.pack()
        else:
            lb_2_3 = Label(DelNew, text='该成员不存在！')
            lb_2_3.pack()
        btDel = Button(DelNew, text='删除', command=mydel)
        btDel.pack()
        btClose = Button(DelNew, text='退出', command=DelNew.destroy)
        btClose.pack()

#修改学生子窗体
def modi_status(args):
    pass

def newwind_modi():

    ModiNew = Toplevel(root)
    ModiNew.geometry('500x600')
    ModiNew.title('修改')
    lb_3_1 = Label(ModiNew, text='请输入要修改成员编号：')
    lb_3_1.pack()
    e9 = StringVar()
    entry1 = Entry(ModiNew, textvariable=e9)
    entry1.pack()

    def modi_name():
        fr = open("私家车.txt", 'r+')
        s1 = fr.read()
        if len(s1):
            note = eval(s1)  # 读取的str转化为字典
            notes1 = copy.deepcopy(note)
        else:
            notes1 = {}
        fr.close()
        id = e9.get()
        lb_3_3 = Label(ModiNew, text='要修改成员姓名为：')
        lb_3_3.pack()
        e10 = StringVar()
        entry_1 = Entry(ModiNew, textvariable=e10)
        entry_1.pack()
        def name2():
            notes1[id]['成员姓名'] = e10.get()
            lb_3_8 = Label(ModiNew, text='修改成功！')
            lb_3_8.pack()
            fw = open("私家车.txt", "w")
            fw.write(str(notes1))  # 把字典转化为str
            fw.close()
        btCtl = Button(ModiNew, text='修改', command=name2)
        btCtl.pack()

    def modi_sex():
        fr = open("私家车.txt", 'r+')
        s1 = fr.read()
        if len(s1):
            note = eval(s1)  # 读取的str转化为字典
            notes1 = copy.deepcopy(note)
        else:
            notes1 = {}
        fr.close()
        id = e9.get()
        lb_3_4 = Label(ModiNew, text='要修改成员性别为：')
        lb_3_4.pack()
        e11 = StringVar()
        entry3 = Entry(ModiNew, textvariable=e11)
        entry3.pack()
        def sex2():
            notes1[id]['成员性别'] = e11.get()
            lb_3_8 = Label(ModiNew, text='修改成功！')
            lb_3_8.pack()
            fw = open("私家车.txt", "w")
            fw.write(str(notes1))  # 把字典转化为str
            fw.close()
        btCtl = Button(ModiNew, text='修改', command=sex2)
        btCtl.pack()

    def modi_status():
        fr = open("私家车.txt", 'r+')
        s1 = fr.read()
        if len(s1):
            note = eval(s1)  # 读取的str转化为字典
            notes1 = copy.deepcopy(note)
        else:
            notes1 = {}
        fr.close()
        id = e9.get()
        lb_3_5 = Label(ModiNew, text='要修改成员状态为：')
        lb_3_5.pack()
        e12 = StringVar()
        entry4 = Entry(ModiNew, textvariable=e12)
        entry4.pack()
        def workspace2():
            notes1[id]['成员状态'] = e12.get()
            lb_3_8 = Label(ModiNew, text='修改成功！')
            lb_3_8.pack()
            fw = open("私家车.txt", "w")
            fw.write(str(notes1))  # 把字典转化为str
            fw.close()
        btCtl = Button(ModiNew, text='修改', command=workspace2)
        btCtl.pack()

    def modi_all():
        fr = open("私家车.txt", 'r+')
        s1 = fr.read()
        if len(s1):
            note = eval(s1)  # 读取的str转化为字典
            notes1 = copy.deepcopy(note)
        else:
            notes1 = {}
        fr.close()
        id = e9.get()
        if id in notes1:
            lb_3_2 = Label(ModiNew, text='要修改成员内容为')
            lb_3_2.pack()
            btChoose1 = Button(ModiNew, text='成员姓名', command=modi_name)
            btChoose1.pack(side=LEFT,anchor=NW,ipadx=0.2)
            btChoose2 = Button(ModiNew, text='成员性别', command=modi_sex)
            btChoose2.pack(side=LEFT,anchor=NW,ipadx=0.2)
            btChoose3 = Button(ModiNew, text='成员状态', command=modi_status)
            btChoose3.pack(side=LEFT,anchor=NW,ipadx=0.2)
        else:
            lb_3_9 = Label(ModiNew, text='该成员不存在！')
            lb_3_9.pack()
    btCtl = Button(ModiNew, text='修改', command=modi_all)
    btCtl.pack()
    btclose = Button(ModiNew, text='退出', command=ModiNew.destroy)
    btclose.place(relx=0.89,rely=0.89)

#搜索操作

#按编号查找子窗体：
def newwind_search1():
    fr = open("私家车.txt", 'r+')
    s1 = fr.read()
    if len(s1):
        note = eval(s1)  # 读取的str转化为字典
        notes1 = copy.deepcopy(note)
    else:
        notes1 = {}
    fr.close()
    Se1New = Toplevel(root)
    Se1New.geometry('600x400')
    Se1New.title('按成员编号查找')
    lb_4_1 = Label(Se1New,text='请输入要查找成员编号：')
    lb_4_1.pack()
    e15 = StringVar()
    entry1 = Entry(Se1New,textvariable=e15)
    entry1.pack()
    def search1():
        id=e15.get()
        if id in notes1:
            lb_4_2 = Label(Se1New,text = '成员编号 %s 的姓名是 %s , 性别是 %s , 状态是 %s'
                      % (id, notes1[id]['成员姓名'], notes1[id]['成员性别'], notes1[id]['成员状态']))
            lb_4_2.pack()
        else:
            lb_4_3 = Label(Se1New,text='该成员不存在！')
            lb_4_3.pack()
    btse1 = Button(Se1New,text='搜索',command=search1)
    btse1.pack()

#按姓名查找子窗体：
def newwind_search2():
    fr = open("私家车.txt", 'r+')
    s1 = fr.read()
    if len(s1):
        note = eval(s1)  # 读取的str转化为字典
        notes1 = copy.deepcopy(note)
    else:
        notes1 = {}
    fr.close()
    Se2New = Toplevel(root)
    Se2New.geometry('600x400')
    Se2New.title('按成员姓名查找')
    lb_5_1 = Label(Se2New,text='请输入要查找成员姓名：')
    lb_5_1.pack()
    e16 = StringVar()
    entry1 = Entry(Se2New,textvariable=e16)
    entry1.pack()
    def search2():
        name = e16.get()
        t = 0   #计数器
        for i in notes1.keys():
            t = t+1
            if notes1[i]['成员姓名'] == name:
                lb_5_2 = Label(Se2New,text='成员编号 %s 的姓名是 %s , 性别是 %s , 状态是 %s'
                      % (i, notes1[i]['成员姓名'], notes1[i]['成员性别'], notes1[i]['成员状态']))
                lb_5_2.pack()
                t = 0   #输出则计数器清零
        if t == len(notes1):
            lb_5_3 = Label(Se2New,text='该成员不存在！')
            lb_5_3.pack()
    btse2 = Button(Se2New, text='搜索', command=search2)
    btse2.pack()

#统计操作

#统计总人数
def newwind_Sp():
    fr = open("私家车.txt", 'r+')
    s1 = fr.read()
    if len(s1):
        note = eval(s1)  # 读取的str转化为字典
        notes1 = copy.deepcopy(note)
    else:
        notes1 = {}
    fr.close()
    SpNew = Toplevel(root)
    SpNew.geometry('320x180')
    SpNew.title('使用该车总人数')
    sum = len(notes1)
    lb_7 = Label(SpNew,text='总数为 %d '%sum,font=('黑体',16,'bold') )
    lb_7.pack()
    btClose = Button(SpNew, text='退出', command=SpNew.destroy)
    btClose.place(relx=0.7, rely=0.7)

#统计男性人数
def newwind_Sman():
    fr = open("私家车.txt", 'r+')
    s1 = fr.read()
    if len(s1):
        note = eval(s1)  # 读取的str转化为字典
        notes1 = copy.deepcopy(note)
    else:
        notes1 = {}
    fr.close()
    SmanNew = Toplevel(root)
    SmanNew.geometry('320x180')
    SmanNew.title('使用该车男性总数')
    t = 0
    for i in notes1.keys():
        if notes1[i]['成员性别']=='男':
            t = t+1
    lb_8 = Label(SmanNew,text='男性总数为 %d '%t,font=('黑体',16,'bold') )
    lb_8.pack()
    btClose = Button(SmanNew, text='退出', command=SmanNew.destroy)
    btClose.place(relx=0.7, rely=0.7)

#统计女性人数
def newwind_Sfemale():
    fr = open("私家车.txt", 'r+')
    s1 = fr.read()
    if len(s1):
        note = eval(s1)  # 读取的str转化为字典
        notes1 = copy.deepcopy(note)
    else:
        notes1 = {}
    fr.close()
    SfemaleNew = Toplevel(root)
    SfemaleNew.geometry('320x180')
    SfemaleNew.title('使用该车女性总数')
    t = 0
    for i in notes1.keys():
        if notes1[i]['性别']=='女':
            t = t+1
    lb_9 = Label(SfemaleNew, text='女性总数为 %d ' % t,font=('黑体',16,'bold'))
    lb_9.pack()
    btClose = Button(SfemaleNew, text='退出', command=SfemaleNew.destroy)
    btClose.place(relx=0.7, rely=0.7)

#菜单设计
mainmenu = Menu(root)
menuFile = Menu(mainmenu)   #菜单分组 menuFile
mainmenu.add_cascade(label="私家车",menu=menuFile)
menuFile.add_command(label="显示/刷新",command=Show)
menuFile.add_separator()    #分割线
menuFile.add_command(label="退出",command=root.destroy)

menuEdit = Menu(mainmenu)   #菜单分组 menuEdit
mainmenu.add_cascade(label="编辑",menu=menuEdit)
menuEdit.add_command(label="插入",command=newwind_add)
menuEdit.add_command(label="修改",command=newwind_modi)
menuEdit.add_command(label="删除",command=newwind_del)

menuSearch = Menu(mainmenu) #菜单分组 menuSearch
mainmenu.add_cascade(label="查询",menu=menuSearch)
menuSearch.add_command(label="按成员编号查找",command=newwind_search1)
menuSearch.add_command(label="按成员姓名查找",command=newwind_search2)

menuCount = Menu(mainmenu)  #菜单分组 menuCount
mainmenu.add_cascade(label="统计使用该车总人数",menu=menuCount)
menuCount.add_command(label="总数",command=newwind_Sp)
menuCount.add_command(label="男性总数",command=newwind_Sman)
menuCount.add_command(label="女性总数",command=newwind_Sfemale)

#将鼠标的触发位置event.x_root 和 event.y_root以post()方法传给菜单
def popupmenu(event):
    mainmenu.post(event.x_root, event.y_root)
root.config(menu=mainmenu)
root.bind('<Button-3>',popupmenu) # 根窗体绑定鼠标右击响应事件

root.mainloop()