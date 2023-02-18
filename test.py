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
    print(firma)
    return firma
hent_info("AAPL")

def info(selskap):
    msft = yf.Ticker(selskap)
    print(msft.info)
    return msft.info
info("msft")

'''
zip : 98052-6399
sector : Technology
fullTimeEmployees : 221000
longBusinessSummary : Microsoft Corporation develops, licenses, and supports software, services, devices, and solutions worldwide. The company operates in three segments: Productivity and Business Processes, Intelligent Cloud, and More Personal Computing. The Productivity and Business Processes segment offers Office, Exchange, SharePoint, Microsoft Teams, Office 365 Security and Compliance, Microsoft Viva, and Skype for Business; Skype, Outlook.com, OneDrive, and LinkedIn; and Dynamics 365, a set of cloud-based and on-premises business solutions for organizations and enterprise divisions. The Intelligent Cloud segment licenses SQL, Windows Servers, Visual Studio, System Center, and related Client Access Licenses; GitHub that provides a collaboration platform and code hosting service for developers; Nuance provides healthcare and enterprise AI solutions; and Azure, a cloud platform. It also offers enterprise support, Microsoft consulting, and nuance professional services to assist customers in developing, deploying, and managing Microsoft server and desktop solutions; and training and certification on Microsoft products. The More Personal Computing segment provides Windows original equipment manufacturer (OEM) licensing and other non-volume licensing of the Windows operating system; Windows Commercial, such as volume licensing of the Windows operating system, Windows cloud services, and other Windows commercial offerings; patent licensing; and Windows Internet of Things. It also offers Surface, PC accessories, PCs, tablets, gaming and entertainment consoles, and other devices; Gaming, including Xbox hardware, and Xbox content and services; video games and third-party video game royalties; and Search, including Bing and Microsoft advertising. The company sells its products through OEMs, distributors, and resellers; and directly through digital marketplaces, online stores, and retail stores. Microsoft Corporation was founded in 1975 and is headquartered in Redmond, Washington.
city : Redmond
phone : 425 882 8080
state : WA
country : United States
companyOfficers : []
website : https://www.microsoft.com
maxAge : 1
address1 : One Microsoft Way
fax : 425 706 7329
industry : Software—Infrastructure
ebitdaMargins : 0.4799
profitMargins : 0.33048
grossMargins : 0.68160003
operatingCashflow : 84385996800
revenueGrowth : 0.02
operatingMargins : 0.40969002
ebitda : 97945001984
targetLowPrice : 212
recommendationKey : buy
grossProfits : 135620000000
freeCashflow : 44613373952
targetMedianPrice : 285
earningsGrowth : -0.113
currentRatio : 1.931
returnOnAssets : 0.14826
numberOfAnalystOpinions : 45
targetMeanPrice : 285.51
debtToEquity : 42.583
returnOnEquity : 0.39312
targetHighPrice : 348
totalCash : 99495002112
totalDebt : 77984997376
totalRevenue : 204093997056
totalCashPerShare : 13.366
financialCurrency : USD
revenuePerShare : 27.327
quickRatio : 1.656
recommendationMean : 1.8
shortName : Microsoft Corporation
longName : Microsoft Corporation
isEsgPopulated : False
gmtOffSetMilliseconds : -18000000
messageBoardId : finmb_21835
market : us_market
annualHoldingsTurnover : None
enterpriseToRevenue : 9.456
beta3Year : None
enterpriseToEbitda : 19.704
morningStarRiskRating : None
forwardEps : 10.73
revenueQuarterlyGrowth : None
sharesOutstanding : 7443800064
fundInceptionDate : None
annualReportExpenseRatio : None
totalAssets : None
bookValue : 24.592
sharesShort : 35766440
sharesPercentSharesOut : 0.0047999998
fundFamily : None
lastFiscalYearEnd : 1656547200
heldPercentInstitutions : 0.73704004
netIncomeToCommon : 67448999936
trailingEps : 9
lastDividendValue : 0.68
SandP52WeekChange : -0.059431553
priceToBook : 10.474138
heldPercentInsiders : 0.00057
nextFiscalYearEnd : 1688083200
yield : None
mostRecentQuarter : 1672444800
shortRatio : 1.07
sharesShortPreviousMonthDate : 1672358400
floatShares : 7437029672
beta : 0.91562
enterpriseValue : 1929883156480
priceHint : 2
threeYearAverageReturn : None
lastSplitDate : 1045526400
lastSplitFactor : 2:1
legalType : None
lastDividendDate : 1676419200
morningStarOverallRating : None
earningsQuarterlyGrowth : -0.125
priceToSalesTrailing12Months : 9.394563
dateShortInterest : 1675123200
pegRatio : 2.38
ytdReturn : None
forwardPE : 24.005592
lastCapGain : None
shortPercentOfFloat : 0.0047999998
sharesShortPriorMonth : 38191521
impliedSharesOutstanding : 0
category : None
fiveYearAverageReturn : None
trailingAnnualDividendYield : 0.009917986
payoutRatio : 0.28219998
navPrice : None
trailingAnnualDividendRate : 2.6
toCurrency : None
expireDate : None
algorithm : None
dividendRate : 2.72
exDividendDate : 1676419200
circulatingSupply : None
startDate : None
trailingPE : 28.619999
lastMarket : None
maxSupply : None
openInterest : None
volumeAllCurrencies : None
strikePrice : None
ask : 257.53
askSize : 2200
fromCurrency : None
fiveYearAvgDividendYield : 1.14
bid : 257.55
tradeable : False
dividendYield : 0.0104
bidSize : 800
coinMarketCapLink : None
preMarketPrice : 259.2
logo_url : https://logo.clearbit.com/microsoft.com
trailingPegRatio : 2.277
'''