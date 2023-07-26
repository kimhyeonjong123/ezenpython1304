name ='김현종'
age = 23
address ='성북구'

# 변수는 한타입만 받을 수 있다.
# 저장할 수 있다
print('안녕하세요')

# 함수(method) -> 괄호 안에 개수에 상괍없고 어떤 타입이든 담을 수 있다
# python method 선언 def 메소드이름() <- 함수(method)
# 함수 (method) -> call 호출한다 자기자신이 호출 할 수 없다.
def name():
    print('김현종')

# name() call 한다.
name()

def age():
    print('23')

age()
def address():
    print('성북구')

address()

def add(a,b):
    result = a + b
    return result
    a = add(3, 4)
    print(a)
