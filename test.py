'''
import yfinance as yf
from datetime import datetime

ibm = yf.Ticker("IBM")

end_date = datetime.now().strftime('%Y-%m-%d')
ibm_history = ibm.history(start='2023-02-10',end=end_date)

print(ibm_history)

'''

import yfinance as yf

liste =[]
aapl= yf.Ticker("AAPL")
aapl_historical = aapl.history(start="2023-01-10", end="2023-02-10", interval="1d")

data = yf.download("AMZN AAPL", start="2017-01-01", end="2017-04-30", group_by='tickers')
print(type(data))



def hent_info(selskap):

    firma = yf.Ticker(selskap)
    praktisk_info = firma.info['sharesOutstanding']
    return praktisk_info
