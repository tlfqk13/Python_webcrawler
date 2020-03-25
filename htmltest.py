from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time
import sys
import pandas as pd

chrome_options=Options()
chrome_options.add_experimental_option("debuggerAddress","127.0.0.1:9222")
path = 'C:\\Users\\tlfqk\\PycharmProjects\\untitled3\\chromedriver.exe'
driver = webdriver.Chrome(path,options=chrome_options)

url = 'https://www.naver.com'
driver.get(url)
searchBar = driver.find_element_by_class_name('ico_search_submit').click()

