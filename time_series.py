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

from coronavirus_daily import access_Link

confirmed = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_19-covid-Confirmed.csv'
deaths = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_19-covid-Deaths.csv'
recovered = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_19-covid-Recovered.csv'



def plotting():
    confirmedCSV = access_Link(confirmed)
    deathsCSV = access_Link(deaths)
    recoveredCSV = access_Link(recovered)

    C = StringIO(confirmedCSV)
    D = StringIO(deathsCSV)
    R = StringIO(recoveredCSV)

    dfC1 = pd.read_csv(C, sep =",") 
    dfD1 = pd.read_csv(D, sep =",") 
    dfR1 = pd.read_csv(R, sep =",") 
    
    dfC = dfC1.rename({'Province/State': 'State', 'Country/Region': 'Country'}, axis=1)
    dfD = dfD1.rename({'Province/State': 'State', 'Country/Region': 'Country'}, axis=1)
    dfR = dfR1.rename({'Province/State': 'State', 'Country/Region': 'Country'}, axis=1)

    dfC.plot()
    plt.savefig('timeseries.pdf')
plotting()

