# -*- coding: utf-8 -*-
# Lesson I

# list1=[1,2,3,4]
# list1[2]=10
# print(list1)
# a='"The Zen of Python"'
# b="-- by Tim Peters"
# print(a+b)
#
# c="xyz"
# d="abc"
# print(c+d)
# print(c[1:3])
# print(d*10)
# print("a" in c, "a" in d)

# list1=[1,2,3,4,5]
# list1.append(100)
# print(list1)
# print(list1[0:3],list1[-1])
# list1.remove(3)
# print(list1)

# str="中国联通上海分公司"
# 分个按顺序输出
# for s in str:
#     print(s)

# 输出列表中的偶数
# list=[1,2,3,4,5,6,7,8,9,0]
# for s in list:
#     if(s%2==0):
#         print(s)

# 读取本地文件夹中所有的文件，并筛选出属于office的文档（第三方库？程序骨架？模糊查询）

#案例：判断输出1990年7月12日出生的人的星座和属相，
# 并且格式化输出：xx年xx月xx日出生的人属相为x，星座为xxx

# chinese_zodiac = "猴鸡狗猪鼠牛虎兔龙蛇马羊"
#
# year = 1995
#
# zodiac_name = ("摩羯座","水瓶座","双鱼座","白羊座","金牛座","双子座","巨蟹座","狮子座","处女座","天秤座","天蝎座","射手座")
#
# zodiac_days = ((1,20),(2,19),(3,21),(4,20),(5,21),(6,22),(7,23),(8,23),(9,23),(10,24),(11,23),(12,22))
#
# (month,day) = (6,12)
#
# # zodiac_days中的元素一个个的和（month，day）进行比较
# #zodia_day 是一个filter对象
# zodiac_day = filter(lambda x:x<(month,day),zodiac_days)

# zodiac_day = list(zodiac_day)
#
# #得到属相的脚标
# index = year % 12
# print(chinese_zodiac[index])
# #得到星座的脚标
# lens = len(zodiac_day)
# print(zodiac_name[lens])
#
# print("{y}年{m}月{d}日出生的人属相为{s},星座为{x}".format(y = year,m = month,d=day,s = chinese_zodiac[index],x=zodiac_name[lens]))

# 99乘法表
# 方法一
# a=-1
# b=4
# listA=[1,2,3,4,5,6,7,8,9]
# listB=[1,2,3,4,5,6,7,8,9]
# listC=[[],[],[],[],[],[],[],[],[]]
# for i in listA:
#     for j in listB:
#         listC[i-1].append(i*j)
# print("{a}*{b}={c}".format(a=a,b=b,c=listC[a-1][b-1]))
# # 方法二，没有完全列举
# input_nums = ((1,1),(1,2),(1,3),(1,4),(1,5),(1,6),(1,7),(1,8),(1,9),(2,1),(2,2),(2,3),(2,4),(2,5),(2,6),(2,7),(2,8),(2,9),(3,1),(3,2),(3,3),(3,4),(3,5),(3,6),(3,7),(3,7),(3,7),(3,8),(3,9),(4,1),(4,2),(4,3),(4,4),(4,5),(4,6),(4,6),(4,7),(4,8),(4,9),(5,1),(5,2),(5,3),(5,4),(5,5),(5,6),(5,7),(5,8),(5,9),(6,1),(6,2),(6,3),(6,4),(6,5),(6,6),(6,7),(6,8),(6,9),(7,1),(7,2),(7,3),(7,4),(7,5),(7,6),(7,7),(7,8),(7,9),(8,1),(8,2),(8,3),(8,4),(8,5),(8,6),(8,7),(8,8),(8,9),(9,1),(9,2),(9,3),(9,4),(9,5),(9,6),(9,7),(9,8),(9,9))
# multiply = list1 = ("1*1=1","1*2=2","1*3=3","1*4=4","1*5=5","1*6=6","1*7=7","1*8=8","1*9=9","2*1=2")
# (a,b) = (1,1)
# num = filter(lambda x : x < (a, b), input_nums)
# num = list(num)
# lens = len(num)
# print(multiply[lens])

# Lesson II

# 生成1-10之间的整数
# range() 左闭右开
# for i in range(1,11):
    # print(i)
