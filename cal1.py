def sum_1(a, b): return a + b

def um(a, b): return a * b

def mi(a, b): return a - b

def de(a, b):
    if c == '/':
        try:
            wtf = a / b
        except ZeroDivisionError:
            wtf = 'Деление на 0 запрещено!'
    return wtf

print('Калькулятор работает. \nДля завершения введите 0.')
while True:
    a = float(input('Введите число :'))
    if a == 0:
        break
    c = input('Выбирите действие +-*/ :')
    b = float(input('Введите число :'))
    if c == '+':
        print(sum_1(a, b))
    elif c == '-':
        print(min(a, b))
    elif c == '*':
        print(um(a, b))
    elif c == '/':
        print(de(a, b))


print("Завершено")