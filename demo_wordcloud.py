from funcs import *
from collections import Counter

df = pd.read_csv('garanti_banksi.csv', index_col=0)

plot_wordcloud(df['entry'], title='Garanti', background_color='White')
list_of_text = [i.strip().split() for i in df['entry']]
list_of_text = [i[0] for i in list_of_text]
list_of_text = [i for i in list_of_text if i not in stopwords_1]
print(Counter(list_of_text))
