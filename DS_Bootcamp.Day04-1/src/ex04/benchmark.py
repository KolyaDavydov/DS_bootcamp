import timeit
import random
from collections import Counter


def my_func(elems):
    my_dict = dict.fromkeys(set(elems), 0)
    for i in elems:
        if i in my_dict:
            my_dict[i] += 1
    return my_dict

def my_func_top(elems):
    my_dict = dict.fromkeys(set(elems), 0)
    for i in elems:
        if i in my_dict:
            my_dict[i] += 1
    sort = sorted(my_dict.items(), key=lambda item: item[1], reverse=True)
    return sort[:10]

def counter_func(elems):
    return dict(Counter(elems))

def counter_top_func(elems):
    return dict(Counter(elems).most_common(10))


def main():
    num_iter = 100
    setup = """
import random
from collections import Counter
from __main__ import my_func, my_func_top, counter_func, counter_top_func
elems = [random.randint(0,100) for i in range(1000000)]
    """
    time_1 = timeit.timeit(setup=setup, stmt='my_func(elems)', number=num_iter)
    time_2 = timeit.timeit(setup=setup, stmt='counter_func(elems)', number=num_iter)
    time_3 = timeit.timeit(setup=setup, stmt='my_func_top(elems)', number=num_iter)
    time_4 = timeit.timeit(setup=setup, stmt='counter_top_func(elems)', number=num_iter)
    print(f"my function: {time_1}")
    print(f"Counter: {time_2}")
    print(f"my top: {time_3}")
    print(f"Counter's top: {time_4}")


if __name__ == '__main__':
    main()
