class animals:
    education = 'PETS'

    def __init__(self, name, height, kind):
        self.name = name
        self.height = height
        self.kind = kind
        print('Создался объект')


st1 = animals(name='Барханный кот', height=51, kind='семейство кошачьих')
st2 = animals(name='Британская короткошёрстная кошка', height=60, kind='семейство кошачьих')

print(st1.education)
print(st1.name)
print(st1.height)
print(st1.kind)

print(st2.education)
print(st2.name)
print(st2.height)
print(st2.kind)


class auto:
    education = 'passenger'

    def __init__(self, name, speed, weight):
        self.name = name
        self.speed = speed
        self.weight = weight
        print('Создался объект')


st3 = auto(name='BMW i3', speed='160', weight='1355')
st4 = auto(name='Mercedes-Benz W211', speed='240', weight='1660')

print(st3.education)
print(st3.name)
print(st3.speed)
print(st3.weight)

print(st4.education)
print(st4.name)
print(st4.speed)
print(st4.weight)
