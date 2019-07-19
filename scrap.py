from typing import List

from funcs import *

vodafone_url = 'https://eksisozluk.com/basliklar/ara?SearchForm.Keywords=vodafone&SearchForm.NiceOnly=false&SearchForm.SortOrder=Date&p=2'

last_page = find_end(vodafone_url)
print("Last page =", last_page)

list_links, list_zero = titles_links('vodafone', last_page)

list_max_pages = last_page_agg(list_links)  # type: List[int]
list_begin = start_date(list_links)
list_begin = [i[0] for i in list_begin]
print(list_begin[:5])
list_end = end_date(list_links, list_max_pages)
list_end = [i[0] for i in list_end]
print(list_end[:5])

checkpoint_one(list_links, list_zero, list_max_pages, list_begin, list_end)
new_dict = dict(title=list_zero, link=list_links, max_page=list_max_pages)
dict_edit = get_icerik(new_dict)
csv_dict = {'titles': list_zero, 'links': list_links, 'max_page': list_max_pages,
            'begin': list_begin, 'end': list_end, 'entry': dict_edit}

df = pd.DataFrame({'titles': list_zero, 'links': list_links, 'max_page': list_max_pages,
                   'begin': list_begin, 'end': list_end, 'entry': [i[0] for i in dict_edit]})
df.to_csv('check_two.csv')

'''print('Writing checkpoint 2 to csv')
with open("checkpoint_two.csv", "w", newline="") as f:
    fieldnames = ['titles', 'links', 'max_page', 'begin', 'end', 'entry']
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow(
        {'titles': list_zero, 'links': list_links, 'max_page': list_max_pages,
         'begin': list_begin, 'end': list_end, 'entry': dict_edit})
'''
