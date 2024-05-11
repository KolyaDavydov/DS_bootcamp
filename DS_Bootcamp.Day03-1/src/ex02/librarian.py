import os

def main():
    try:
        if os.environ['VIRTUAL_ENV'][-8:] == 'almetate':
            # raise Exception("Неправильное окружение")
            os.system('pip install Beautifulsoup4 pytest')
            os.system('pip freeze')
            os.system('pip freeze > requirements.txt')
    except KeyError:
        print('Неверное окружение')
    return

if __name__ == '__main__':
    main()