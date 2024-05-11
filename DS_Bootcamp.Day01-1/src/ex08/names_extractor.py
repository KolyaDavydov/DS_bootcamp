# Запустить скрипт"
# python3 names_extractor.py emails.txt
import sys


def name_extractor(file_path):
    with open(file_path, 'r') as emails:
        with open('employees.tsv', 'w') as employees:
            employees.write('Name\tSurname\tE-mail\n')
            for line in emails:
                temp = line.split('@')[0].split('.')
                name = temp[0].capitalize()
                surname = temp[1].capitalize()
                employees.write(f'{name}\t{surname}\t{line}')


if __name__ == '__main__':
    if len(sys.argv) == 2:
        name_extractor(sys.argv[1])
    else:
        print('Нужен аргумент - путь к файлу. Например:')
        print('python names_extractor.py email.txt')
