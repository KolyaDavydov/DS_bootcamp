import timeit
import sys
from functools import reduce


def f_loop(num: int):
    result = 0

    for i in range(1, num + 1):
        result += i ** 2
    return result

def f_reduce(num: int):
    result = reduce(lambda x, y: x + y ** 2, [i for i in range(1, num + 1)])
    return result


def main(function, num_iter, number):
    try:
        num_iter = int(num_iter)
        number = int(number)
    except:
        raise ValueError('Неправильный аргумент, необходимо целое число')
    
    functions = ['loop', 'reduce']
    if function not in functions:
        raise ValueError('Неккоректное название аргумента')
    setup = f"from __main__ import f_{function}"
    stmt = f'f_{function}({number})'
    time = timeit.timeit(setup=setup, stmt=stmt, number=num_iter)
    print(time)


if __name__ == '__main__':
    if len(sys.argv) == 4:
        main(sys.argv[1], sys.argv[2], sys.argv[3])
