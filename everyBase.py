# coding=utf-8
'''
1.读取csv文件，让表格输出  --  容易编码出错，不要直接在excel表格填写数据再改格式，先新建csv格式的文件再填入数据
2.异常处理:try....except
3.多行打印
4.字典练习
5.学会使用接口文档看内置函数：python3.6 Module Docs
6.os模块
7.sys模块
8.urllib模块
9.re模块，正则表达式
10.tkinter模块：创建一个窗体,添加一个按钮,增加事务，增加菜单
11.pillow模块
12.threading：线程,active_count():当前激活线程数量，enumerate():激活的哪些线程，current_thread():当前线程，start():开启线程，join():控制线程运行的顺序，Lock.acquire():获取锁，Lock.release():解锁
13.Queue：队列（FIFO），put():把值放进队列，get():从队列取值
14.Mapplotlib：绘制2D图像--plot函数:坐标点，title():图像名，xlabel():x轴名称，ylabel():y轴名称,legend():显示图例,grid():显示网格,scatter():散点图，bar():柱状图
'''

import csv
import os
import time
import sys
import urllib.request
import urllib.parse  #参数的http请求
import re
from tkinter import *
from PIL import Image,ImageTk
import threading
from queue import Queue
import copy
from concurrent.futures import ThreadPoolExecutor #使用线程池
from matplotlib import pyplot

try:
    with open(r'C:\Users\gowild-666\Desktop\example02.csv') as csvfile:
        readCSV = csv.reader(csvfile,delimiter=',')
        citys = []
        passwords = []
        days = []
        for row in readCSV:
            print(row)
            # city = row[0]
            # password = row[1]
            # day = row[2]
        # citys.append(city)
        # passwords.append(password)
        # days.append(day)

        print(citys)
        print(passwords)
        print(days)

except Exception as e:
    print(e)
    print("请确认该csv文件是否存在")

print("********************************************")

# 多行打印
print('''
第一行内容：我是无敌美少年
第二行内容：我很努力的在学习
第三行内容：我将来要在深圳买房
。。。
============================================
|                                         |
|                                         |
|                                         |
|                                         |
|                 Wecome                  |
|                                         |
|                                         |
|                                         |
|                                         |      
============================================

''')

print("********************************************")
# 字典
# 设计几个不同城市的天气温度
temperature = {"北京":-10,"上海":3,"广州":15,"深圳":18}

print(temperature)

# 打印最高温度
print(temperature["深圳"])

# 字典加元素
temperature["重庆"] = 20
print(temperature)

# 删除上海
del temperature["上海"]
print(temperature)

# 更新北京的值
temperature["北京"] = -8
print(temperature)

# 升一维度字典嵌套
temp = {"成都":["温度：-5","天气：多云"],"苏州":["温度：5","天气：晴朗"]}
print(temp)

# 打印单个成都，并只打印温度
print(temp["成都"])
print(temp["成都"][0])

print("********************************************")

# 打印my_csv文件的当前目录路径
curDir = os.getcwd()
print(curDir)

# 新建文件夹
os.mkdir("helloworld")
time.sleep(2)

# 重命名文件夹
os.rename("helloworld","lalala")
time.sleep(2)

#删除文件夹
os.rmdir("lalala")

print("********************************************")
# 重定向标准错误信息
sys.stderr.write("This is a stderr text\n")

#因为重定向有缓冲区，所有需要去掉
sys.stderr.flush()
sys.stdout.write("This is a stdout text\n")

#获取命令行参数，默认sys.argv[0]表示代码本身的文件路径
print(sys.argv)

print("********************************************")

# 向服务器发送一个请求，打开百度学术首页
x = urllib.request.urlopen("http://xueshu.baidu.com")

# 打印该网页的源代码
print(x.read())

# 带参数的http请求
url = "http://php.weather.sina.com.cn/search.php"
values = {'city':'北京',
          'dpc':'1'
          }
'''
city=北京，北京这个字段会在网址栏上转码成：%B1%B1%BE%A9，这个转码过程叫做encode
'''
data = urllib.parse.urlencode(values)

# 参数编码格式默认是：Unicode，这里用的utf-8，最适合网络传输的编码协议
data = data.encode('utf-8')

# 调用url和参数的请求，通过Request（参数）
req = urllib.request.Request(url,data)

# 打开这个请求，通过urlopen函数
resq = urllib.request.urlopen(req)

# 定义一个响应返回的数据resqData，读取查询北京天气的页面
respData = resq.read()

# 打印北京查询天气页面的源代码
print(respData)

print("********************************************")

'''
\d:匹配所有的数字
\D:匹配所有的非数字
\s:空格
\S:非空格
\w:字母
\W:非字母
. :任意，除换行\n
\.:表示 . 本身，斜杠是转义字符
{1,3};表示至少一次，最多三次出现的
+:一或多
?:零或一
*:零或多
^:匹配字符串开头部分
$:匹配字符串结尾的部分
|:匹配左右表达式中任意一个
[A-Z]:表示大写A到Z
{5}:表示5次出现的
'''

