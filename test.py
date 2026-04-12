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
    
