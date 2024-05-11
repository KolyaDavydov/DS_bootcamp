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


def main():
    setup = """
from __main__ import loop, list_comprehension
emails = 5 * ['john@gmail.com', 'james@gmail.com',
'alice@yahoo.com', 'anna@live.com', 'philipp@gmail.com']
    """
    stmt_1 = 'loop(emails)'
    stmt_2 = 'list_comprehension(emails)'
    time_1 = timeit.timeit(setup=setup, stmt=stmt_1, number=9000000)
    time_2 = timeit.timeit(setup=setup, stmt=stmt_2, number=9000000)
    if time_1 < time_2:
        res = 'loop'
    else:
        res = 'list comprehension'
    time_sorted = sorted([time_1, time_2])
    print(f'it is better to use a {res}')
    print(f'{time_sorted[0]} vs {time_sorted[1]}')


if __name__ == '__main__':
    main()