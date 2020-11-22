# class Student():
#     def __init__(self,id,name,score):
#         self.id = id
#         self.name = name
#         # self.score = score
#         if score >= 0 and score <= 100:
#             self.score = score
#         else:
#             print('当前分数不符合要求')
#
#     def returnMe(self):
#         info = f'''
#         学员编号:{self.id}
#         学员姓名:{self.name}
#         学员分数:{self.score}
#         '''
#         print(info)
#     def __setattr__(self, key, value):
#         if key == 'score':
#             if value >= 0 and value <= 100:
#                 object.__setattr__(self,key,value)
#             else:
#                 print('当前分数不符合要求')
#         else:
#             object.__setattr__(self,key,value)
#     #
# zs = Student(1011,'张三丰',99)
# zs.returnMe()
# zs.score = -20
# zs.score = 88
# zs.returnMe()


class Score():
    def __get__(self, instance, owner):
        return self.__score
    def __set__(self, instance, value):
        if value >= 0 and value <= 100:
            self.__score = value
        else:
            print('分数要求不合理')

class Student():
    score = Score()

    def __init__(self,id,name,score):
        self.id = id
        self.name = name
        self.score = score

    def returnMe(self):
        info = f'''
        学员编号:{self.id}
        学员姓名:{self.name}
        学员分数:{self.score}
        '''
        print(info)

zs = Student(1011,'张三丰',99)
zs.returnMe()
