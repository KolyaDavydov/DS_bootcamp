import sys


def get_price(company_name: str):
    COMPANIES = {
    'Apple': 'AAPL',
    'Microsoft': 'MSFT',
    'Netflix': 'NFLX',
    'Tesla': 'TSLA',
    'Nokia': 'NOK'
    }

    STOCKS = {
    'AAPL': 287.73,
    'MSFT': 173.79,
    'NFLX': 416.90,
    'TSLA': 724.88,
    'NOK': 3.37
    }

    if company_name not in COMPANIES:
        print('Unknown company')
    else:
        print(STOCKS[COMPANIES[company_name]])


if __name__ == '__main__':
    if len(sys.argv) == 2:
        get_price(sys.argv[1].capitalize())
    else:
        print('В качестве аргумента введите название щдной компании')
