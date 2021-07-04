user_input = input("5자리 숫자를 입력하세요 : ")
sum = 0
for i in range(1,6) :
    print("{} x {} = {}" .format(user_input[-i],(i+2),int(user_input[-i])*(i+2)))
    sum += int(user_input[-i])*(i+2)
print("합계 :", sum)
print ("고유번호는 \"{}\"입니다." .format(sum%3))