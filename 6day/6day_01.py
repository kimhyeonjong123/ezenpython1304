# static 변수 지역변수

name = '김현종'
age = 23
address = '일본'


def name():
    name = '김현종'
    return name


def age():
    age = 23
    return age


def address():
    address = '일본'
    return address


print(name())
print(age())
print(address())


def home():
    home = '성북구, 김현종, 23'
    return home
print(home())