import pandas as pd

lst =[5.7,75.2,74.4,84,66.5,66.3,55.8,75.7,29.1,43.7]

lista = pd.Series(lst)
print(lista[2])

b = [
    [53.1, 95.0, 67.5, 35.0, 78.4],
    [61.3, 40.8, 30.8, 37.8, 87.6],
    [20.6, 73.2, 44.2, 14.6, 91.8],
    [57.4, 0.1, 96.1, 4.2, 69.5],
    [83.6, 20.5, 85.4, 22.8, 35.9],
    [49.0, 69.0, 0.1, 31.8, 89.1],
    [23.3, 40.7, 95.0, 83.8, 26.9],
    [27.6, 26.4, 53.8, 88.8, 68.5],
    [96.6, 96.4, 53.4, 72.4, 50.1],
    [73.7, 39.0, 43.2, 81.6, 34.7]]

panda_b = pd.DataFrame(b)

colnames = ['score_1','score_2','score_3','score_4','score_5']
panda_b = pd.DataFrame(b, columns=colnames)
cortt = panda_b[['score_1','score_3','score_5']]
print(cortt)
print(panda_b['score_3'].mean())
print(panda_b['score_4'].mean())
print(panda_b['score_3'].median())

orders = {'Description': ['LUNCH BAG APPLE DESIGN',
                           'SET OF 60 VINTAGE LEAF CAKE CASES '
                           'RIBBON REEL STRIPES DESIGN ',
                           'WORLD WAR 2 GLIDERS ASSTD DESIGNS',
                           'PLAYING CARDS JUBILEE UNION JACK',
                           'POPCORN HOLDER',
                           'BOX OF VINTAGE ALPHABET BLOCKS',
                           'PARTY BUNTING',
                           'JAZZ HEARTS ADDRESS BOOK',
                           'SET OF 4 SANTA PLACE SETTINGS'],
              'Quantity':[1, 24, 1, 2880, 2, 7, 1, 4, 10, 48],
              'UnitPrice':[1.65, 0.55, 1.65, 0.18, 1.25, 0.85, 11.95, 4.95, 0.19, 1.25],
              'Revenue':[1.65, 13.2, 1.65, 518.4, 2.5, 5.95, 11.95, 19.8, 1.9, 60.0]}

ordenes = pd.DataFrame.from_dict(orders)
print(ordenes)

amount = ordenes['Quantity'].sum()
print()
print(amount)
profit = ordenes['Revenue'].sum()
print()
print(profit)

expensive = orders['UnitPrice'].max()
print()
print(expensive)

cheaper = orders['UnitPrice'].min()
print()
print(cheaper)

difference = expensive - cheaper
print()
print(difference)