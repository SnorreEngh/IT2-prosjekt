import yfinance as yf
import pandas as pd
# import matplotlib.pyplot as plt
# from datime import dateime 
# plt.style.use('seaborn')

msft = yf.Ticker("msft")
print(msft.info)