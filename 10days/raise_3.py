class raise_3:

    def fromethod(self):

        for i in range(1, 6):

            if i == 4:
                raise Exception('에러입니다.')


ra = raise_3()
ra.fromethod()
