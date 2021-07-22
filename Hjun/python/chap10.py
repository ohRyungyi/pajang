# 241
import datetime
now = datetime.datetime.now()
print(now)
# datetime.datetime.now() 현재시간 저장
# 242
print(now, type(now))

# 243
import datetime

now = datetime.datetime.now()

for day in range(5, 0, -1):
    delta = datetime.timedelta(days=day)
    date = now - delta
    print(date)
# datetime.timedelta(days) days의 값 후의 시간을 나타낸다.

# 244
import datetime

now = datetime.datetime.now()
print(now.strftime("%H:%M:%S"))
# %H : 0을 채운 10진수 표기로 시간, %M : 0을 채운 10진수 표기로 분, %S : 0을 채운 10진수 표기로 초
# strftime 메서드에 서식을 지정해 날짜 형식을 변환하는 함수

# 245
import datetime

day = "2020-05-04"
ret = datetime.datetime.strptime(day, "%Y-%m-%d")
print(ret, type(ret))
# strptime 문자열을 날짜/시간으로 변환

# 246
import time
import datetime

while True:
    now = datetime.datetime.now()
    print(now)
    time.sleep(1)

# 247

# 248
import os
ret = os.getcwd()
print(ret, type(ret))

# 249
import os
os.rename("C:/Users/hyunh/Desktop/before.txt", "C:/Users/hyunh/Desktop/after.txt")

# 250
import numpy
for i in numpy.arange(0, 5, 0.1):
    print(i)

# 후기 
# 모듈부분은 워낙 외워야할것도 많고 그냥 답지 베꼇다..ㅎ
# 사용하는 방식만 알면 된다고 생각하기때문에 꽁으로 넘어갔지만!