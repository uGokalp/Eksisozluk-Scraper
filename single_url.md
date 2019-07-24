# Gather Entries from single url
1. Import funcs module 
`from scraper.funcs import *`
2. Call get_with_method and assign to two variables. This will grab each entry and entry date from the url.
```python
 list_entry, list_date = get_with_method(url, method = 'all')
 ```
- Optionally method could be set to `'input'` where the user can define the range.
3. Wrap the resulting lists with dict() and serve to pandas DataFrame
```python
df = pd.DataFrame(dict(entry=list_entry,date='list_date))
```
4. (Optional) Use plot_wordcloud to quickly plot a wordcloud
`plot_wordcloud(text=df, names='Tutorial', folder_name='Tutorial')`
