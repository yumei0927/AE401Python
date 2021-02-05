x = {}
while True: 
    print('功能=>')
    print('1. 輸入入住者資料')
    print('2. 查詢')
    print('3. 體溫')
    print('4. 離開系統')

    y = int(input('請輸入欲執行的功能代號: '))

    if (y == 1):
        b=0
        print('')
        k = []
        n = str(input('入住者姓名: '))
        r = int(input('入住者房號: '))
        i = str(input('入住日期: '))
        o = str(input('應退房日期: '))
        p = int(input('入住者電話號碼: '))
        k.append(r)
        k.append(i)
        k.append(o)
        k.append(p)
        k.append(b)
        x[n] = k
        print('')
        print('姓名:',n)
        print('房號:',r)
        print('入住日期:',i)
        print('應退房日期:',o)
        print('入住者電話號碼: ',p)
        print('')

    elif (y == 2):
        print('')
        for key in x.keys():
            print('入住者姓名: ',key)
        print('')
        f = str(input('請輸入入住者姓名: '))
        while (f in x) == False:
            f = str(input('請重新輸入: '))
        else:
            print('')
            print(f,'=>',x[f])
            print('')

    elif (y == 3):
        print('')
        for key in x.keys():
            print('入住者姓名: ',key)
        print('')
        g = str(input('請輸入入住者姓名: '))
        while (g in x) == False:
            g = str(input('請重新輸入: '))
        print('')
        q = x[g][3]
        print('他的電話號碼是',q)
        print('')
        b = float(input('請輸入他的體溫:'))
        x[g][4] = b
        print('')
        if (b > 37.5):
            print('體溫過高')
        print('')
    elif (y == 4):
        break
    else:
        print('wrong input')
        
