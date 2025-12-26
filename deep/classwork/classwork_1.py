'''
1 неизменяемые типы данных
списки, словари, множества, байтовый массив
2 неизменяемые типы данных
кортежи, float, int, string, bool, None, complex, bytes, frozenset
'''
#
# def heap_test_foo() -> None:
#     num = 100
#     num_2 = num
#
#     print(f'num: id {id(num)}')
#     print(f'num_2: id {id(num_2)}')
#     Ссылка на ячейку в оперативной памяти
# heap_test_foo()


#
# def heap_test_foo() -> None:
#     num = 100
#     num_2 = num
#     print(f'num: id {id(num)}')
#     print(f'num_2: id {id(num_2)}')
#     num += 1
#     print(f'num: id {id(num)}')

# num: id 140704363728904
# num_2: id 140704363728904


#heap_test_foo()

# num: id 140704363728904
# num_2: id 140704363728904
# num: id 140704363728936

# Поведение изменяемых типов данных
def heap_test_foo() -> None:
    lst_num = [100]
    lst_num_2 = lst_num
    print(f'num: id {id(lst_num)}')
    print(f'num_2: id {id(lst_num_2)}')
    lst_num.append(101)
    print(f'num: id {id(lst_num)}')

heap_test_foo()
# num: id 2750253671360
# num_2: id 2750253671360
# num: id 2750253671360
# сериолайзер - инструмент который позволяет преобразовывать типы данных







