from funcs import *

df_gitar = pd.read_csv('example_gitar2.csv', index_col=0)
plot_all(df_gitar, 'Gitar')
