from 9days class import parent

class Icefatory(parent):

#오버라이팅 -> 부모에 있는 메소드 이름, 직접, 개수가 같으면 자식이 부모에 있는 메소드를 재정의한다.
#오버로딩 ->메소드명은 같은데 리턴타입 아귀먼트 타입, 아퀴먼트 개수가 틀린 경우
    def parentmethod(self):
        print('parentmethod')