#
# num=0
# while True:
#     num+=1
#     if num<=10:
#         print(num)
#     else:
#         break

# 根据年份格式化输出生肖，2018年是狗年
# chinese_zodiac = "猴鸡狗猪鼠牛虎兔龙蛇马羊"
# for year in range(2000,2019):
#     print("%d年是%s年"%(year,chinese_zodiac[year%12]))

# 不断接受输入，返回生肖
# while True:
#     year = input("Input year of birth：")

# chinese_zodiac = "猴鸡狗猪鼠牛虎兔龙蛇马羊"
# zodiac_name = ("摩羯座","水瓶座","双鱼座","白羊座","金牛座","双子座","巨蟹座","狮子座","处女座","天秤座","天蝎座","射手座")
# zodiac_days = ((1,20),(2,19),(3,21),(4,20),(5,21),(6,22),(7,23),(8,23),(9,23),(10,24),(11,23),(12,22))
# month=int(input("input month:"))
# day=int(input("input day:"))
# n=0
# while zodiac_days[n]<(month,day):
#     if month==12 and day>23:
#         break
#     n+=1
# print(zodiac_name[n])

# 字典 dict
# {"key":"value"}

# rectangle = {"width":10, "height":20}

# 可访问key的value
# print(rectangle["width"])

# 也可新增key:value
# rectangle["length"]=30
# print(rectangle)

# 问题一：生成1-10之间的整数
# 左闭右开
#range(1,11)
# 输出1-10之间的整数，for
# for n in range(1,11):
#     print(n)

#案例：格式化输出2000年到2018年的生肖，例如：2018年的生肖是狗
# chinese_zodiac = "猴鸡狗猪鼠牛虎兔龙蛇马羊"
#
# year = 2018
#
# print("{y}年".format(y = year))
# # 格式化输出方式
# print("%d年"%year)
#
# #index = year % 12
#
# for year in range(2000,2019):
#     print("%d年的生肖是%s"%(year,chinese_zodiac[year%12]))

# http://www.runoob.com/python/python-while-loop.html
#问题：不断的接收用户的输入年份，判断用户的属相
# while True:
#     # 接收用户的输入，返回用户输入的内容，为字符串
#     year = input("请输入您的年份：")
#     print(year)

#案例：用while循环输出5-10之间的整数
# break：跳出循环
# continue：跳出本次循环，继续下次循环
#
# import time
# num = 5
# while True:
#     num += 1
#     if num == 10:
#         continue
#     print(num)
#
#     time.sleep(1)


#案例：接收用户输入的年份，月份，日期，格式化输出：您的生肖为x，星座为xxx

# chinese_zodiac = "猴鸡狗猪鼠牛虎兔龙蛇马羊"
#
# zodiac_name = ("摩羯座","水瓶座","双鱼座","白羊座","金牛座","双子座","巨蟹座","狮子座","处女座","天秤座","天蝎座","射手座")
#
# zodiac_days = ((1,20),(2,19),(3,21),(4,20),(5,21),(6,22),(7,23),(8,23),(9,23),(10,24),(11,23),(12,22))
#
#
# year = int(input("请输入您的出生年份："))
# month = int(input("请输入您的出生月份："))
# day = int(input("请输入您的出生日期："))
#
# n = 0
# while zodiac_days[n] < (month,day):
#     #临界问题
#     if month == 12 and day > 23:
#         break
#     n += 1
#
# #得到脚标
# index = year % 12
#
# print("您的生肖为%s,星座为%s"%(chinese_zodiac[index],zodiac_name[n]))



#字典dict
# http://www.runoob.com/python/python-dictionary.html
# {"哈希值":"对象"}
# {"key":"value"}
#
# rectangle = {"width":80,"height":10}
#
# print(rectangle["width"])
#
# rectangle["length"] = 100
#
# print(rectangle)
#
# print(type(rectangle))

