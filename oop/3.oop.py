class Person():
    name = None
    age = None
    sex = None
    def __init__(self,n,a,s):
        self.name = n
        self.age = a
        self.sex = s
        self.say()

    def say(self):
        print(f'大噶好,唔系{self.name}系兄弟就来砍我')

zzh = Person('渣渣辉',56,'男')
print(zzh.name)
print(zzh.age)
