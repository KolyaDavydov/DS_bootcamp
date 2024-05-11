# Пример запуска скрипта:
# python3 letter_starter.py ivan.petrov@corp.com

import sys


def letter_starter(email):
    with open('employees.tsv', 'r') as input:
        for line in input:
            data = line.split('\t')
            # print(data)
            if data[2].strip('\n') == email:
                return f'Dear {data[0]}, welcome to our team. We are sure that it will be a pleasure to work with you. That’s a precondition for the professionals that our company hires.'
            else:
                continue


if __name__ == '__main__':
    if len(sys.argv) == 2:
        print(letter_starter(sys.argv[1]))
    else:
        print('Нужен аргумент - путь к файлу. Например:')
        print('python letter_starter.py email.txt')