class static_1:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

    def standmethod(self, input1):
        print(self.name)
        print(self.age)
        print(self.address)
        print(input)

    # @staticmethod 는 self로는 접근하지 못한다.
    @staticmethod
    def static_method():
        print('static method')
        print(input)


st = static_1('이무개', 23, '한국')
st.standmethod('입력')
st.static_method('입력2')
static_1.static_method('입력2')