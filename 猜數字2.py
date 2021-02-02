import random
y=0
num=random.randint(1,10)
while y < 2:
    x=int(input('猜猜看1~10哪個會被挑中'))
    if x == num:
        print('太厲害了!')
        y=y+2
    elif x > num:
        print('你猜錯了，太大了')
    else:
        print('你猜錯了，太小了')
       
        
        
