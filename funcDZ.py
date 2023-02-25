

def fun(fn):
    if type(fn) is str:
        bk = 0
        for i in fn:
            if i.isalpha():
                bk += 1
        print(fn, ' - это строка, в ней', bk, 'букв')
    elif type(fn) is int:
        cht = 0
        for i in str(fn):
            i = int(i)
            if i % 2 == 0:
                cht += 1
        print(fn, ' - это число, в нем', cht, 'четных символов.')
    elif type(fn) is tuple:
        print('кортеж')
    elif type(fn) is list:
        nu = 0
        buk = 0
        for i in str(fn):
            if i.isalpha():
                buk += 1
            elif i.isdigit():
                nu += 1
        print(fn, ' - Это список, в нем', buk, '- букв и', nu, '- цифр.')


fun(34289766)
fun('hjghj568')
fun([789, 'sdfgssss'])
fun(('bj',))


