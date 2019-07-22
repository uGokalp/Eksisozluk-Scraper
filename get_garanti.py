from funcs import *

garanti = 'https://eksisozluk.com/garanti-bankasi--72619'
list_garanti, list_date = get_with_method(garanti, method='all')

print("Length of list_date is", len(list_date))
print("Length of list_garanti is", len(list_garanti))
df = pd.DataFrame({'entry': list_garanti, 'date': list_date})
df.to_csv('garanti_banksi.csv')

