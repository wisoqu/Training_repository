#
#
# def mini_work() -> None:
#     ar = {'a', 'b', 'c'}
#     ar_1 = ar
#     ar_2 = ar.copy()
#
#     print(f'id arr: {id(ar)}')
#     print(f'id ar_1 (we have link): {id(ar_1)}')
#     print(f'id ar_2 (we just copied data): {id(ar_2)}')
#
#     ar_1.add(2)
#     ar_2.add(3)
#     print(f'id ar_1 (we have link) and add some new data: {id(ar_1)}')
#     print(f'id ar_2 (we just copied data) and add some new data: {id(ar_2)}')
#
# mini_work()
# Bad example with unpredictable behavior
#
# def test_foo_1(listening=[]):
#     listening.append(1)
#     print(listening)
#
# test_foo_1()

def test_foo_2(listening=None) -> None:
    if listening is None:
        listening = []
    listening.append(1)
    print(listening)

test_foo_2()
#[1]
test_foo_2()
#[1]
test_foo_2([8, 1, 3, 2, 34,45])
test_foo_2()