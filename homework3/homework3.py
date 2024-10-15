def dvenadcat(n):
    f=n//12
    if f==10:
        f='A'
    if f==11:
        f='B'
    g=n%12
    if g==10:
        g='A'
    if g==11:
        g='B'    
    if n < 12:
        if n==10:
            n='A'
            return str(n)
        elif n==11:
            n='B'
            return str(n)
        else:
            return str(n)          
    else:
        return dvenadcat(f) + str(g)
print('Введите целое положительное число для перевода в двенадцатиричную систему счисления')
x=input()
if x.isdigit():
    x=int(x)
    print(f'Число {x} в двенадцатиричной системе счисления: {dvenadcat(x)}')
else:
    print('Введите целое положительное число для перевода, программа переводит только их')