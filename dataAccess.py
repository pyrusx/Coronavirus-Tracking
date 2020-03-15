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

data_url = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/'


#~ access_Links retrieves the data in string form 
def read_url(url):
        uClient = uReq(url)
        html = uClient.read()
        uClient.close()
        main_soup = bs(html, "lxml")

        return main_soup.body.get_text()


#~ get the proper link based on the date
def get_link_for_date(date):
    return data_url + date.strftime("%m-%d-%Y.csv")


#~ access previous link if today's data has not been added 
def get_latest_data():
    #~ Get current time 
    dt = datetime.datetime.today()
    for _ in range(20):
        try:
            return read_url(get_link_for_date(dt))
        except:
            dt = dt - timedelta(days=1)

    #TODO Find exception syntax        

print(get_latest_data())

#// #TODO Make yesterday/today error go away\

# #// #! error: main_df does not print properly, something is going wrong from line 68-75, need to figure out how to make functions work together

# #TODO make the code go back to the last accessible date if yesterday also does not have data
# #TODO Figure out how to return the \t print statement
#// # #TODO change Province/State to State and Country/Region to Country
# #TODO allow for user input ie "Which Country do you want to see"
# #TODO interactive charts with the data: bokeh, plotly, pygal, mpld3, holoviews, geoplotlib