#阶段性大案例：记录用户的类型，输出：生肖为x的有x个;星座为xxx的有x个
#
# chinese_zodiac = "猴鸡狗猪鼠牛虎兔龙蛇马羊"
#
# zodiac_name = ("摩羯座","水瓶座","双鱼座","白羊座","金牛座","双子座","巨蟹座","狮子座","处女座","天秤座","天蝎座","射手座")
#
# zodiac_days = ((1,20),(2,19),(3,21),(4,20),(5,21),(6,22),(7,23),(8,23),(9,23),(10,24),(11,23),(12,22))
#
# year = int(input("请输入您的出生年份："))
# month = int(input("请输入您的出生月份："))
# day = int(input("请输入您的出生日期："))
#
# #通过分析，生肖名称为key，出现的次数为value
# cz_times = {}
# for cz_name in chinese_zodiac:
#     cz_times[cz_name] = 0
# print(cz_times)

# 230-234 用字典的推导式可简化为
# aDict={cz_name:0 for cz_name in chinese_zodiac}
# print(aDict)

# #星座名称为key，出现的次数为value
# z_times = {}
# for z_name in zodiac_name:
#     z_times[z_name] = 0
# print(z_times)

# #1989 8 14
# cz_times[chinese_zodiac[year%12]] += 1

# #星座日期的脚标
# n = 0
# while zodiac_days[n]< (month,day):
#     if month == 12 and day > 23:
#         break
#     n += 1

# z_times[zodiac_name[n]] += 1

# #通过keys函数可以得到dict中所有的key值

# for each_key in cz_times.keys():
#     print("生肖为%s的有%d个"%(each_key,cz_times[each_key]))

# for each_key in z_times.keys():
#     print("星座为%s的有%d个"%(each_key,z_times[each_key]))

# 使用if语句判断字符串的长度是否等于10，根据判断结果进行不同的输出
# str=input("input a string:")
# if len(str)==10:
#     print("str=10")
# else:
#     print("str!=10")

# 提示用户输入一个1 - 40之间的数字，使用if语句根据输入数字的大小进行判断，
# 如果输入的数字在1 - 10，11 - 20，21 - 30，31 - 40，分别进行不同的输出
# a=int(input("input an integer"))
# # if a>=1 and a <=10:
# #     print("1 - 10")
# # else:
# #     if a>10 and a <=20:
# #         print("11 - 20")

# 使用for语句输出1-100之间的所有偶数
# for even in range(1,101):
#     if even%3==0:
#         print(even)

# 使用while语句输出1-100之间能够被3整除的数字
# while a>0 and a<=100:
#     a=0
#     if a%3==0:
#         print(a)
#         a+=1

# 1. 定义一个字典，分别使用a、b、c、d作为字典的关键字，值为任意内容
# 2. 为该字典增加一个元素‘c':'cake'后，将字典输出到屏幕
# 3. 取出字典中关键字为d的值

# # 1-10中所有偶数的平方存入列表
# # 方法一
# aList=[]
# for i in range(1,11):
#     if i%2==0:
#         aList.append(i*i)
# print(aList)
#
# # 方法二：列表的推导式
# bList=[i*i for i in range(1,11) if(i%2==0)]
# print(bList)

# 文件内建函数和方法
# https://www.runoob.com/python3/python3-inputoutput.html
# open() 若有，打开；若无，创建
# read() 读取所有 readline() 读取第一行 readlines() 读取多行
# write()
# close()
# seek() 文件内光标移动

# # f.write(string) 将 string 写入到文件中
# file1=open("name.txt","w")
# file1.write("张三")
# file1.close()
#
# # f.read()读全部文件
# file2=open("name.txt","r")
# print(file2.read())
# file2.close()
#
# # "a."=append=追加
# file3=open("name.txt","a")
# file3.write("李四")
# file3.close()
#
# # f.readlines() 将返回该文件中包含的所有行。读取多行
# file4=open("name.txt","r")
# for line in file4.readline():
#     print(line)
# file4.close()
#
# # seek()改变文件中光标的位置。file.tell()返回从文件开头起到光标当前位置的字节数。
# file5=open("name.txt","r")
# print(file5.tell())
# # # 读取一个字符
# file5.read(1)
# print(file5.tell())
#
# # seek(arg1, arg2) arg1=移动几个字符，arg2=从什么位置移动
# # args: 0=从文件开头，1=从当前位置，2=从文件末尾
# file5.seek(2,0)
# print(file5.tell())
# file5.close()

