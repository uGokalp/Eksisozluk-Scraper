from eksi_scraper.funcs import *

df_vodafone = pd.read_csv('data/vodafone.csv', index_col=0)
plot_all(df_vodafone, 'Vodafone')
