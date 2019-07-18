import requests
import re
import pandas as pd
from bs4 import BeautifulSoup
from time import sleep
from tqdm import tqdm
import matplotlib.pyplot as plt
import seaborn as sns
import random
from collections import OrderedDict
import numpy as np
import csv

# TODO: Load from Checkpoint
# TODO: get icerik

headers_1 = {"User-Agent": "Mozilla/5.0"}


# Find the last page of given link
def find_end(url):
    end_r = requests.get(url, headers=headers_1)
    soup_end = BeautifulSoup(end_r.content, 'html.parser')
    page_end = re.findall(re.compile('(?:\D*(\d+)){2}'), str(soup_end.find_all("div", class_='pager')))
    try:
        page_end = int(page_end[0])
    except:
        page_end = 0

    return page_end


# Return titles and links for searchedtitle
def titles_links(baslik_search, page_end):
    '''

    :param baslik_search: string -> specific to search query
    :param page_end: integer -> should be passed from find_end(url)
    :return: list_links -> lists of links, list_zero -> lists of titles
    '''
    domain = 'https://eksisozluk.com'
    list_links = []
    list_zero = []
    print('Scraping started')
    for i in tqdm(range(1, 3)):
        url = 'https://eksisozluk.com/basliklar/ara?SearchForm.Keywords=' + baslik_search + '&SearchForm.NiceOnly=false&SearchForm.SortOrder=Date&p=' + str(
            i)
        # print(url)
        get_request = requests.get(url, headers=headers_1)
        search_soup = BeautifulSoup(get_request.content, 'html.parser')
        baslik_link = search_soup.find("section", {"id": "content-body"}).find('ul', {'class': 'topic-list'})
        baslik_href = search_soup.find("section", {"id": "content-body"})
        search_baslik = baslik_href.find('ul', {'class': 'topic-list'}).find_all('a')
        entry_link = [domain + li.find('a')['href'] if li.find('a') else None for li in baslik_link.find_all('li') if
                      li.text.strip() != '']
        list_links.append(entry_link)
        entry_baslik = [' '.join(y.text.split()[:-1]).strip() for y in search_baslik]
        list_zero.append(entry_baslik)
        # sleep(random.randint(0,2))
    list_links = [item for sublist in list_links for item in sublist]
    list_zero = [item for sublist in list_zero for item in sublist]
    print('Scraping ended')
    return list_links, list_zero


def last_page_agg(url_list):
    '''

    :param url_list: List -> input list of urls
    :return: last page for each url
    '''
    print('Gathering max pages for each url')
    max_page = []
    for url in tqdm(url_list):
        page = find_end(url)
        max_page.append(page)
    print('Done')
    return max_page


def start_date(list_links):
    print('Gathering start date for each title')
    list_begin = []
    for i in tqdm(list_links):
        r = requests.get(i, headers=headers_1)
        soup_try = BeautifulSoup(r.content, 'html.parser')
        try:
            begin = [i.strip()[:10] for i in
                     soup_try.find('div', {'id': 'content'}).find('div', {'class': 'info'}).find('a', {
                         'class': 'entry-date permalink'})]
        except:
            begin = ['0']
        list_begin.append(begin)
    print('Done')
    return list_begin


def end_date(list_links, max_page):
    '''

    :param list_links:
    :param max_page:
    :return:
    '''
    print('Gathering start date for each title')
    list_end = []
    for link, page in tqdm(zip(list_links, max_page), total=len(list_links)):
        url = link + '?p=' + str(page)
        r = requests.get(url, headers=headers_1)
        soup_try = BeautifulSoup(r.content, 'html.parser')
        try:
            end = [i.strip()[:10] for i in
                   soup_try.find('div', {'id': 'content'}).find('div', {'class': 'info'}).find('a', {
                       'class': 'entry-date permalink'})]
        except:
            end = ['0']
        list_end.append(end)
    print('Done')
    return list_end


def checkpoint_one(list_link, list_zero, max_page, list_begin, list_end):
    print('Writing checkpoint 1 to csv')
    with open("checkpoint_one.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows([list_link, list_zero, max_page, list_begin, list_end])
    print('Done')


def get_icerik(new_dict):
    '''

    :param new_dict:
    :return:
    '''
    print('Started scraping icerik')
    dict_edit = []
    list_edit = []
    for url,page_max in tqdm(zip(new_dict.get('link'),new_dict.get('max_page')),total=len(new_dict.get('link'))):  # type: (object, object)
        list_edit = []
        for i in range(1,2):
            urls = url + '?p=' + str(i)
            r = requests.get(url, headers=headers_1)
            soup_try = BeautifulSoup(r.content, 'html.parser')
            #     text = soup_try.find('div',class_='content').text.strip().split(';')
            try:
                text_edit = [i.text.strip().split(';') for i in soup_try.find_all('div', class_='content')]
            except AttributeError:
                text_edit = [str(i.string).strip() for i in soup_try.find('div', class_='content')]
            #             text_edit = [i for i in text_edit if i != 'None']
            except TypeError:
                text_edit = ['Problem']
            list_edit.append(text_edit)
            sleep(random.randint(0, 2))
        dict_edit.append(list_edit)
    print('Done')
    return dict_edit