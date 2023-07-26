# method 오버로딩이 안된다. -> 메소드 이름을 다름 메소드 명으로 둘 수 있다.
# 오버로딩: 메소트 이름

def name(*home):
    print(home)


def home2(*name):
    return name

def home3(name, home):
    print(f'{name} 나머지는 {home} 입니다.')

name('김현종', 40, '시흠')

print(home2('유영훈', 23, '성북구'))

print(home2('김현종', 25, '호주'))