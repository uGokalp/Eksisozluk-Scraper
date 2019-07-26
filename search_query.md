# Gather entries from search query
1. Import funcs module ``` from scraper.funcs import *```
2. Find the last page of query with find_end_search ``` page_end = find_end_search('turkcell')```
3. Get titles and links with titles_links ```list_links, list_titles = titles_links('turkcell', page_end)```
``
4. Get the last page of each link
```page_end = find_end_search('turkcell')```
5. Get the first entry date
```list_begin = start_date(list_links)```
6. Get the last entry date 
```list_end = end_date(list_links, list_max_pages)```
7. Create a dictionary with keys title,link,max_page
```starter_dict = dict(title=list_titles, link=list_links, max_page=list_max_pages)```
8. Grab entries from each url with get_icerik
```list_icerik = get_icerik(starter_dict)```
9. Combine the results in a dictionary
``` df_dict = dict(entry=list_icerik, listend=list_end, listbegin=list_begin, maxpage=list_max_pages,links=list_links, title=list_titles) ```
10. pass the dictionary to a DataFrame
```df_turkcell = pd.DataFrame(df_dict)```
11. Export csv using to.csv method
```df_turkcell.to_csv('data/turkcell.csv')```
12. (Optional) pass DataFrame to plot_all() to plot wordcloud for each title
```plot_all(df_turkcell, 'turkcell')```

[turkcell.py](https://github.com/uGokalp/Eksisozluk-Scraper/blob/0.1.0/turkcell.py)
