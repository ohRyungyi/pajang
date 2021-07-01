# 031
# 34가 출력된다.

# 032
# HiHiHi

# 033
print('-'*80)

# 034
t1 = 'python'
t2 = 'java'
t3 = t1+' '+t2+' '
print(t3*4)

# 035
name1 = "김민수" 
age1 = 10
name2 = "이철희"
age2 = 13
print("이름: %s 나이: %d" %(name1,age1))
print("이름: %s 나이: %d" %(name2,age2))

# 036
print("이름: {} 나이: {}".format(name1, age1))
print("이름: {} 나이: {}".format(name2, age2))

# 037
print(f"이름: {name1} 나이: {age1}")
print(f"이름: {name2} 나이: {age2}")

# 038
상장주식수 = "5,969,782,550"
상장주식수_replace = 상장주식수.replace(',','')
상장주식수_int = int(상장주식수_replace)
print(상장주식수_int, type(상장주식수_int))

# 039
분기 = "2020/03(E) (IFRS연결)"
print(분기[:7])

# 040
data = "   삼성전자    "
data_strip = data.strip()
print(data_strip)

# 후기
# 데이터타입(%)와 포맷팅 방식을 활용한 출력에 관해서 다시금 상기시켰다.