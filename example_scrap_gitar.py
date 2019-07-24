from eksi_scraper.funcs import *

page_end = find_end_search('gitar')
print("Max page", page_end)
list_links, list_titles = titles_links('gitar', page_end)

list_max_pages = last_page_agg(list_links)
list_begin = start_date(list_links)

print(list_begin[:5])
list_end = end_date(list_links, list_max_pages)

print(list_end[:5])

starter_dict = dict(title=list_titles, link=list_links, max_page=list_max_pages)
list_icerik = get_icerik(starter_dict)
list_iceriks = list_icerik[0]

print("Length of icerik is", len(list_icerik))
print("Length of listend is", len(list_end))
print("Length of listbegin is", len(list_begin))
print("Length of maxpage is", len(list_max_pages))
print("Length of links is", len(list_links))
print("Length of title is", len(list_titles))

df_dict = dict(entry=list_icerik, listend=list_end, listbegin=list_begin, maxpage=list_max_pages,
               links=list_links, title=list_titles)
df = pd.DataFrame(df_dict)
df.to_csv('data/example_gitar.csv')

df_gitar = pd.read_csv('data/example_gitar.csv', index_col=0)
plot_all(df_gitar, 'Gitar')
