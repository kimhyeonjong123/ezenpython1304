# finally 무조건 실행 에러가 나든 안나든
class raise_4:

    def fromethod(self):
        try:
            a = [1, 2, 3, 4, 5]
            print(a[6])

        except:
            raise Exception('에러입니다.')

        finally:
            raise Exception('무조건 에러')


ra = raise_4()
ra.fromethod()
