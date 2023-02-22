import requests
from bs4 import BeautifulSoup

def hent_aksjepris(selskap):
    url = 'https://finance.yahoo.com/quote/'+ selskap +'?p=' + selskap + '&.tsrc=fin-srch'
    page = requests.get(url)
    print(page.status_code)

    soup = BeautifulSoup(page.text, 'html.parser')

    price = soup.find('fin-streamer', {'class': 'Fw(b) Fz(36px) Mb(-4px) D(ib)'}).text
    print('Loading: ', url)
    print(price)
    return selskap
print(hent_aksjepris('AMZN'))

'''
import requests
from bs4 import BeautifulSoup

def getData(symbol):
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'}
    url = 'https://uk.finance.yahoo.com/quote/' + symbol
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, 'html.parser')
    stock = {
        'symbol' : symbol,
        'price' : soup.find('div', {'class': 'D(ib) Mend(20px)'}).find_all('fin-streamer')[0].text,
        'change' : soup.find('div', {'class': 'D(id) Mend(20px)'}).find_all('fin-streamer')[1].text
        }
    return stock

print(getData('AAPL'))
'''