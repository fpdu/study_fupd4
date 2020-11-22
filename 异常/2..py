try:
    s1 = 'hello'
    int(s1)

except ValueError as e:
    print(e)

try:
    s1 = 'hello'
    s1[5]
except IndexError as e:
    print('IndexError',e)
except KeyError as e:
    print('KeyError',e)
except ValueError as e:
    print('ValueError',e)


s1 = 'world'
try:
    int(s1)
except Exception as e:
    print('Exception ===',e)