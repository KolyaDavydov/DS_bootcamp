import timeit


def loop(gmails: list):
    new_gmails = []

    for email in gmails:
        if email.endswith('@gmail.com'):
            new_gmails.append(email)
    return new_gmails

def list_comprehension(gmails: list):
    new_gmails = [email for email in gmails if email.endswith('@gmail.com')]
    return new_gmails

def map_loop(gmails: list):
    new_gmails = list(map(lambda x: x if x.endswith('@gmail.com') else None, gmails))
    return new_gmails


def main():
    num_iter = 9000000
    setup = """
from __main__ import loop, list_comprehension, map_loop
emails = 5 * ['john@gmail.com', 'james@gmail.com',
'alice@yahoo.com', 'anna@live.com', 'philipp@gmail.com']
    """
    stmt_1 = 'loop(emails)'
    stmt_2 = 'list_comprehension(emails)'
    stmt_3 = 'map_loop(emails)'
    time_1 = timeit.timeit(setup=setup, stmt=stmt_1, number=num_iter)
    # print(time_1)
    time_2 = timeit.timeit(setup=setup, stmt=stmt_2, number=num_iter)
    # print(time_2)
    time_3 = timeit.timeit(setup=setup, stmt=stmt_3, number=num_iter)
    # print(time_3)
    times = [time_1, time_2, time_3]
    if time_1 == min(times):
        res = 'loop'
    elif time_2 == min(times):
        res = 'list comprehension'
    elif time_3 == min(times):
        res = 'map'
    times = sorted(times)
    print(f'it is better to use a {res}')
    print(f'{times[0]} vs {times[1]} vs {times[2]}')


if __name__ == '__main__':
    main()