import bs4
import pandas as pd
import matplotlib.pyplot as plt
import datetime

from bs4 import BeautifulSoup as bs
from urllib.request import urlopen as uReq
from collections import Counter

#corona_link = 'https://github.com/CSSEGISandData/COVID-19/tree/master/csse_covid_19_data/csse_covid_19_daily_reports'

d = datetime.datetime.now()

date_csv = '0'+ str(d.month) + '-' + str(d.day) + '-' + str(d.year) + '.csv'

day_links = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/' + str(date_csv)

def access_Link(link):
    uClient = uReq(link)
    html = uClient.read()
    uClient.close()
    main_soup = bs(html, "lxml")

    for main in main_soup.find_all('body'):
        corona_data = main.get_text()

access_Link(day_links)

    



