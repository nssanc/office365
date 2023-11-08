# 这是一个猜数字的游戏
import random # 导入随机数模块

# 生成一个1到100之间的随机整数
answer = random.randint(1, 100)

# 初始化猜测的次数为0
count = 0

# 循环猜测，直到猜对为止
while True:
    # 让用户输入一个猜测的数字
    guess = int(input("请输入一个1到100之间的整数："))

    # 增加猜测的次数
    count += 1

    # 判断用户的猜测是否正确
    if guess == answer:
        # 猜对了，结束游戏并显示猜测的次数
        print("恭喜你，猜对了！")
        print("你一共猜了{}次。".format(count))
        break # 跳出循环
    elif guess > answer:
        # 猜大了，提示用户并继续猜测
        print("猜大了，再试一次吧。")
    else:
        # 猜小了，提示用户并继续猜测
        print("猜小了，再试一次吧。")
