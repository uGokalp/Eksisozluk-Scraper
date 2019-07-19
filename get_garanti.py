from funcs import *

garanti = 'https://eksisozluk.com/garanti-bankasi--72619'
list_garanti, list_date = grab_hard(garanti)

df = pd.DataFrame({'entry': list_garanti, 'date': list_date})
df.to_csv('garanti2.csv')

algo = 'https://eksisozluk.com/garanti-bankasi-sira-bekleme-algoritmasi--6080093'
list_algo, date_algo = grab_hard(algo, method='all')
df = pd.DataFrame({'entry': list_algo, 'date': date_algo})
df.to_csv('algo.csv')
