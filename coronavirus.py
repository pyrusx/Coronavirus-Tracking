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


from io import StringIO
from bs4 import BeautifulSoup as bs
from urllib.request import urlopen as uReq
from collections import Counter

# Link to the Github of CSV files from JHU = 'https://github.com/CSSEGISandData/COVID-19/tree/master/csse_covid_19_data/csse_covid_19_daily_reports'

#~ Get time 
d = datetime.datetime.now()

#~ Todays Date + .csv extension for today_links
today_date_csv = '0'+ str(d.month) + '-' + str(d.day) + '-' + str(d.year) + '.csv'

#~ Yesterday Date + .csv extension for yesterday_links

yesterday_date_csv = '0'+ str(d.month) + '-' + str(int(d.day) - 1) + '-' + str(d.year) + '.csv'

#~ todays_links and yesterday_links to put added to access_Link for access to the csv files 
today_links = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/' + str(today_date_csv)
yesterday_links = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/' + str(yesterday_date_csv)





#~ access_Links retrieves the data in string form 
def access_Link(link):
        uClient = uReq(link)
        html = uClient.read()
        uClient.close()
        main_soup = bs(html, "lxml")

        return main_soup.body.get_text()

#~ access yesterday's link if today's data has not been added 
def get_proper_Link():
    try:
        return access_Link(today_links)
    except:
        return access_Link(yesterday_links)
    
#~ saving the data to a variable
csv_string = get_proper_Link()

#~ str_csv converts the data in string format to csv format
def str_csv(string):

    convertedCSV = StringIO(csv_string)
    reader = csv.reader(convertedCSV, delimiter=',')
    # for row in reader:
    #     print('\t'.join(row))
    return


daily_csv = str_csv(csv_string)

#~ csv_df converts the csv file to a pandas dataframe
def csv_df(csv):
    return daily_df = pd.read_csv(daily_csv, sep=',')
    #print(daily_df)

main_df = csv_df(daily_csv)


#// #TODO Make yesterday/today error go away\

#! error: main_df does not print properly, something is going wrong from line 68-75, need to figure out how to make functions work together

#TODO make the code go back to the last accessible date if yesterday also does not have data
#TODO Figure out how to return the \t print statement
#TODO change Province/State to State and Country/Region to Country
#TODO allow for user input ie "Which Country do you want to see"
#TODO interactive charts with the data, bokeh, plotly, pygal, mpld3, holoviews, geoplotlib

