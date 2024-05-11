import sys


def get_price(company_ticker: str):
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

    if company_ticker not in STOCKS:
        print('Unknown ticker')
    else:
        for item in COMPANIES:
            if COMPANIES[item] == company_ticker:
                print(item, STOCKS[company_ticker])



if __name__ == '__main__':
    if len(sys.argv) == 2:
        get_price(sys.argv[1].upper())
    else:
        print('В качестве аргумента введите название одной компании')