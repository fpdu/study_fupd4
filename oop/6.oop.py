class mkke():
    maose = '猫纹'
    sex = 'm'

    def pao(self):
        print('走猫步')
    def pa(self):
        print('能上树')

class mao(mkke):
    def pa(self):
        super().pa()
        print('很快就能上树了')
    def vr(self):
        print('喜欢抓老鼠')


h = mao()
# print(h)
# print(h.__dict__)
# print(mkke.__dict__)
print(h.maose)
h.pao()
h.pa()

res = 100/3
print(res)