exampleString = '''
Anthony is 18 years old, and Daniel is 27 years old.
Tom is 78 and his grandfather,Bob is 102. 
'''
# 找到所有一到三位的数字
ages = re.findall(r'\d{1,3}',exampleString)
print(ages)

# 找到所有英文名字，首字母大写，其他小写
names = re.findall(r'[A-Z][a-z]*',exampleString)
print(names)

# 把姓名跟年龄放到一个字典里里面输出
# 先定义一个字典
ageDict = {}
x = 0

for eachName in names:
    ageDict[eachName] = ages[x]
    x+=1
print(ageDict)

print("********************************************")

'''
开始接触桌面图形界面编程 
你可以到安装路径：\lib\tkinter 
打开__init__.py文件了解tkinter
'''
class Window(Frame):
    '''
    这里Frame是一个class，你可以在__init__.py里找到这个 class Frame(widget):
    这个意思说，定义一个Window类，Window的父类是Frame，这样Window就用了Frame的
    属性和功能。
    '''

    def __int__(self,master = None):
        '''
        构造函数
        :param master:
        :return:
        '''
        Frame.__init__(self,master)
        self.master = master
        self.init_window()

    def init_window(self):
        # 设置窗体的标题，如果不设置，默认显示tk
        self.master.title("第一个窗体")

        # 调用pack方法，让它根据文本自适应窗口大小
        self.pack(fill = BOTH,expand = 1)

        # # 创建一个按钮，调用tkinter下的Button类,添加一个comment，进行事务处理，点击退出按钮，执行退出程序
        # quitButton = Button(self,text = "退出",command = self.client_exit)
        #
        # quitButton.place(x = 0,y = 0)

        # 实例化一个Menu对象，这个在主窗体添加一个菜单
        menu = Menu(self.master)
        self.master.config(menu = menu)

        # 创建File菜单，下面有Save和Exit两个子菜单
        file = Menu(menu)
        file.add_command(label = "Save")
        file.add_command(label = 'Exit',command = self.client_exit)
        menu.add_cascade(label = 'File',menu = file)

        # 创建Edit菜单，下面有一个Undo菜单
        edit = Menu(menu)
        edit.add_command(label = 'Undo')
        edit.add_command(label = 'Show_Image',command = self.ShowImage)
        edit.add_command(label = 'Show_Text',command = self.ShowText)
        menu.add_cascade(label='Edit', menu=edit)

    def client_exit(self):
        exit()

    def ShowImage(self):
        # 实例对象加载我本地图片
        path = "C:\\Users\\gowild-666\\Desktop\\AR_UI\\a476.jpg" #需要转义，所以需要//去把 / 转义过来
        load = Image.open(path)
        render = ImageTk.PhotoImage(load)

        img = Label(self,image = render)
        img.image = render
        img.place(x = 0,y = 0)

    def ShowText(self):
        text = Label(self,text = "GUI图像编程")
        text.pack()

# 初始化一个Tk对象，Tk（）这个类描述的是一个窗体
root = Tk()

# 设置窗体大小
root.geometry("400x300")

# 把root这个窗体作为一个对象参数传入到我们定义的Window类中
app = Window(root)

# 出现退出按钮，点击并会调用client_exit()函数退出
app.init_window()

# w = Label(root,text = "hello,world")
# w.pack()

# mainloop()的解释是：执行Tk主要的loop
root.mainloop()

print("********************************************")

def thread_demo():

    # 打印当前激活的线程数量
    print(threading.active_count())

    # 查看上面激活的线程是哪几个
    print(threading.enumerate())

# 调用函数执行
thread_demo()

# 创建一个线程
def init_thread():
    add_thread = threading.Thread(target=thread_job)
    add_thread.start()

# 这是线程主要的工作是。。。
def thread_job():
    print("这是添加一个线程，序列号是%s" % threading.current_thread())

init_thread()

def thread1_job():
    print("T1 开始\n")
    for i in range(2):
        time.sleep(0.5)
    print("T1 结束\n")

def init_thread1():
    add_thread1 = threading.Thread(target=thread1_job,name='T1')
    add_thread1.start()
    add_thread1.join()
    print("所有任务都做完了。\n")

init_thread1()

print("********************************************")

def queue_job(data,q):
    for i in range(len(data)):
        data[i] = data[i]**2

    # put方法把结果放入队列，这里不能使用return语句
    q.put(data)

def queue_init():

    # 新建一个队列
    q = Queue()

    # 新建一个空的多线程列表
    threads = []

    # 给出数据，到queue_job去计算
    data = [[1,2,3],[2,3,4],[3,4,5],[4,5,6]]

    # for 循环创建一个多线程，大小根据data[]的大小
    for x in range(4):
        t = threading.Thread(target=queue_job(data[x],q))
        # 启动线程
        t.start()
        # 把创建的线程添加到线程组中
        threads.append(t)

    # bolck住主线程
    for each_thread in threads:
        each_thread.join()

    # 定义一个计算结果的类表
    results = []

    #把结果从队列中取出
    for y in range(4):
        results.append(q.get())
    # 打印结果列表
    print(results)