# 创建一个文件，写入当前日期，读取文件的前4个字符后退出
# import datetime
# current_time = int(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
# file6=open("name.txt","w")
# file6.write(current_time)
# file6=open("name.txt","r")
# print(file6.read(4))
# file6.close()

# 模糊搜索，引入os
# 筛选出files文件夹中,文件名含area，后缀是gif/png的文件()
# import os
# path="C:/Users/tanglj31/PycharmProjects/project3-4/files"
# files=os.listdir(path)
# for a in files:
#     if("area" in a) and (a.endswith("gif") or a.endswith("png")):
#         print(a)
# for循环可简化为：
# print([filename for filename in os.listdir('C:\\Windows') if ("area" in a) and (a.endswith("gif") or a.endswith("png"))])


# 作业II
# 找到全部100内被13整除的整数
# print([i for i in range(100) if i%13==0])

# http://www.runoob.com/python/python-func-eval.html
# 编写一个简易的计算器，实现简单的加、减、乘、除运算，运行脚本后可重复输入和输出结果，
# 当用户输入指定退出符号（如：Q）时终止脚本运行。
# while True:
#     cal = input('Pls input calculation：')
#     if cal != 'Q':
#         try:
#             result = eval(cal)
#             print('Outcome：'+str(result))
#         except:
#             print('Input error！')
#     else:
#         break

# month1=[]
# month2=[]
# month3=[]
#
# file1=open("btc_price.txt","rb")
# for line in file1.readlines():
#     line=str(line)
#     if "2018-01-" in line:
#         month1.append(line)
#     elif "2018-02-" in line:
#         month2.append(line)
#     elif "2018-03-" in line:
#         month3.append(line)
# file1.close()
# sum1=0
# count1=0
# for item in month1:
#     sum1+=float(item.split("\\")[1][1:])
#     count1+=1
# avg1=sum1/count1
# print("Average price of January:%f"%avg1)
#
# sum2=0
# count2=0
# for item in month2:
#     sum2+=float(item.split("\\")[1][1:])
#     count2+=1
# avg2=sum2/count2
# print("Average price of Feburary:%f"%avg2)
#
# sum3=0
# count3=0
# for item in month3:
#     if count3==30:
#         sum3 += float(item.split("\\")[1][1:-1])
#     else:
#         sum3 += float(item.split("\\")[1][1:])
#     count3+=1
# avg3=sum3/count3
# print("Average price of March:%f"%avg3)
#
# file2=open("btc_price_season1.txt","w")
# file2.write("month1\t%f\n"%avg1)
# file2.write("month2\t%f\n"%avg2)
# file2.write("month3\t%f\n"%avg3)
# file2.close()

# file=open("btc_price.txt",'r')
# # month
# m=[1,2,3]
# # sum
# s=[0,0,0]
# # day
# d=[0,0,0]
# # 定位时间、价格
# for line in file.readlines():
#     date=line[:10]
#     price=line[-11:]
#     p=float(price)
#     if int(date[6])==m[0]:
#         # 每个月的sum和day分别累加
#         s[0]=s[0]+p
#         d[0]=d[0]+1
#     elif int(date[6])==m[1]:
#         s[1]=s[1]+p
#         d[1]=d[1]+1
#     elif int(date[6])==m[2]:
#         s[2]=s[2]+p
#         d[2]=d[2]+1
# file.close()
# file1=open("btc_price_season1.txt",'w')
# # 写入并换行
# file1.writelines("January average price:"+str(s[0]/d[0])+"\n")
# file1.writelines("February average price:"+str(s[1]/d[1])+"\n")
# file1.writelines("March average price:"+str(s[2]/d[2])+"\n")
# file1.close()

# Lesson III
# # 实现按照格式自动归类文件到对应的文件夹
# https://docs.python.org/2/library/shutil.html
# 1.如何移动文件
# 2.归类的规则？

#如何按照格式自动归类文件到对应的文件夹

#第一个问题：如何移动文件
#第二个问题：归类的规则是什么？

#回归昨天的os模块
# import os
#
# path = "./files"
# files = os.listdir(path)
# for f in files:
#     if("area" in f ) and (f.endswith("gif")):
#         print(f)

