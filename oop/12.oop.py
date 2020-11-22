class Demo():
    listurl = []

    def __len__(self):
        return len(self.listurl)

    def __str__(self):
        return '这是当前脚本中的一个_对象 str'

    def __repr__(self):
        return '这是一个对象'

    def __bool__(self):
        return bool(self.listurl)


obj = Demo()
# res = len(obj)
res = bool(obj)
print(res)
# print(obj)
# print(res)