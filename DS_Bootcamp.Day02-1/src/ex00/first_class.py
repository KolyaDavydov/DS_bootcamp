# Пример запуска скрипта:
# python3 first_class.py

class Must_read:
    with open('data.csv', 'r') as f:
        print(f.read())


if __name__ == '__main__':
    Must_read()