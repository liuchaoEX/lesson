import random
count=3
answer=random.randint(1,10)

while counts>0:
    temp=input("不妨猜一下我现在心里想的时哪个数字？")
    guess=int(temp)
    if guess==answer:
        print("你是我心里的蛔虫吗？")
        print("哼！猜中了也没奖励！")
        break
    else:
        if guess<answer:
            print("小了~")
        else:
            print("大了~")
        counts=count-1
print("游戏结束，不玩了^_^")