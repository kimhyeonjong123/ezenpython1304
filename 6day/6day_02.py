name = '김현종'


# f-string f'{변수}'변수명 대입
# 지역변수 해당하는 문이 끝나면 (괄호) 소멸한다.
# def name(name):
#     print(f'이름은 {name} 입니다.')

# i=0
'''result = 0
for i in range(1,11):
    result = 0
    # print(i)
    result = result + i
print(result)'''

def printsve(name):
    print(f'{name}입니다.')

printsve('김현종')

def printage(age):
    print(f'{age}입니다.')

printage('23')

def printaddress(address):
    print(f'{address}입니다.')

printaddress('성북구')

def home(name, age, address):
    print(f'{name}, {age}, {address}')

printsve('가나다')
printage('25')
printaddress('경기도')

home('김현종', 23, '성북구')