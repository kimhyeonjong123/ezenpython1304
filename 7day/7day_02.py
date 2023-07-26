dic ={}

i = 0
while True:
    inputvalue = input('이름을 입력하세요.')

    i = i + 1
    if inputvalue =='q':
        exit()
    dic.setdefault(i, inputvalue)
    print(dic)