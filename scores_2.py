count=int(input('請輸入學生人數'))
namelist = []
agelist = []
scorelist = []

for i in range(count):
    namelist.append(input('名字'))
    agelist.append(int(input('年齡')))
    scorelist.append(int(input('成績')))

print('最高分的是', namelist[scorelist.index(max(scorelist))], ' 分數是 ', max(scorelist))
print('最低分的是', namelist[scorelist.index(min(scorelist))], ' 分數是 ', min(scorelist))

avg = sum(agelist)/count
minagediff = []
for i in range(count):
    minagediff.append(abs(agelist[i] - avg))
print('年齡距離平均值最近的是', namelist[minagediff.index(min(minagediff))])
