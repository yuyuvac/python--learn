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