#移动文件，对不同的文件进行处理，打包，压缩（针对文件的增删改查） ---- shutil
#调用shutil.move()就可以移动文件
# for f in files:
#     if f.endswith(".xxx"):
#         move_to(someFolder)
#     if f.endswith(".xxx"):
#         move_to(someFolder)
#     if f.endswith(".xxx"):
#         move_to(someFolder)
#
# for f in files:
#     if folder not extist:
#         make folder
#         move file to folder
#     else:
#         move file to folder
# import os
# import shutil
#
# path = "./files"
# files = os.listdir(path)
# for f in files:
#     folder_name = f.split(".")[-1]
#     if not os.path.exists("./"+folder_name):
#
#         #创建同级目录
#         os.makedirs("./"+folder_name)
#         shutil.move(f, folder_name)
#     else:
#         shutil.move("./files/"+ f, folder_name)

#加你个同类型的文件归类，防御img和document文件夹中，删除其他文件夹
#删除文件夹 os.removedirs()
#import os
# path = "./"
# files = os.listdir(path)
# #创建出来img和document这两个文件夹
# os.makedirs(path+ "img")
# os.makedirs(path+ "document")
#
# #将需要的筛选的文件夹名称，写入list中
# img_suffix = ["jpg", "png", "gif"]
# doc_suffix = ["doc", "docx", "md", "ppt", "pptx"]
#
# #"./img/xx.jpg"
# #"./img/xx.jpg"
#
# for i in img_suffix:
#     #./jpj
#     currne_path = path + i
#     files = os.listdir(currne_path)
#     print(files)
#     for f in files:
#         #./jpg/1.jpg    ./img
#         shutil.move(currne_path+ "/" +f, path+ "img")
#     os.remove(currne_path)
#
# for d in doc_suffix:
#     #./doc
#     currne_path = path + d
#     files = os.listdir(currne_path)
#     for f in files:
#         #./jpg/1.jpg
#         shutil.move(currne_path+ "/"+ f,path+ "document")
#     os.remove(currne_path)

# # Lesson IV
# file1 = open("name.txt", encoding='utf-8')
# data1 = file1.read()
# print(data1.split("|"))
#
# file2 = open("weapon.txt", encoding='utf-8')
# i =1
# for line in file2.readlines():
#     if i %2 == 1:
#         print(line.split("\n"))
#     i += 1
#
# #读入sanguo
# file3 = open("sanguo.txt", encoding="GB18030")
# data3 = file3.read()
# print(data3.replace("\n", ""))
#
# #函数
# #function add（arg1, arg2){
# #         return
# #}
# def show_conten(filename):
#     print(open(filename,encoding='utf-8').read())
#
# show_conten("name.txt")

#函数的可变长参数"*"
# print("abc", end="\n\n")
# print("abc")
# def show(a,b,c):
#     print("a = %s"%a)
#     print("b = %s"%b)
#     print("c = %s"%c)
# show(1,c=2,b=3)
#
# def howlong(first,*other):
#     print(1+len(other))
#     print(*other)
# howlong(1,2,3)

# import re
#
# #从sanguo.txt中发现英雄出现的次数
# def find_item(hero):
#     with open("sanguo.txt",encoding="GB18030") as f:
#         data = f.read().replace("\n","")
#         #re.findall()名字每出现一次，在list中增加一次
#         name_times = re.findall(hero,data)
#
#     return len(name_times)
#
#
# #定义一个空字典
# name_dict = {}
# with open("name.txt",encoding="utf-8") as f:
#     for name in f:
#         names = name.split("|")
#         # key(诸葛亮)，value(100次)
#         for n in names:
#             name_times = find_item(n)
#             name_dict[n] = name_times
#
#
# name_sorted = sorted(name_dict.items(),key=lambda item:item[1],reverse=False)
# print(name_sorted)
# print(name_sorted[0:10])

# # 1. 创建一个函数，用于接收用户输入的数字，并计算用户输入数字的和
# def add():
#     two_num=input("input 2 nums, separate with space")
#     num1,*_,num2=list(two_num)
#     print(int(num1)+int(num2))
#
# # 2. 创建一个函数，传入n个整数，返回其中最大的数和最小的数
# def func1(*nums):
#     print(max(list(nums)))
#     print(min(list(nums)))
# func1(1,2,3,45,61,109)
#
# # 3. 创建一个函数，传入一个参数n，返回n的阶乘
# # 递归调用
# def fact(num3):
#     if num3==0 or num3==1:
#         return 1
#     else:
#         return (num3*fact(num3-1))
# # ()里填数字
# print(fact())

