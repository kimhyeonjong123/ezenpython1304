# raise 고의로 에러를 발생
class raise_1:

    def fromethod(self):

        for i in range(1, 6):

            if i == 4:
                raise


ra = raise_1()
ra.fromethod()
