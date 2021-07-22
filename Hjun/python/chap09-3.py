# 221
def print_reverse(string):
    print(string[::-1])

print_reverse("python")

# 222
def print_score(abs):
    print(sum(abs)/len(abs))

print_score([3,4,5])

# 223
def print_even(abs):
    for i in abs:
        if i % 2==0:
            print(i)

print_even([2,4,8,6,3,1,5])

# 224
def print_keys(dictionary):
    for i in dictionary.keys():
        print(i)
print_keys ({"이름":"김말똥", "나이":30, "성별":0})

# 225
my_dict = {"10/26" : [100, 130, 100, 100],
           "10/27" : [10, 12, 10, 11]}

def print_value_by_key(dictionary, keys):
    print(dictionary[keys])

print_value_by_key(my_dict, "10/26")

# 226
def print_5xn(line):
    chunk_num = int(len(line) / 5)
    for x in range(chunk_num + 1) :
        print(line[x * 5: x * 5 + 5])

print_5xn("아이엠어보이유알어걸")

# 227
def printxn(line, num):
    chunk_num = int(len(line) / num)
    for x in range(chunk_num + 1) :
        print(line[x * num: x * num + num])

printxn("아이엠어보이유알어걸", 3)

# 228
def calc_monthly_salary(annual_salary):
    month_salary = int(annual_salary/12)
    print(month_salary)

calc_monthly_salary(3800)

# 229 
# 왼쪽: 100
# 오른쪽: 200

# 230
# 왼쪽: 100
# 오른쪽: 200