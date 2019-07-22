from funcs import *

garanti = 'https://eksisozluk.com/garanti-bankasi--72619'
list_garanti, list_date = get_with_method(garanti,method='debug')

list_garanti[0],list_date[0]
df = pd.DataFrame({'entry': list_garanti, 'date': list_date})
df.to_csv('garanti_banksi.csv')

