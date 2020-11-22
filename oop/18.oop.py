class Demo():
    __obj = None

    def __new__(cls, *args, **kwargs):
        if not cls.__obj:
            cls.__obj = object.__new__(cls)

        return cls.__obj

a = Demo()
b = Demo()
print(a)
print(b)