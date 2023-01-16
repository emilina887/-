def divider(a, b):
    if type == str:
        a = int(a)
    if b == 0:
        b = 1
    try:
        c = a / b
        return c
    except ZeroDivisionError:
        print('division by zero')


if a < b:
    try:
        a = a + b
    except ValueError:
        print('A < B')
if b > 100:
    raise IndexError

result = []

data = {10: 2, 2: 5, "123": 4, 18: 0, 1: 15, 8: 4}
for key in data:
    res = divider(key, data[key])
    result.append(res)

print(result)
