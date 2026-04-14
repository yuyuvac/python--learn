"""
print("hello world")
print("hello world")
"""
"""
name = "传智播客"
stock_price = 19.99
stock_code = "003032"
stock_price_daily_growth_factor = 1.2
growth_days = 7
print(f"公司:{name},股票代码:{stock_code},当前股价:{stock_price}")
print("每日增长指数%.2f，""经过%d天后的价格为%.2f"%(stock_price_daily_growth_factor,
growth_days,
stock_price*1.2*1.2*1.2*1.2*1.2*1.2*1.2))
"""
"""
user_name = input("请输入用户名")
user_type = input("请输入用户类型")
print(f"您好{user_name},尊贵的{user_type}用户,欢迎你的光临")
"""
"""
import random
num = random.randint (1,10)
print("欢迎来到猜数字游戏，你有三次机会")
guess = int(input())
if guess == num:
    print("恭喜你你猜中了")
else:
    if guess > num:
        print("你猜的数字大了")
    else :
        print("你猜的数字小了")
    print("你还有两次机会") 
    guess = int(input())
    if guess == num:
        print("恭喜你猜中了") 
    else:
        if guess> num :
            print("你猜的数字大了")
        else :
            print("你猜的数字小了")
        print("你还有一次机会")
        guess = int(input())
        if guess == num:
            print("恭喜你猜中了")
        else:
            if guess > num:
                print("猜的大了")
            else:
                print("猜的小了")
            print(f"你失败了正确数字是{num}，选择重新开始")
"""
"""
num1 = 0
num2 = 1
while num2 <=100:
    num1 = num1 +num2
    num2 = num2+1
print("num1=%d"%num1)
"""
"""
from operator import truediv
import random
num= random .randint(1,100)
flag = True
count = 0
print("欢迎来到猜数字游戏")
while flag :
    guess = int(input())
    count= count+1
    if guess == num:
        print("恭喜你猜对了")
        flag= False
    else:
        if guess > num:
            print("猜的大了")
        else:
            print("猜的小了")
print("你一共猜了%d"%count)
"""
"""
i=1
while i<=9:
    j=i
    while j<=9:
        print(f"{i}*{j}={i*j}",end='\t')
        j = j+1
    print("\t")
    i=i+1
"""
"""
name = "itheima is a brand of itcast"
count=0
for letter in name:
    print(f"{letter}",end='')
    if letter=="a":
        count=count+1
print("")
print(f"有{count}个字母a")
"""
"""
count=0
for num in range(1,100):
    if num%2 ==0 :
        count=count+1
print(f"一共有{count}个偶数")
"""
"""
for i in range(1,10):
    for j in range(i,10):
        print(f"{i}*{j}={i*j}\t",end='')
    print("")
    """
"""
import random
money=10000
for i  in range(1,21):
    num = random.randint(1,10)
    if num>=5:
        money=money-1000
        print(f"员工{i},绩效是{num},分得1000,账户余额剩余{money}")
        if money ==0:
            print(f"工资发完了")
            break
        else:
            continue
    else:
        print(f"员工{i}绩效是{num}小于5,不发工资")
        continue
        if i==20:
            break
"""
"""
def hesuan() :
    print("我是黑马程序员")
    print("请在七十二小时内出试你的核算")

hesuan()
"""
"""
num=True
money= 5000000
def select():
    print("=========查询余额========")
    print(f"{name},你好，你目前剩余:{money}元")
def cunqian():
    i = int(input("请输入你要存放的金额："))
    print("=========存款========")
    print(f"{name},你好，你存款{i}元成功")
    print(f"{name},你好，你目前剩余:{money+i}元")
def quqian():
    i=int(input("请输入你要取出的金额："))
    print("=========取款========")
    print(f"{name},你好，你取款{i}元成功")
    print(f"{name},你好，你目前剩余:{money-i}元")
def out():
    global num 
    num= False
    return num
def func(x):
    if x==1:
        select()
        return money
    elif x==2:
        cunqian()
    elif x==3:
        quqian()
    elif x==4:
        out()
def word():
    print("=========主菜单========")
    global name
    name = input("请输入姓名：")
    print(f"{name},你好.欢迎来到黑马银行ATM,请选择操作:")
    print("查询余额\t[输入1]\t")
    print("存款\t\t[输入2]\t")
    print("取款\t\t[输入3]\t")
    print("退出\t\t[输入4]\t")
while num:       
    word();
    func(int(input("请输入您的选择："))) 
"""
"""
agelist=[21,25,21,23,22,20]
agelist.append(31)
print(f"追加年龄后的列表{agelist}")
list=[29,33,30]
agelist.extend(list)
print(f"追加新列表后的列表{agelist}")
letter =agelist.pop(0)
print(f"取出第一个元素后的列表：{agelist}，取出的元素是{letter}")
last =agelist.pop(-1)
print(f"取出最后一个元素后的列表：{agelist}。取出的元素是{last}")
location=agelist.index(31)
print(f"这是元素31的下标是{location}")
"""
"""
list = [1,2,3,4,5,6,7,8,9,10]
list2 = [1,2,3,4,5,6,7,8,9,10]
list3 =[]
index = 0
index2= 0
while index<len(list) :
    if list[index]%2==0:
        continue
    else :
        list.pop(index)
    index=index+1
print(f"只有偶数的列表是：{list}")
for element in list2:
    if element%2 == 0:
        list3.append(element)
print(f"只有偶数的列表是：{list3}")
"""
"""
yuanzu=("周杰轮",11,["footall","music"])
a=yuanzu.index(11)
print(f"学生年龄所在的下标位置是：{a}")
print(f"学生的名字是：{yuanzu[0]}")
del yuanzu[2][0]
print(f"删除football后的元祖:{yuanzu}")
yuanzu[2].append("coding")
print(f"增加元素后的元祖：{yuanzu}")
"""
"""
strlist="itheima itcast boxuegu"
count=strlist.count("it")
print(f"字符串内有{count}个it字符")
newstrlist=strlist.replace("itheima itcast boxuegu","itheima丨itcast丨boxuegu")
print(f"将空格改为丨的新字符串：{newstrlist}")
list=newstrlist.split("丨")
print(f"用丨分隔后的字符串得到的列表：{list}")
"""
str="万过薪月.员序程马黑来,nohtyp学"
list=[]
i=-10
count=0
while count<5:
    list.append(str[i])
    i=i-1
    count=count+1
print(f"列表list：{list}")
str2=str[9:4:-1]
print(f"str2:{str2}")