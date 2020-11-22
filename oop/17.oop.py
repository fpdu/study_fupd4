# class ScoreManange():
#     def __get__(self, instance, owner):
#         pass
#     def __set__(self, instance, value):
#         pass
#     def __delete__(self, instance):
#         pass
#
# class Student():
#     score = ScoreManange
#

# class Student():
#     def getscore(self):
#         print('getscore')
#
#     def setscore(self,value):
#         print('setcore')
#
#     def delscore(self):
#         print('delscore')
#
#     score = property(getscore,setscore,delscore)
# zs = Student()
# print(zs.score)
# zs.score = 200
# del  zs.score

class Student():
    __score = None

    @property
    def score(self):
        print('get')
        return self.__score
    @score.setter
    def score(self,value):
        print('set')
        self.__score = value

    @score.deleter
    def score(self):
        print('delete')
        del self.__score

zs = Student()
print(zs.score)
zs.score = 199
print(zs.score)
del zs.score