# # 迭代器和生成器(迭代器的一种)
# list1=[1,2,3,4]
# # iter() next()
# it=iter(list1)
# print(it)
# print(next(it))
# print(next(it))
# print(next(it))
#
# # 写一个函数floatRange()，让第三个参数是float
# def floatRange(start,stop,step):
#     x=start
#     if start<stop:
#         while x<stop:
#             # 一次性输出
#             # print(x)
#             yield x
#             x+=step

# #循环法
# i=0
# for rooster in range(5,101,5):   # 公鸡
#     for hen in range(3,101 - rooster,3):  #母鸡
#         for chicken in range(1,101 - rooster - hen): #小鸡
#             if rooster // 5 + hen // 3 + chicken * 3 == 100 and rooster + hen + chicken == 100:
#                 i+=1
#                 print("%d roosteres\t%d hens\t%d chickens" % (rooster // 5, hen // 3, chicken * 3))
# print("method 1: %s ways to purchase"%i)
# #列表推导式
# rooster_MaxNum,hen_MaxNum,chicken_MaxNum=range(20)[1:],range(34)[1:],range(int(300))[1:]
# items=[(rooster,hen,chicken)for rooster in rooster_MaxNum for hen in  hen_MaxNum[1:] for chicken in  chicken_MaxNum[1:]
# if int(rooster*5+hen*3+chicken/3)==100 and chicken%3==0 and rooster+hen+chicken==100]
# print('%-5s%8s%10s' % ('rooster','hen','chicken'))
# for c in items:
#    print('%-5s%10s%15s' % c)
# print("method 2: %s ways to purchase"%str(len(items)))

# Lesson V
import csv
# *=all
from wxpy import *
# def readinfo():
#     file1=open("./sample.csv", "r", encoding="utf-8")
#     reader=csv.DictReader(file1)
    # list1=[]
    # for i in reader:
    #     list1.append(i)
    # return list1
    # 列表推导式
#     return[i for i in reader]
# def postinfo():
#     template="{name} please attend {} at {}".format(name=info["姓名"], )

# 微信群发消息：读取csv文件中的信息，给csv文件中的好友发送定制消息
#
# import csv
# from wxpy import *
# import time
#
# # 读取信息
# def read_info():
#     file1 = open("./sample.csv", "r", encoding="utf-8")
#     reader = csv.DictReader(file1)
#     # list1 = []
#     # for i in reader:
#     #     list1.append(i)
#     #
#     # return list1
#     #列表的推导式
#     return [i for i in reader]
#
# # 制作消息模板
# # xx同学请于xx事件参加xx课程，地址是xxx，收到请回复，谢谢
# def make_info(row_info):
#     template = "{n}-同学请于{t}时间参加{c}课程，地址是{a}，收到请回复，谢谢"
#     # template_info = []
#     # for info in row_info:
#     #     template = "{name}同学请于{t}时间参加{c}课程，地址是{a}，收到请回复，谢谢"
#     #     template_info.append(template)
#     # return template_info
#
#     return [template.format(n = info["姓名"],
#                             t = info["上课时间"],
#                             c=info["课程"],
#                             a = info["上课地址"]) for info in row_info]
#
# #发送消息
# def send_info(msg_list):
#     #初始化
#     bot = Bot()
#     for msg in msg_list:
#         friend_name = msg.split("-")[0] # str
#         f = bot.friends().search(friend_name) # list类型
#
#         if len(f) == 1:
#             f[0].send(msg)
#         else:
#             print(friend_name)
#             print("请检查你的好友名称")
#
#     time.sleep(3)
#
# row_info = read_info()
# msg_list = make_info(row_info)
# send_info(msg_list)
import requests
from bs4 import BeautifulSoup
# 爬虫 I --requests

# api https://api.github.com/repos/channelcat/sanic
# web_page https://github.com/channelcat/sanic

