import bs4
import pandas as pd
import matplotlib.pyplot as plt
import datetime
import sys
import csv
import numpy as np 

# if using python 2
if sys.version_info[0] < 3: 
    from StringIO import StringIO
else:
    from io import StringIO

from datetime import date, timedelta
from io import StringIO
from bs4 import BeautifulSoup as bs
from urllib.request import urlopen as uReq

from dataAccess.py import get_latest_data

#~ str_df converts the data in string format to dataframe format
def create_plots(data):

    #~ saving the data to a variable
    csv_string = get_latest_data()

    convertedCSV = StringIO(csv_string)
    df = pd.read_csv(convertedCSV, sep =",") 
    df = df.rename({'Province/State': 'State', 'Country/Region': 'Country'}, axis=1)
    

    df_STATE_CRD = df[[str(State), 'Confirmed', 'Deaths', 'Recovered']]

    ax = plt.gca()

    df.groupby('state')['name'].nunique().plot(kind='line',x='Country',y='Confirmed',ax=ax)
    df_COUNTRY_CDR.plot(kind='line',x='Country',y='Deaths', color='red', ax=ax)
    df_COUNTRY_CDR.plot(kind='line',x='Country',y='Recovered', color='green', ax=ax)
    plt.savefig('country.pdf')
