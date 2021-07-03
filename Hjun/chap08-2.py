# 141
리스트 = [100,200,300]
for i in 리스트:
    print(i+10)

# 142
리스트 = ["김밥", "라면", "튀김"]
for i in 리스트:
    print(f'오늘의 메뉴: {i}')

# 143
리스트 = ["SK하이닉스", "삼성전자", "LG전자"]
for i in 리스트:
    print(len(i))

# 144
리스트 = ['dog', 'cat', 'parrot']
for i in 리스트:
    print(i, len(i))

# 145
for i in 리스트:
    print(i[0])

# 146
리스트 = [1,2,3]
for i in 리스트:
    print(f'{리스트[-1]} x {i}')

# 147
리스트 = [1,2,3]
for i in 리스트:
    print(f'{리스트[-1]} x {i} = {리스트[-1]*i}')

# 148
리스트 = ["가", "나", "다", "라"]
for i in 리스트:
    if i == "가":
        continue
    else:
        print(i)

# 해설지 풀이
리스트 = 리스트[1:]
for i in 리스트:
    print(i)

# 149
리스트 = ["가", "나", "다", "라"]
for i in 리스트[0::2]:
    print(i)

# 150
for i in 리스트[::-1]:
    print(i)

# 후기
# 아직까지는 쉬운데 무엇보다 문제가 마음가짐이다.
# 금방하는걸 안하다가 이렇게 되다니... 매일매일 열심히 해야겠다.