# import requests
# import webbrowser
# import time
# api="https://api.github.com/repos/channelcat/sanic"
# webpage="https://github.com/channelcat/sanic"
# all_info=requests.get(api)
# # web上用来传输数据的格式：json（多数，字典形式），xml（少数，html形式）
# dict_info=all_info.json()
# # 得到当前项目的最新更新时间
# current_time=dict_info["updated_at"]
# while True:
#     if():
#         pass
#     else:
#         webbrowser.open(web_page)

# 爬虫 II - BeautifulSoup4
from bs4 import BeautifulSoup
import requests
# step 1: 解析网页
# html:需要解析的本地网页地址
# lxml:解析器，此外还有html5lib，html.parser
#
# soup=BeautifulSoup(html,"lxml")

# step 2: 描述需要爬取的网页/图片等的位置
#f12, 右键元素, copy selector/copy xpath
# soup.select()

# step 3: 从标签中获取所需信息

# # 从API获取数据
# # import requests
# # import webbrowser
# # import time
# #
# # web_api = ""
# # web_url = ""
# #
# # #第一步
# # all_info = requests.get(web_api)
# # dict_info = all_info.json()
# #
# # current_time = dict_info["updated_time"]
# #
# # last_time = None
# #
# # while True:
# #     if not last_time:
# #         last_time = current_time
# #     if last_time < current_time:
# #         webbrowser.open()
# #
# #     time.sleep(300)
#
#
#
# # 从本地网页获取数据
# # 安装第三方库的命令：pip install 包名称
# # 卸载第三方库的命令：pip uninstall 包名称
# # 查看用pip安装了哪些库：pip list
#
# # 第一步：使用BeautifulSoup去解析网页
# # html是需要解析的本地网页地址
# # lxml是解析器(需要安装)，除此之外还有html5lib(需要使用pip安装)
# # html.parser(无需安装)
# #Soup = BeautifulSoup(html,"lxml")
#
# # 第二步：描述需要爬取的东西的位置
#
# #Soup.select()
# # 第三步：从标签中获取到你需要的信息
#
# from bs4 import BeautifulSoup
#
# goods_info = []
#
# with open("Apple/index.html","r",encoding='utf-8') as web_data:
#     Soup = BeautifulSoup(web_data,"lxml")
#     titles = Soup.select("body > div.content > div > h3")
#     images = Soup.select("body > div.content > div > img")
#     descriptions = Soup.select("body > div.content > div > p:nth-of-type(1)")
#     prices = Soup.select("body > div.content > div > p > span")
#
#
# # for price in prices:
# # #     print(price.get_text().split(" ")[-1])
# # #
# # # for title in titles:
# # #     print(title.get_text())
# # #
# # # for description in descriptions:
# # #     print(description.get_text())
# # #
# # # for image in images:
# # #     print(image.get("src"))
#
# # 多个for循环同时进行
# for price,title,description,image in zip(prices,titles,descriptions,images):
#     data = {
#         "image":image.get("src"),
#         "price":price.get_text().split(" ")[-1],
#         "description":description.get_text(),
#         "title":title.get_text()
#     }
#
#     goods_info.append(data)
#
# for good_info in goods_info:
#     if float(good_info["price"])>10000:
#         print(good_info)
#
# '''
# CSS Selector   是谁，在哪，长什么模样
#     title:        body > div.content > div:nth-child(1) > h3
#     img:          body > div.content > div:nth-child(1) > img
#     descriptions: body > div.content > div:nth-child(1) > p:nth-child(3)
#     price:        body > div.content > div:nth-child(1) > p:nth-child(4) > span
# '''
#
# '''
# XPath          是谁，在哪
#     title:     /html/body/div[3]/div[1]/h3
# '''

# web = requests.get("https://cn.bing.com/search?q=National%20US%20Senate%20Results&p1=%5BElection.pole_requery+state%3D%22%22+office%3D%22senate%22%5D&FORM=BESBTB&ensearch=1")
# web.encoding = 'utf-8'
# soup = BeautifulSoup(web.text, "lxml")
# titles=soup.select("#b_results > li")
# for title in titles:
#     print(title.get_text())

# tripadvisor

