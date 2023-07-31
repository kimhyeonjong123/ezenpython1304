class classmethod_1:

    def __init__(self, name):
        self.name = name

    def standmethod(self):
        print(self.name)

    # classmethod 해당하는 생성자를 호출해서 리턴한다.
    @classmethod
    def class__method(cls):
        return cls('아무개')


cn = classmethod_1('김현종')
cn.standmethod()
cn2=cn.class__method()
cn2.standmethod()