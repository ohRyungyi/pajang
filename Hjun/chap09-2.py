# 211
# 안녕
# Hi

# 212
# 7
# 15

# 213
# 함수에 들어갈 문자열이 들어가 있지 않기때문

# 214
# 함수 안에서 실행한 문자열과 숫자는 더할수 없기때문

# 215
def print_with_smile(a):
    print(a + ':D')



# 216
print_with_smile('안녕하세요')

# 217
def print_upper_price(price):
    print(price*1.3)
print_upper_price(13000)

# 218
def print_sum(a, b):
    print(a+b)
print_sum(3,4)

# 219
def print_arithmetic_operation(a, b):
    print(f'{a} + {b} = {a+b}')
    print(f'{a} - {b} = {a-b}')
    print(f'{a} * {b} = {a*b}')
    print(f'{a} / {b} = {a/b}')
print_arithmetic_operation(3,4)

# 220
def print_max(a,b,c):
    if a>b:
        if a>c:
            print(a)
        else:
            print(c)
    else:
        if b>c:
            print(b)
        else:
            print(c)

print_max(1,2,3)