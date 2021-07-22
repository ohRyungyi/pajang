#011
삼성전자 = 50000
print(f"평가금:{삼성전자*10}")

#012
삼성전자 = {
    '시가총액':298,
    '현재가':50000,
    'PER':15.79
}
print(f"삼성전자 시가총액:{삼성전자['시가총액']}조",f"상성전자 현재가:{삼성전자['현재가']}원",f"삼성전자 PER:{삼성전자['PER']}",sep='\n')

#013
s = "hello"
t = "python"

print(f"{s}! {t}")

#014
#8

#015
a = 132
print(type(a))

#016
num_str = "720"
num_int = int(num_str)
print(type(num_int))

#017
num = 100
num_str = str(num)
print(type(num_str))

#018
num = "15.79"
num_float = float(num)
print(type(num_float))

#019
year = "2020"
year_int = int(year)
print(f'{year_int-2}',f'{year_int-1}',f'{year_int}',sep=',')

#020
pay = 48584
print(pay*36)

# 여러가지 입력값을 넣을때 +를 넣는 방식도있지만 f를 활용한 방식이 더나에게 맞는것 같다.