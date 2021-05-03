class Person:
    def __init__(self, name, surname, age):
        self.name = name
        self.__surname = surname
        self.__age = age

    def get_info(self):
        return 'Name+Surname-> {} {}\nAge: {}'.format(str(self.name), str(self.__surname), str(self.__age))


# 1. Напишите код, который выведет на экране все переменные объекта произвольного пользовательского класса.
# :return:
def num1():

    print('1->')
    p1 = Person('Jin', 'Kim', 28)
    print(dir(p1))
    print(vars(p1))
    print(p1.__dict__)


# 2. Напишите код, который по имени метода, заданному строкой, вызовет этот метод в некотором пользовательском классе.
# :return:
def num2():

    print('\n2->')
    p1 = Person('Jin', 'Kim', 28)
    method_to_invoke = getattr(p1, 'get_info')
    print(method_to_invoke())


if __name__ == '__main__':
    num1()
    num2()