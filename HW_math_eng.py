math_score = float(input('請輸入你的數學成績: '))
english_score = float(input('請輸入你的英文成績: '))
if math_score >= 90 and english_score >= 90:
            print('有獎勵')
elif math_score < 60 and english_score < 60:
            print('要處罰')
elif math_score < 60 and english_score >= 60:
            print('再加油')
elif math_score >= 60 and english_score < 60:
            print('再加油')
else:
            print('還可以')
