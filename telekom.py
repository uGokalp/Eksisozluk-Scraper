from eksi_scraper.funcs import *

# Get list of entries and respective dates
turk_telekom = 'https://eksisozluk.com/turk-telekom--38478?nr=true&rf=turk%20telekom'
list_turk, list_date = get_with_method(turk_telekom)

# Ensure len(dates) == len(entries)
print("Length of list_date is", len(list_date))
print("Length of list_turk is", len(list_turk))

# Load to pandas DataFrame to export to csv
df_telekom = pd.DataFrame({'entry': list_turk, 'date': list_date})
df_telekom.to_csv('data/turk_telekom.csv')

# Create wordclouds from DataFrame and save to wordclouds/Turk_Telekom
plot_all(df_telekom, 'Turk_Telekom')