queue_init()

print("********************************************")

# 多线程比较：案例一
# def queue_job1(l,q1):
#     res = sum(l)
#     q1.put(res)
#
# def queue_inti1(l):
#     q1 = Queue()
#     threads1 = []
#     for x in range(4):
#         th1 = threading.Thread(target=queue_job1,args=(copy.copy(l),q1))
#         th1.start()
#         threads1.append(th1)
#
#     # 这样的写法是相当于把语句直接放前面，简化步骤，一行搞掂
#     [each_thread1.join() for each_thread1 in threads1]
#
#     total = 0
#     for x in range(4):
#         total += q1.get()
#     print(total)

# 多线程比较：案例二
'''
1.并行任务最好采用采用线程池的方式来进行
2.你建立的线程join了之后就会block住主线程的，相当于线程一个一个执行了，如果想做真正的并发，需要通过在start后，在主进程中判决变量来监控执行
3.计算normal的时候加长了list的长度会增加程序取值的时间消耗。
'''
def threadPool_job(l):
    return sum(l)

def threadPool_init(l):
    threads2 = []
    size = 4
    s_t1 = time.time()
    with ThreadPoolExecutor(max_workers=size) as executor:
        _futures = []
        for i in range(size):
            _futures.append(executor.submit(threadPool_job,l))
        total = sum([future.result() for future in _futures])
        print("多线程执行时间-->",time.time()-s_t1)
        print(total)

def normal(l):
    total = sum(l)
    print(total)

if __name__ == "__main__":
    l = list(range(1000000))

    s_t = time.time()
    # normal(l*4)--计算normal的时候加长了list的长度会增加程序取值的时间消耗
    for _ in range(4):
        normal(l)
    print("普通方法的执行时间是：",time.time()-s_t)

    s_t = time.time()

    # 案例一的调用
    # queue_inti1(l)

    # 案例二的调用
    threadPool_init(l)
    print("多线程执行的时间是：",time.time()-s_t)

print("********************************************")

def lock_job1():
    global A,lock
    # 开始插入一个锁标记，这个线程已经被锁住了
    lock.acquire()

    num = 10
    for i in range(num):
        A += 1
        print("lock_job1-->",A)

    # 等这个线程工作干完了，就释放锁，也就是解锁
    lock.release()

def lock_job2():
    global  A,lock
    lock.acquire()
    num = 10
    for i in range(num):
        A += 5
        print("lock_job2-->",A)

    lock.release()

def lock_init():
    # 定义一个共享内存，全局变量
    global A
    A = 0
    # 定义一个全局锁
    global lock
    lock = threading.Lock()

    t1 = threading.Thread(target=lock_job1)
    t2 = threading.Thread(target=lock_job2)
    t1.start()
    t2.start()
    t1.join()
    t2.join()

lock_init()

print("********************************************")

x = [5,6,7,8]
y = [7,3,8,3]

x1 = [2,5,3,9]
y1 = [5,3,2,7]

x2 = [6,2,1,5]
y2 = [3,7,8,4]

x3 = [9,5,2,7]
y3 = [6,6,1,8]
#
# x4 = [4,5,2,4]
# y4 = [1,6,1,2]
#
# x5 = [2,3,2,5]
# y5 = [6,9,3,5]
#
# x6 = [8,6,3,1]
# y6 = [4,9,4,6]
#
# x7 = [6,5,3,1]
# y7 = [7,3,1,7]

# 可以设置颜色，g代表green, r代表red，y代表yellow，b代表blue，k代表black,w代表white,c代表cyan（青色），m代表magenta（品红）
# linewidth:设置线条粗细
# label 设置线条名称
# pyplot.plot(x,y,'b',linewidth=5,label='Line One')
# pyplot.plot(x1,y1,'r',linewidth=8,label='Line Two')
# pyplot.plot(x2,y2,'g',linewidth=3,label='Line Three')
# pyplot.plot(x3,y3,'y',linewidth=6,label='Line Four')
# pyplot.plot(x4,y4,'k',linewidth=6,label='Line Five')
# pyplot.plot(x5,y5,'m',linewidth=6,label='Line Six')
# pyplot.plot(x6,y6,'c',linewidth=6,label='Line Seven')

# 绘制散点图用scatter函数
pyplot.scatter(x,y,color='b',label='Line One')
pyplot.scatter(x1,y1,color='r',label='Line Two')

# 绘制柱状图用bar函数
pyplot.bar(x2,y2,color='g',label='Line Three')
pyplot.bar(x3,y3,color='y',label='Line Four')

pyplot.title("XXX") # 最好不要中文，容易报错

pyplot.xlabel('x axis') # x轴名称

pyplot.ylabel('y axis') # y轴名称

# 显示图例
pyplot.legend()

# # 显示网格
# pyplot.grid(True,color='k')

pyplot.show()

