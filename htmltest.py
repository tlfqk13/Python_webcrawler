
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


print("="*80)
print("8. instagram 헤쉬테그 정보 수집하기")
print("="*80)
print("\n")
query_text='instagram 헤쉬테그'
path = 'C:\\Users\\tlfqk\\PycharmProjects\\untitled3\\chromedriver.exe'
f_name=input('검색결과를 저장할 경로를 입력하세요')
driver = webdriver.Chrome(path)
hashTag='안양역카페'
tagurl = 'https://www.instagram.com/explore/tags/'+hashTag+'/'
driver.get(tagurl)
time.sleep(2)
orig_stdout=sys.stdout
f=open(f_name,'w',encoding='UTF-8')
sys.stdout=f
time.sleep(1)
html=driver.page_source
soup=BeautifulSoup(html,'html.parser')
tag=soup.find('img')
srcList=tag.get('src')
tag2=soup.select('img')
tag3=soup.find_all('img')

for i in tag3:
    print(i.get('src'))

print(srcList)
print("###")
sys.stdout=orig_stdout
f.close()
