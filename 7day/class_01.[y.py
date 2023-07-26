result = 0


def num(input):
    global result
    result = input
    return result


print(num('입력'))


class room1304:
    # self 현재 해당하는 객체(instance)
    def name(self):
        return 'self 객체'

    # 객체지향은 큰데에서 작은데러 간다

    # 지구.대한민국.서울.강남구.w건물.13.1304.김현호
    def prname(self, name):
        print(f'이름은 {name} 입니다')


r1304 = room1304()
print(r1304.name())
# prname = room1304()

r1304.prname('김현호')

r1304_2 = room1304()
r1304_2.prname('아무개')
# print(id(r1304))
# print(id(r1304_2))

# class: python1304
# 1번 객체는 1~10 합을 출력하는 sum1 출력 return
# 2번 객체는 11~20 합을 출력하는 sum2 출력 print()

class python1304:
    # self 현재 해당하는 객체(instance)
    def object1(self):

        sum1 = 0
        for i in range(1, 11):
            sum1= sum1 + i
        return sum1

r1304 = python1304()
print(r1304.object1())

# class python1304:
#     def object2(self):
#
#         sum2 = 0
#         for i in range(11, 21):
#             sum2= sum2 + i
#         return sum2
#
#         print(f'숫자의 합은 {sum2}')
#
# r1304 = python1304()
# print(r1304.object2())


class fourcal:
    result = 0
    def setdate(self, first, ten):
        self.first = first
        self.ten = ten
        a = fourcal
        a.setdate(1,10)

    def add2(self):

        result = self.first + self.ten
        return result
        print(f'숫자의 합은 {result}')

add1 = fourcal()
print(add1.add2())
