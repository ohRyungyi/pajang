#021
letters = 'python'
print(letters[0], letters[2])

#022
license_plate = "24가 2210"
print(license_plate[-4:])

#023
string = "홀짝홀짝홀짝"
print(string[::2])

#024
string = "PYTHON"
print(string[::-1])

#025
phone_number = "010-1111-2222"
print(phone_number.replace('-',' '))

#026
print(phone_number.replace('-',''))

#027
url = "http://sharebook.kr"
url_split = url.split('.')
print(url_split[-1])

#028
# 에러가 발생한다. 문자열은 수정할수 없기때문이다.

#029
string = 'abcdfe2a354a32a'
print(string.replace('a','A'))

#030
# 문자열은 수정할수 없기때문에 그대로 출력이 되거나 오류가 발생한다.

# 후기
# 문자열을 할 상황이 별로 없었기 때문에 문자열이 수정되지 않는다는것은 처음알았고
# 문자열을 replace할때는 따로 변수선언후 변경할수 없다는것이 중요하다고 생각했다.
# 인덱싱의 편리성과 중요함에 대하여 다시금 알게 되었다.