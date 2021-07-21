# 1부터 50까지 숫자 중 임의의 한 숫자를 뽑습니다. (변수명 예시 : answer)
# 사용자에게 input을 받습니다. (변수명 예시 : num // input을 받는 형태 : "n번째 시도입니다. 숫자를 입력하세요 => " )
# answer과 num을 비교해 up, down을 알려줍니다.
# 답을 맞출 때 까지 위 과정을 반복합니다.

# 하나의 클래스를 생성해야합니다
# 해당 클래스에는 임의의 숫자를 만드는 메서드(makeAnswer)와 답, 오류를 체크하는 메서드(checkAll)이 있습니다.
# 사용자는 객체를 생성함으로써 해당 게임에 참여할 수 있습니다. (NumberGame)
# 객체생성시, 이름과 나이를 생성자로 입력해야합니다.
# 해당 게임에 참여하는 사용자의 수를 셀 수 있어야합니다.
# 사용자가 시도한 총 횟수를 셀 수 있어야합니다.
# 사용자가 문자를 입력하는 경우 : "invalid literal for int() with base 10: '사용자입력' 숫자를 입력하세요" 이러한 문자열이 출력되어야합니다 (Except as 사용)


# 예시
""" 

kim = NumberGame("kim", 20)
yoon = NumberGame("yoon", 21)
park = NumberGame("park", 23)

print(NumberGame.PLAYER_COUNT)  // 3

kim.makeAnswer()
kim.checkAll()

"""

