class Calculator:

    def __init__(self, first_num, second_num, operation):
        self.first_num = first_num
        self.second_num = second_num
        self.operation = operation

    def addition(self):
        return self.first_num + self.second_num

    def difference(self):
        return self.first_num - self.second_num

    def multiplication(self):
        return self.first_num * self.second_num

    def division(self):
        return self.first_num / self.second_num

    def calculation(self):
        if self.operation == '+':
            return self.addition()
        if self.operation == '-':
            return self.difference()
        if self.operation == '*':
            return self.multiplication()
        if self.operation == '/':
            return self.division()


if __name__ == '__main__':
    print('Введите первое число:')
    first_numeric = int(input())
    print('Введите оператор:')
    sign = input()
    print('Введите второе число:')
    second_numeric = int(input())
    cal_object = Calculator(first_numeric, second_numeric, sign)
    print('Полученный результат: ' + str(cal_object.calculation()))
