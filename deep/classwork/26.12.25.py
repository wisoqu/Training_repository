# lambda: (params)
#
# def message(): print('Hello')
#
#
# # anonym function
# message_1 = lambda: print('Hello')
#
# message()
# message_1()
from dns.reversename import ipv4_reverse_domain
from torch.fx.experimental.migrate_gradual_types import operation


# openai = lambda x: x ** x
#
# def do_operation(a, b, operation):
#     result = operation(a, b)
#
# do_operation(5, 4, lambda a, b: a + b)
# do_operation(5, 4, lambda a, b: a * b)

# def do_operation(a, b, operation):
#     result = operation(a, b)
#     return result
#
# a, b = map(int, input().split())
# sighn = input()
# if sighn == '-': do_operation(a, b, lambda a, b: a - b)
# elif sighn == '+': do_operation(a, b, lambda a, b: a + b)
# else: do_operation(a, b, lambda a, b: a * b)

#
# def select_choice(user_choice):
#     if user_choice == 1:
#         return lambda num_1, num_2: num_1 * num_2
#     elif user_choice == 2:
#         return lambda num_1, num_2: num_1 + num_2
#
# operation = select_choice(1)
# print(operation(1, 3))


# name = 'Yuki' # In global context
#
# def say_hi(): print(f'Hi, {name}')
# def say_bye(): print(f'Bye, {name}')
#
#
# say_hi()
# say_bye()

# Local context
#
#
#
# def say_hi():
#     """Local context variable"""
#     name = 'Yuki'
#     surname = 'Kioto'
#     print(f'Hi, {name}')
# def say_bye():
#     """Again local context variable"""
#     name = 'Yuki'
#     surname = 'Kioto'
#     print(f'Bye, {name}')
#
# say_hi()
# say_bye()


# Hiding variables
#
# name = 'T-800'
#
#
# def say_hi():
#     """Local context variable"""
#     global name # redefinition ONLY FOR FUNCTIONS
#     name = 'Yuki'
#     print(f'Hi, {name}')
#
#
# def say_bye():
#     """Again local context variable"""
#     # name = 'Yuki'
#     print(f'Bye, {name}')
#
#
# say_hi()
# say_bye()


# Nonlocal
#
# def outer():
#     num = 5
#
#     def inner(): # Include func
#         nonlocal num
#         num = 25
#         print(num)
#
#     inner() # 5
#     print(num)
#
# outer() # 5

# closure
#
# def outer():
#     num = 5 # Lexical environment
#
#     def inner(): # Include func
#         nonlocal num # This means we have this from another function, IMPORTANT
#         num += 1
#         print(num)
#
#      # 5
#     return inner
#
# foo = outer() # 5
# foo() # 6
# foo() # 7
# foo() # 8