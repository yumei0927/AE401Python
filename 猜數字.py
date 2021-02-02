import random
num=random.randint(1,10)
x=int(input('猜猜看1~10哪個會被挑中: '))
if x==num:
    print('太厲害了!')

else:
    print('你猜錯了，答案是',num)
