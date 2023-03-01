class Calculator:
    def __init__(self, num1,operat, num2):
        self.num1 = num1
        self.operat = operat
        self.num2 = num2


    def um(self): print(self.num1 * self.num2)

    def de(self):
        if self.operat == '/':
            try:
                wtf = self.num1 / self.num2
            except ZeroDivisionError:
                wtf = 'Деление на 0 запрещено!'
        print(wtf)

    def sl(self): print(self.num1 + self.num2)

    def vch(self): print(self.num1 - self.num2)

while True:
    num1 = float(input('Введите число :'))
    if num1 == 0:
        break
    operat = input('Выбирите действие +-*/ :')
    num2 = float(input('Введите число :'))
    if operat == '+':
        print(Calculator)
    elif operat == '-':
        print(Calculator)
    elif operat == '*':
        print(Calculator)
    elif operat == '/':
        print(Calculator)

