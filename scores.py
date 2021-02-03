scores = []

max=0
low=101
sum=0

p=int(input('請問班上有幾人? '))

for i in range (p):

    s=int(input('請輸入分數: '))
    scores.append(s)
    print(scores)

    sum=sum + (scores[i])

    if s>max:
        max=s

    elif s<low:
        low=s

all=sum/p
print(max,low,all)

    
