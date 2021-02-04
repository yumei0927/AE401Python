x = {}
a = 0
a_m = 0
all_m = 0
all_a = 0
while True: 
    print('功能=>')
    print('1. 設定')
    print('2. 進貨')
    print('3. 出貨')
    print('4. 營業額統計')
    print('5. 庫存統計')
    print('6. 離開系統')

    y = int(input('請輸入欲執行的功能代號: '))
            

    if (y == 1) :
        print('')
        a = int(input('有幾顆蘋果: '))
        a_m = int(input('一顆多少錢: '))
        print('')
        print('目前有',a,'顆蘋果')
        print('一顆',a_m,'元')
        print('')
        
    elif (y == 2):
        print('')
        a_c = int(input('進多少顆蘋果: '))
        print('')
        print('進',a_c,'顆蘋果')
        a = a + a_c
        print('目前有',a,'顆蘋果')
        print('')

    elif (y == 3):
        print('')
        a_o = int(input('賣出多少顆蘋果: '))
        print('')
        print('賣出',a_o,'顆蘋果')
        m_in = a_m * a_o
        print('應付',m_in)
        a = a - a_o
        print('目前有',a,'顆蘋果')
        x[a_o] = m_in
        all_m = all_m + m_in
        all_a = all_a + a_o
        print('')

    elif (y == 4):
        print('')
        print(len(x),'筆交易')
        for key,value in x.items():
            print(key,'顆',value,'元')
        print('總收入: ',all_m)
        print('共賣出',all_a,'顆蘋果')
        print('')

    elif (y == 5):
        print('')
        print('目前剩',a,'顆蘋果')
        print('')

    else:
        all_m = str(all_m)
        z = ('總收入: ' + all_m + '\n')
        all_a = str(all_a)
        q = ('共賣出' + all_a + '顆蘋果\n')
        a = str(a)
        v = ('目前剩' + a + '顆蘋果\n')
        
        fo = open('蘋果店.txt','w')

        fo.write(z)
        fo.write(q)
        fo.write(v)
        
        fo.close()
        break
            

  
        
        

