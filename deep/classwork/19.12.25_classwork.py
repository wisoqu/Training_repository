# Iterators
#tumb = ["pencil", "apple", "book"]
#
# print(iter(tumb)) It doesn`t work!
# num = 23193
# Cycle for works not with objects inside collection but with iterations
#in this collection
#print(iter(num))
#<list_iterator object at 0x000001D66661CC70>
from sqlalchemy.sql.functions import next_value

#
# our_set = {1, 2, 3, 4}
# print(iter(our_set))


# for obj in tumb:

#     print(obj)
# For is just using iter algorithm for its work

# Analogue of for cycle with while
# tumb = {1, 2, 4, False, 'dfv', True}
#
# it  = iter(tumb) # Rule


# Have been just working on the custom iterartion with next()
# try:
#     while True:
#         next_value = next(it)
#         print(f'One more value: {next_value}')
# except StopIteration:
#     print('No more value, go and touch a grass')
# print('It is over!')

# name is argument
# def say_hi(name, ):
#     """The function says hi"""
#     print(f"hi there, {name.title()}")
#
#  A good version of a function+
# def summ(num, num1):
#     return num1 + num
#
# print(summ(1, 2))
#
# def print_message():
#     """Local functions"""
#     def say_hi(): print("hi")
#     def say_bye(): print("bye")
#
#     say_hi()
#     say_bye()
#
#
# print_message() # while trying to realize do not do this through PRINT it would cause None type
# # spasibo

# def main():
#     say_hi()
#     say_bye()
#
#
# def say_hi(): print("hi")
# def say_bye(): print("bye")
#
# main()

# def main():
#     num_1 = 3
#     num_2 = 2
#     print(multiplication(num_1, num_2))
#     print(summ(num_1, num_2))
#
# def summ(num_1, num_2):
#     summ = num_1 + num_2
#     return summ
#
# def multiplication(num_1, num_2, res_mult):
#     multiplication = num_1 * res_mult
#     return res_mult
#
# main()

# The argument`s passing

