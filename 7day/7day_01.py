a = 1


def vartest():
    # global a
    # a = 0 # 초기값 설정하기
    b = 0
    result = b + 1
    global a
    a = result
    print(a)


'''name = []

while True:
    name = input('이름을 입력하세요: ')
    dic = {'name1' : '김현종', 'name2' : '유영훈'}
    dic.get('name1')
    # print(name)'''

