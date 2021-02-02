import random

high=int(input('請輸入最大上限: '))
low=int(input('請輸入最小下限: '))
number=int(input('請問你想要幾次機會: '))

num=random.randint(low,high)

for i in range(number) :
    x=int(input('猜猜看'))
    if ( x == num):
        print('你太厲害了')
        break        
    if (x < low or x > high) :
        print('不符合所輸入的數字大小，你還有',number - (i+1),'次機會')
    elif ( x < num ):
        print('大一點，你還有',number - (i+1),'次機會')
    else:
        print('小一點，你還有',number - (i+1),'次機會')
        


