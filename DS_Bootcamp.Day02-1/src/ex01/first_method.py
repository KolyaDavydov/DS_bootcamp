# Пример запуска скрипта:
# python3 first_method.py

class Research:
    def file_reader(self):
        with open('data.csv', 'r') as f:
            text = f.read()
        return text


if __name__ == '__main__':
    r = Research()
    print(r.file_reader())
