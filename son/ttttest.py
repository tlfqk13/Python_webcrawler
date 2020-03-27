#step 1. 라이브러리 로딩
from bs4 import BeautifulSoup
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
import math
import numpy
import pandas as pd
import random
import os
import pprint as pp
import json
import sys

query_text='instagram 헤쉬테그'
path = 'C:\\Users\\tlfqk\\PycharmProjects\\untitled3\\chromedriver.exe'
driver = webdriver.Chrome(path)
hashTag='valenciacf'
tagurl = 'https://www.instagram.com/explore/tags/'+hashTag+'/'
driver.get(tagurl)
time.sleep(2)

html=driver.page_source
soup=BeautifulSoup(html,'html.parser')

with open('soup','w') as f:
    data=