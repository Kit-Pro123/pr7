print('Подсчет уравнения по формуле x=a-b-4*c')
print('Введите число a')
a=input()
print('Введите число b')
b=input()
print('Введите число c')
c=input()
if a.isdigit() and b.isdigit() and c.isdigit():
    a=int(a)
    b=int(b)
    c=int(c)
    x=a-b-4*c
    print(f'Полученный результат: {x}')
else:
    print('Данные введены неверно, вводите целые числа для подсчета уравнения, программа использует только их')