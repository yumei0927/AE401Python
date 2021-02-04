classroom = []
score = []
max = 0
low = 101
stu=int(input('請問有多少學生? '))

for i in range(stu):
    n=str(input('請輸入名字: '))
    a=int(input('請輸入年齡: '))
    s=int(input('請輸入分數: '))
    student = []
    student.append(n)
    student.append(a)
    student.append(s)
    score.append(s)
    classroom.append(student)
    print(classroom)

    if (s > max):
        max = s
    elif (s < low):
        low = s

max_num=score.index(max)
low_num=score.index(low)
print('最高分是',classroom[max_num][0],classroom[max_num][2])
print('最低分是',classroom[low_num][0],classroom[low_num][2])

