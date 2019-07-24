# Scraper
 
### Prerequistes:
- Requirements.txt

### Sample workflow
#### Gather entries from a list of urls
1. Start by importing funcs
```python 
from eski-scraper.funcs import * 
```
2. Assign gather_all function to 3 variables
``` python
max_page, list_begin, list_end = gather_all(url_list)
```
3. Create a dictionary with keys 'link' and 'max_page'
``` python
to_scrape = dict(link=url_list,max_page=max_page)
```
4. Pass the dictionary to get_icerik
``` python
entries = get_icerik(to_scrape)
```
6. Scrape titles from urls
``` python
titles = grab_titles(url_list)
```
5. Load to DataFrame
``` python
df = pd.Dataframe(dict(title=titles,link=url_list,max_page=max_page,entry=entries)
``` 
6. Export to csv
```
df.to_csv('eksi.csv')
```
7. (Optional) Plot a wordcloud with a specified name and directory in /wordcloud
``` python
plot_wordcloud(text=df,names='eksi', foldername='eksi')
```