# # 获取多个页面，实现跨页面搜索
# urls = ["https://www.tripadvisor.cn/Attractions-g60763-Activities-oa{}-New_York_City_New_York.html#FILTERED_LIST".format(str(i)) for i in range(30,1230,30)]
# # url="https://www.tripadvisor.cn/Attractions-g60763-Activities-New_York_City_New_York.html"
# for url in urls:
#     web_data=requests.get(url)
#     soup=BeautifulSoup(web_data.text,"lxml")
#     # 把copy selector得来的第一个#删掉
#     titles=soup.select("div.attraction_clarity_cell > div > div > div.listing_info > div.listing_title > a")
#     imgs=soup.select("img[width='180']")
#     for title in titles:
#         print(title.get_text())
#     for img in imgs:
#         print(img)
#
# import requests
# from bs4 import BeautifulSoup
# import time
#
# urls = ["https://www.tripadvisor.cn/Attractions-g60763-Activities-oa{}-New_York_City_New_York.html#FILTERED_LIST".format(str(i)) for i in range(30,1230,30)]
#
# def get_attractions(url,data=None):
#     web_data = requests.get(url)
#     time.sleep(4)
#     soup  = BeautifulSoup(web_data.text,"lxml")
#     titles = soup.select("div.attraction_element > div.attraction_clarity_cell > div > div > div.listing_info > div.listing_title > a")
#     imgs = soup.select("img[width='180']")
#
#     print(titles)
#
#     if data == None:
#         for title,img in zip(titles,imgs):
#             data = {
#                 "title":title.get_text(),
#                 "img":img.get("src")
#             }
#             print(data)
#
# n = 0
# for url in urls:
#     n += 1
#     print(n)
#     get_attractions(url)
#
# from selenium import webdriver
# import time
# url = 'https://weibo.com/5869525717/G2VASlH1o?from=page_1005055869525717_profile&wvr=6&mod=weibotime&type=comment'
# driver = webdriver.Chrome()
# driver.start_client()
# return driver
#
# from selenium import webdriver
# import time
#
#
# # 用pip安装selenium
# from selenium import webdriver
# import time
# #进博会话题第一条微博
# url = "http://live.weibo.com/show?id=1042152:30f6080b0d359eccedf11455d0099b9f"
# driver = webdriver.Chrome(executable_path="./chromedriver")
# driver.start_client()
# driver.get(url)
# sel = "div.WB_from.S_txt2.clearfix > span.WB_praishare.W_fr > a > span"
# elems = driver.find_elements_by_css_selector(sel)
# print([int(el.text.split(" ")[-1]) for el in elems])
#
# # def start_chrome():
# #     driver = webdriver.Chrome(executable_path="./chromedriver")
# #     driver.start_client()
# #     return driver
# #
# # def get_info():
# #     sel = "div.WB_from.S_txt2.clearfix > span.WB_praishare.W_fr > a > span"
# #     elems = driver.find_elements_by_css_selector(sel)
# #     print(elems)
# #     return [int(el.text.split(" ")[-1]) for el in elems]
# #
# # while True:
# #     driver = start_chrome()
# #     driver.get(url)
# #     time.sleep(6)
# #     info = get_info()
# #     # [123,456,789]
# #     rep, comm, like = info
# #
# #     if rep > 90000:
# #         print('你关注的微博转发量已经过 '+str(rep))
# #         print(f'你喜欢的微博转发量已经超过{rep}') # f-string
# #         break
# #     else:
# #         print('Not happening')
# #
# #     time.sleep(1200)
# #
# # print("完成")

from selenium import webdriver
import time
# 进博会话题讨论数超过1.2万
url = "https://s.weibo.com/weibo/%23%E8%BF%9B%E5%8D%9A%E4%BC%9A%23"
driver=webdriver.Chrome()
#
# def get_driver():
#     driver = webdriver.Chrome(executable_path="./chromedriver")
#     driver.start_client()
#     return driver

def find_elements():
    driver.get(url)
    css_selector = "#pl_topic_header > div.card-topic-a > div > div.total > span:nth-child(2)"
    nums = driver.find_element_by_css_selector(css_selector)
    return nums.text.replace("讨论","")

while True:
    # driver = get_driver()
    nums = find_elements()
    if nums > "1.2万":
        print("进博会讨论数超过1.2万")
    time.sleep(3000)
    print("Done")