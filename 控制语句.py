def whl_t():
    a, b = 0, 1
    while a < 10:
        print(a, end=',')
        a, b = b, a + b


def if_t():
    x = int(input("Please input an integer: "))
    if x < 0:
        x = 0
        print('Negative changed to zero')
    elif x == 0:
        print('Zero')
    elif x == 1:
        print('Single')
    else:
        print('More')


def for_t():
    words = ['cat', 'window', 'defenestrate']
    for w in words:
        print(w, len(w))


# def for_change_error():
#     users = {'a': 'active', 'window': 'inactive', 'defenestrate': 'active'}
#     for user, status in users.items():  # RuntimeError: dictionary changed size during iteration
#         if status == 'inactive':
#             del users[user]

def for_change():
    users = {'a': 'active', 'window': 'inactive', 'defenestrate': 'active'}
    for user, status in users.copy().items():  # RuntimeError: dictionary changed size during iteration
        if status == 'inactive':
            del users[user]
    print(users.keys())


def for_change2():
    active_users = {}
    users = {'a': 'active', 'window': 'inactive', 'defenestrate': 'active'}
    for user, status in users.items():  # RuntimeError: dictionary changed size during iteration
        if status == 'active':
            active_users[user] = status
    print(active_users.keys())


def break_t():
    for n in range(2, 10):
        for x in range(2, n):
            if n % x == 0:
                print(n, 'equals', x, '*', n//x)
                break
        else:
            # loop fell through without finding a factor
            print(n, 'is a prime number')


def continue_t():
    for num in range(2, 10):
        if num % 2 == 0:
            print("Found an even number", num)
            continue
        print("Found an odd number", num)


def pass_t():
    while True:
        pass  # Busy-wait for keyboard interrupt


class MyEmptyClass:
    pass


def initlog(*args):
    pass  # Remember to implement this!


if __name__ == '__main__':
    # whl_t()
    # if_t()
    # for_t()
    # for_change()
    # for_change2()
    # break_t()
    continue_t()
    # pass_t()
