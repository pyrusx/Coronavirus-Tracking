import bs4
import pandas as pd
import matplotlib.pyplot as plt
import datetime
import sys
import csv

if sys.version_info[0] < 3: 
    from StringIO import StringIO
else:
    from io import StringIO

from datetime import date, timedelta
from io import StringIO
from bs4 import BeautifulSoup as bs
from urllib.request import urlopen as uReq
from collections import Counter

from coronavirus_daily import access_Link


confirmed = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_19-covid-Confirmed.csv'
deaths = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_19-covid-Deaths.csv'
recovered = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_19-covid-Recovered.csv'


print(access_Link(confirmed))
# def access_Link(link):
#         uClient = uReq(link)
#         html = uClient.read()
#         uClient.close()
#         main_soup = bs(html, "lxml")

#         return main_soup.body.get_text()
    

# def str_df(link):

#     #~ saving the data to a variable
#     confirmed_csv = access_Link(confirmed)


#     convertedCSV = StringIO(csv_string)
#     df = pd.read_csv(convertedCSV, sep =",") 
#     print(df)

# str_df()