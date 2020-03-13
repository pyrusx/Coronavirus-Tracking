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
