# import requests
# from bs4 import BeautifulSoup

# def hent_aksjepris(selskap):
#     url = 'https://finance.yahoo.com/quote/'+ selskap +'?p=' + selskap + '&.tsrc=fin-srch'
#     page = requests.get(url)
#     #print(page.status_code)

#     soup = BeautifulSoup(page.text, 'html.parser')

#     price = soup.find('fin-streamer', {'class': 'Fw(b) Fz(36px) Mb(-4px) D(ib)'}).text
#     #print('Loading: ', url)
#     #print(price)
#     #print(hent_aksjepris(selskap))
#     pris = float(price)
#     return pris

# print(hent_aksjepris('AMZN'))

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

import requests
from bs4 import BeautifulSoup
def web_content_div(web_content, class_path):
    web_content_div = web_content.find_all("div", {"class": class_path})
    try:
        spans = web_content_div[0].find_all("span")
        texts = [span.get_text() for span in spans]
    except IndexError:
        texts = []
    return texts

def getData(symbol):
    url = 'https://finance.yahoo.com/quote/'+ symbol +'?p=' + symbol + '&.tsrc=fin-srch'
    # headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'}
    req = requests.get(url)
    soup = BeautifulSoup(req.text, 'html.parser')

    url_summary = 'https://money.cnn.com/quote/profile/profile.html?symb=' + symbol
    page_summary = requests.get(url_summary)
    #print(page.status_code)

    soup2 = BeautifulSoup(page_summary.text, 'html.parser')
    

    web_content = BeautifulSoup(req.text, "lxml")
    texts = web_content_div(web_content, "D(ib) Va(m) Maw(65%) Ov(h)")

    if texts != []:
        price, change, info = texts[0], texts[1], texts[2]
    else:
        price, change, info = [], [], []

    stock = {
        'company' : soup.find('h1', {'class': 'D(ib) Fz(18px)'}).text,
        'symbol' : symbol,
        'price' : soup.find('fin-streamer', {'class': 'Fw(b) Fz(36px) Mb(-4px) D(ib)'}).text,
        'change' : change,
        'info' : info,
        'summary' : soup2.find('div', {'id': 'wsod_companyDescription'}).text
        }
    return stock

print(getData('AAPL'))

# import requests
# from bs4 import BeautifulSoup
# def web_content_div(web_content, class_path):
#     web_content_div = web_content.find_all("section", {"class": class_path})
#     try:
#         spans = web_content_div[0].find_all("h1")
#         texts = [section.get_text() for section in spans]
#     except IndexError:
#         texts = []
#     return texts

# def getData(symbol):
#     url = 'https://finance.yahoo.com/quote/'+ symbol +'/profile/'
#     # headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'}
#     req = requests.get(url)
#     soup = BeautifulSoup(req.text, 'html.parser')

#     stock = {
#         'symbol' : symbol,
#         'price' : soup.find('fin-streamer', {'class': 'Fw(b) Fz(36px) Mb(-4px) D(ib)'}).text,
#         }
    
#     web_content = BeautifulSoup(req.text, "lxml")
#     texts = web_content_div(web_content, "Mt(15px) Lh(1.6)")

#     if texts != []:
#         price, change = texts[0], texts[1]
#     else:
#         price, change = [], []

#     return stock, change

# print(getData('AAPL'))



# import requests
# from bs4 import BeautifulSoup

# def hent_aksjepris(selskap):
#     url = 'https://money.cnn.com/quote/profile/profile.html?symb=' + selskap
#     page = requests.get(url)
#     #print(page.status_code)

#     soup = BeautifulSoup(page.text, 'html.parser')

#     price = soup.find('div', {'id': 'wsod_companyDescription'}).text
#     #print('Loading: ', url)
#     #print(price)
#     #print(hent_aksjepris(selskap))
#     return price

# print(hent_aksjepris('AAPL'))