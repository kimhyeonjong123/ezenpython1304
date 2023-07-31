from ects.node.ezen_factory1 import ezen_factory1


class ezenone(ezen_factory1):

    def printezenone(self):
        print('ezen one')



ez = ezenone('ezen', 'room1301', 'htp', 6)


ez2 = ezenone('ezen', 'room1302', 'c++', 8)


ez3 = ezenone('ezen', 'room1303', 'ph', 10)


ez4 = ezenone('ezen', 'room1304', 'python', 5)


ezenlist=[ez,ez2,ez3,ez4]
for i in ezenlist:
    print(i.school_name(),end='\t')
    print(i.room_number(),end='\t')
    print(i.room_type(),end='\t')
    print(i.person_count())


