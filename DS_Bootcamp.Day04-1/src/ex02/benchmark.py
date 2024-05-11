import timeit
import sys


def f_loop(gmails: list):
    new_gmails = []

    for email in gmails:
        if email.endswith('@gmail.com'):
            new_gmails.append(email)
    return new_gmails

def f_list_comprehension(gmails: list):
    new_gmails = [email for email in gmails if email.endswith('@gmail.com')]
    return new_gmails

def f_map(gmails: list):
    new_gmails = list(map(lambda x: x if x.endswith('@gmail.com') else None, gmails))
    return new_gmails

def f_filter(gmails: list):
    new_gmails = list(filter(lambda x: x.endswith('@gmail.com'), gmails))
    return new_gmails


def main(function, num_iter):
    try:
        num_iter = int(num_iter)
    except:
        raise ValueError('Неправильный аргумент, необходимо целое число')
    
    functions = ['loop', 'list_comprehension', 'map', 'filter']
    if function not in functions:
        raise ValueError('Неккоректное название аргумента')
    setup = f"""
from __main__ import f_{function}
emails = 5 * ['john@gmail.com', 'james@gmail.com',
'alice@yahoo.com', 'anna@live.com', 'philipp@gmail.com']
    """
    stmt = f'f_{function}(emails)'
    time = timeit.timeit(setup=setup, stmt=stmt, number=num_iter)
    print(time)


if __name__ == '__main__':
    if len(sys.argv) == 3:
        main(sys.argv[1], sys.argv[2])
