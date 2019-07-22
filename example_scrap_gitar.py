from funcs import *

page_end = find_end_search('gitar')
print("Max page", page_end)
list_links, list_titles = titles_links('gitar', page_end)

list_max_pages = last_page_agg(list_links)
list_begin = start_date(list_links)
list_begin = [i[0] for i in list_begin]
print(list_begin[:5])
list_end = end_date(list_links, list_max_pages)
list_end = [i[0] for i in list_end]
print(list_end[:5])

starter_dict = dict(title=list_titles, link=list_links, max_page=list_max_pages)
list_icerik = get_icerik(starter_dict)

df_dict = dict(entry=[i[0] for i in list_icerik], listend=list_end, listbegin=list_begin, maxpage=list_max_pages,
               links=list_links, title=list_titles)
df = pd.DataFrame(df_dict)
df.to_csv('example_gitar.csv')
