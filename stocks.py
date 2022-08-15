from features.stocks_data_class import StocksDataClass

wig20list = [
    ('ALLEGRO', 'ale'),
    ('ASSECOPOL', 'acp'),
    ('CCC', 'ccc'),
    ('CDPROJEKT', 'cdr'),
    ('CYFRPLSAT', 'cps'),
    ('DINOPL', 'dnp'),
    ('JSW', 'jsw'),
    ('KETY', 'kty'),
    ('KGHM', 'kgh'),
    ('LPP', 'lpp'),
    ('MBANK', 'mbk'),
    ('ORANGEPL', 'opl'),
    ('PEKAO', 'peo'),
    ('PEPCO', 'pco'),
    ('PGE', 'pge'),
    ('PGNIG', 'pgn'),
    ('PKNORLEN', 'pkn'),
    ('PKOBP', 'pko'),
    ('PZU', 'pzu'),
    ('SANPL', 'spl')
    ]

class Stock():
    name = {
        'name':'',
        'ticker':'',
    }
    date = ''
    quotes = {
        'open':0,
        'high':0,
        'low':0,
        'close':0,
        'daily change':0,
        'volume':0
    }
    results = {
        'przychody netto':0,
        'zysk operacyjny':0,
        'zysk brutto':0,
        'zysk netto':0,
        'amortyzacja':0,
        'ebitda':0,
        'aktywa':0,
        'kapital':0,
        'liczba akcji':0,
        'zysk na akcje':0,
        'wartosc akcji':0
    }
    indicators = {
        'P/E':0,     # price/earnings -cena zysk - liczba akcji*kurs akcji/zysk netto
        'P/EBID':0,  # prince/EBIT (Earnings Before Interest and Tax) -cena zysk operacyjny - liczba akcji*kurs akcji/zysk operacyjny
        'ROE':0,     # return on equity - rentowność kapitału własnego - zysk netto/kapital*100%
        'ROA':0,     # return on assets – wskaźnik rentowności aktywów - zysk netto/aktywa*100%
        'ROS':0      # return on sales - marza zysku operacyjnego - zysk operacyjny/przychody netto*100%
    }
    
    

for index, stock in enumerate(wig20list):
    dataHandler = StocksDataClass(wig20list[index][0],wig20list[index][1])
    dataHandler.load_data()


stockData = StocksDataClass(wig20list[0][0], wig20list[0][1])
stockData.load_data()

stock = Stock()


stock.name['name'] = stockData.name
stock.name['ticker'] = stockData.ticker
stock.date = stockData.stockQuotesHandler.data['Date'][0]
stock.quotes['open'] = stockData.stockQuotesHandler.data['Open'][0]
stock.quotes['high'] = stockData.stockQuotesHandler.data['High'][0]
stock.quotes['low'] = stockData.stockQuotesHandler.data['Low'][0]
stock.quotes['close'] = stockData.stockQuotesHandler.data['Close'][0]
#stock.quotes['daily change'] = stockData.stockQuotesHandler.data['Daily Change][0]
stock.quotes['volume'] = stockData.stockQuotesHandler.data['Volume'][0]

# for index, res in enumerate(stock.results):
#     res = stockData.financialResultsHandler.data.iloc[index+1, 5]
#     print(stockData.financialResultsHandler.data.iloc[index+1, 5])
    
stock.results['przychody netto'] = stockData.financialResultsHandler.data.iloc[1,5]
stock.results['zysk operacyjny'] = stockData.financialResultsHandler.data.iloc[2,5]
stock.results['zysk brutto'] = stockData.financialResultsHandler.data.iloc[3,5]
stock.results['zysk netto'] = stockData.financialResultsHandler.data.iloc[4,5]
stock.results['amortyzacja'] = stockData.financialResultsHandler.data.iloc[5,5]
stock.results['ebitda'] = stockData.financialResultsHandler.data.iloc[6,5]
stock.results['aktywa'] = stockData.financialResultsHandler.data.iloc[7,5]
stock.results['kapital'] = stockData.financialResultsHandler.data.iloc[8,5]
stock.results['liczba akcji'] = stockData.financialResultsHandler.data.iloc[9,5]
stock.results['zysk na akcje'] = stockData.financialResultsHandler.data.iloc[10,5]
# stock.results['wartosc akcji':] = stockData.financialResultsHandler.data.iloc[11,5]

stock.indicators['P/E'] = 10*stock.results['liczba akcji']/stock.results['zysk netto']
stock.indicators['P/EBID'] = stock.quotes['close']*stock.results['liczba akcji']/stock.results['zysk operacyjny']
stock.indicators['ROE'] = stock.results['zysk netto']/stock.results['kapital']*100
stock.indicators['ROE'] = stock.results['zysk netto']/stock.results['aktywa']*100
stock.indicators['ROE'] = stock.results['zysk operacyjny']/stock.results['przychody netto']*100

# print(stock.name)
# print(stock.date)
# print(stock.quotes)
print(stock.results['przychody netto'])
print(stock.results['zysk na akcje'])

