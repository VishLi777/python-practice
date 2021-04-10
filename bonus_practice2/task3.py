# import pyfiglet
import os

# Преобразование Барроуза-Уилера
def transformation_burrows_wheeler(src_num):
    index = 0
    temporary = tmp_string = resp_arr = []

    for i in range(len(src_num)):
        temporary.append(src_num)
        src_num = src_num[1:] + src_num[0]
    temporary.sort()

    for i in range(len(src_num)):
        if temporary[i] == src_num:
            index = i
            break

    for i in range(len(src_num)):
        resp_arr.append(temporary[i][-1])
        tmp_string += temporary[i][-1]
    resp_arr.sort()

    for i in range(len(src_num) - 1):
        for j in range(len(src_num)):
            resp_arr[j] = tmp_string[j] + resp_arr[j]
        resp_arr.sort()

    return resp_arr[index]


if __name__ == '__main__':
    print(transformation_burrows_wheeler('25789'))
    print(transformation_burrows_wheeler('9874261'))


# Разработать функцию, выдающую ASCII-баннер с пользовательским текстом.
def draw_banner1(text):
    arr = []
    i = 0

    with open('doc.txt') as file:
        read_file = file.read()
        line_split = read_file.split('@@')
    line_split.pop()

    for read_file in line_split:
        arr.append(read_file.split('@\n'))
        if (arr[i][0][:1] == "\n"):
            arr[i][0] = arr[i][0].replace('\n', '')
        i += 1

    for j in range(6):
        tmp = ''
        for i in range(len(text)):
            ind = ord(text[i])
            if (65 <= ind <= 90):
                tmp += arr[ind - 65][j]
            elif (97 <= ind <= 122):
                tmp += arr[ind - 71][j]
        print(tmp)

draw_banner1('MIREA')

# to run def draw_banner2(string) uncomment this code and  string import pyfiglet in the top of task3.py
#def draw_banner2(string):
#   print(pyfiglet.figlet_format(string))
# print('---------------------')
# draw_banner2('IKBO')


# Написать утилиту командной строки, формирующую дерево каталогов и файлов с учетом вложенности и начиная с заданного
# пути. Результат должен быть выдан в виде текста в формате graphviz.
def recursive_files_and_directories():
    for dirpath, dirnames, filenames in os.walk(os.getcwd()):
        print("Files->")
        # перебор файлов
        for filename in filenames:
            print('  ' + os.path.basename(dirpath) + " -> " + f'"{filename}"')
        print("Directories->")
        # перебор папок
        for dirname in dirnames:
            print('  ' + os.path.basename(dirpath) + " -> " + dirname)

#формат graaphviz
def print_tree(s):
    if s == 'start':
        print('digraph G {')
    elif s == 'end':
        print('}')
    return s


def form_tree():
    print_tree('start')
    recursive_files_and_directories()
    print_tree('end')


form_tree()

