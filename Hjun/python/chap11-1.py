# 251
# 클래스

# 252
class Human():
    pass

# 253
areum = Human()

# 254
class Human():
    def __init__(self):
        print("응애응애")

areum = Human()

# 255
class Human():
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

areum = Human("아름", 25, "여자")


# 256
print(areum.name, areum.age, areum.sex)

# 257
class Human():
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex
    
    def who(self):
        print(f'이름: {self.name}, 나이: {self.age}, 성별: {self.sex}')

areum = Human("아름", 25, "여자")
areum.who()

# 258
class Human():
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex
    
    def who(self):
        print(f'이름: {self.name}, 나이: {self.age}, 성별: {self.sex}')

    def setInfo(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

areum = Human("모름", 0, "모름")
areum.who()
areum.setInfo("아름", 25, "여자")
areum.who()

# 259
class Human():
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

    def __del__(self):
        print("나의 죽음을 알리지마라!")
    
    def who(self):
        print(f'이름: {self.name}, 나이: {self.age}, 성별: {self.sex}')

    def setInfo(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex
    
areum = Human("아름", 25, "여자")
del(areum)

# 260
# 애초에 들여쓰기 잘못..