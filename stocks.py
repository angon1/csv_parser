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
        'C/Z':0,     # cena zysk - liczba akcji*kurs akcji/zysk netto
        'C/Zo':0,    # cena zysk operacyjny - liczba akcji*kurs akcji/zysk operacyjny
        'ROE':0,     # return on equity - rentowność kapitału własnego - zysk netto/kapital*100%
        'ROA':0,     # return on assets – wskaźnik rentowności aktywów - zysk netto/aktywa*100%
        'ROS':0      # return on sales - marza zysku operacyjnego - zysk operacyjny/przychody netto*100%
    }
    
    

for index, stock in enumerate(wig20list):
    dataHandler = StocksDataClass(wig20list[index][0],wig20list[index][1])
    dataHandler.load_data()