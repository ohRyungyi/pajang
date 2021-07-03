# 131 -
과일 = ["사과", "귤", "수박"]
for 변수 in 과일:
    print(변수)
# 사과
# 귤
# 수박
# 출력

# 132 - 
과일 = ["사과", "귤", "수박"]
for 변수 in 과일:
  print("#####")
# #####
# #####
# #####

# 133 - 
# for 변수 in ["A", "B", "C"]:
#   print(변수)
print('A')
print('B')
print('C')

# 134 - 
# for 변수 in ["A", "B", "C"]:
#   print("출력:", 변수)
print('출력:',"A")
print('출력:','B')
print('출력:','C')

# 135 - 
# for 변수 in ["A", "B", "C"]:
#   b = 변수.lower()
#   print("변환:", b)
print('변환:','a')
print('변환:','b')
print('변환:','c')

# 136 - 
# 변수 = 10
# print(변수)
# 변수 = 20
# print(변수)
# 변수 = 30
# print(변수)
for i in [10, 20, 30]:
    print(i)

# 137 - 
# print(10)
# print(20)
# print(30)
for i in [10, 20, 30]:
    print(i)

# 138 - 
# print(10)
# print("-------")
# print(20)
# print("-------")
# print(30)
# print("-------")
for i in [10, 20, 30]:
    print(i, "-------", sep="\n")

# 139 - 
# print("++++")
# print(10)
# print(20)
# print(30)
for i in [0, 10, 20, 30]:
    if i ==0:
        print("++++")
    else:
        print(i)

# 140 - 
# print("-------")
# print("-------")
# print("-------")
# print("-------")
for i in range(4):
    print("-------")

# 141 - 
리스트 = [100, 200, 300]
for i in 리스트:
    print(i+10)

# 142 - 
리스트 = ["김밥", "라면", "튀김"]
for menu in 리스트:
    print('오늘의 메뉴:',menu)

# 143 - 
리스트 = ["SK하이닉스", "삼성전자", "LG전자"]
for i in 리스트:
    print(len(i))

# 144 - 
리스트 = ['dog', 'cat', 'parrot']
for item in 리스트:
    print(item, len(item))

# 145 - 
리스트 = ['dog', 'cat', 'parrot']
for item in 리스트:
    print(item[0])

# 146 - 
리스트 = [1, 2, 3]
for item in 리스트:
    print("3 x %d" %item)

# 147 - 
리스트 = [1, 2, 3]
for item in 리스트:
    print("3 x %d = %d" %(item, item*3))

# 148 - 
리스트 = ["가", "나", "다", "라"]
for i in 리스트[1:]:
    print(i)

# 149 - 
리스트 = ["가", "나", "다", "라"]
for i in 리스트[::2]:
    print(i)

# 150 - 
리스트 = ["가", "나", "다", "라"]
for i in 리스트[::-1]:
    print(i)

# 151 - 
리스트 = [3, -20, -3, 44]
for i in 리스트:
    if i<0:
        print(i)

# 152 - 
리스트 = [3, 100, 23, 44]
for i in 리스트:
    if i%3 == 0:
        print(i)

# 153 - 
리스트 = [13, 21, 12, 14, 30, 18]
for i in 리스트:
    if i<20 and i%3 ==0:
        print(i)

# 154 - 
리스트 = ["I", "study", "python", "language", "!"]
for i in 리스트:
    if len(i)>=3:
        print(i)

# 155 - 
리스트 = ["A", "b", "c", "D"]
for i in 리스트:
    if i.isupper():
        print(i)

# 156 - 
리스트 = ["A", "b", "c", "D"]
for i in 리스트:
    if i.islower():
        print(i)

# 157 - 
리스트 = ['dog', 'cat', 'parrot']
for item in 리스트:
    # print(item.capitalize())
    # 답지 풀이
    print(item[0].upper(), item[1:], sep="")

# 158 -
리스트 = ['hello.py', 'ex01.py', 'intro.hwp']
for file in 리스트:
    print(file.split('.')[0])

# 159 - 
리스트 = ['intra.h', 'intra.c', 'define.h', 'run.py']
for file in 리스트:
    if file.split('.')[-1] == 'h':
        print(file)

# 160 -
리스트 = ['intra.h', 'intra.c', 'define.h', 'run.py']
for file in 리스트:
    if file.split('.')[-1] == "h" or file.split('.')[-1] == "c":
        print(file)

# 160 - 
