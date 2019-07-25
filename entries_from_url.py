from eksi_scraper.funcs import *

url_list = ['https://eksisozluk.com/abdden-4-odul-alan-kisa-film--6119212',
            'https://eksisozluk.com/eski-olmasina-ragmen-hala-oynanan-oyunlar--6118935',
            'https://eksisozluk.com/kahramanmaras-vali-yardimcisinin-aciga-alinmasi--6119163',
            'https://eksisozluk.com/reynmenin-sarkisini-dinlememis-insan--5932469']

max_page, list_begin, list_end = gather_all(url_list)
to_scrape = dict(link=url_list, max_page=max_page)

entries = get_icerik(to_scrape)

titles = grab_titles(url_list)

df = pd.DataFrame(dict(title=titles, link=url_list, max_page=max_page, entry=entries))
df.to_csv('data/eksi.csv')
plot_all(df, 'eksi')
