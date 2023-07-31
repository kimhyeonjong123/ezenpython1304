# 추상클래스는 추상메소트가 오면 객체생성을 할 수 없다.
# 추상메소드가 없으면 객체를 생설할 수 있다:
# 추상클래스는 반드시 ABEMETA 상속 받아야한다.

import abc
from abc import ABCMeta, abstractmethod


# metaclass=ABCMeta -> 추상클래스 선언 (abstract class)
class abstractclasss_1(metaclass=ABCMeta):

    def __init__(self, ob):
        self.ob = ob

    def standmethod(self.intut):
        print(self.ob)
        print(self.input)

# 추상메소드는 몸체가 없다.
# 추상메소드를 상속하는 클래스는 반드시 몸체구현을 해줘야한다. 아니면
# 자식은 객체생성을 할 수 있다. (일반클래스)
#     @abstractmethod
#     def abstract_method(self):


ac = abstractclasss_1('타입')
ac.standmethod()
