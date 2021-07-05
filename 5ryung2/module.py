# 241 - 
import datetime

now = datetime.datetime.now()
print(now)

# 242 - 
import datetime
now = datetime.datetime.now()
print(type(now))
# # 답지 풀이
# print(now, type(now))

# 243 - 
import datetime
now  = datetime.datetime.now()
for i in range(5, 0, -1):
    day = datetime.timedelta(days = i)
    date = now - day
    print(date)

244 - 
datetime.datetime.now().strfime(형식) : 현재 시간을 인자로 제공하는 형식에 맞춰서 출력
import datetime
now = datetime.datetime.now()
print(now.strftime('%H:%m:%S'))

# 245 - 
import datetime
timeStr = "2020-05-04"
timeVal = datetime.datetime.strptime(timeStr, '%Y-%m-%d')
print(timeVal, type(timeVal))

# 246 -
import datetime, time
while True:
    now  = datetime.datetime.now()
    print(now)
    time.sleep(1)

# # 247 - 모듈 임포트 방법
# 예를 들어서 modi.py 파일 내에 add, sub, multi, division 이라는 함수가 정의된 모듈이 정의되어 있다.
# 1. import 모듈이름
# 예) import modi # 주의 mody.py 라고 하지 않도록 주의한다.
# 2. from 모듈이름 import 모듈함수
# 예) from modi import add
# 3. from 모듈이름 import 모듈함수1, 모듈함수2
# 예) from mody import add, sub
# 4. from 모듈이름 import * 
# 모듈 내의 모든 함수를 호출한다.

# 248 -
import os
print(os.getcwd())

# 249 -
import os
os.rename('/Users/yelimoh/Desktop/test.txt', '/Users/yelimoh/Desktop/changeFileName.txt')

# 250 - 
import numpy
for i in numpy.arange(1.0, 5.0, 1.0):
    print(i)