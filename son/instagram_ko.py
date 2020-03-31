
#-* coding:utf-8 -*-

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
import re
import nltk
import xlwt
from nltk.tokenize import RegexpTokenizer
from nltk.tokenize import TweetTokenizer
from nltk.tokenize import word_tokenize


print("="*80)
print("8. instagram 헤쉬테그 정보 수집하기")
print("="*80)
print("\n")
query_text='instagram 헤쉬테그'
path = 'C:\\Users\\tlfqk\\PycharmProjects\\untitled3\\chromedriver.exe'
f_name=input('검색결과를 저장할 경로를 입력하세요')
#fx_name=input('검색결과를 저장할 엑셀파일 경로를 입력하세요')
driver = webdriver.Chrome(path)
hashTag='안양역카페'
tagurl = "https://www.instagram.com/explore/tags/{}".format(hashTag)
driver.get(tagurl)
time.sleep(2)
orig_stdout=sys.stdout
f=open(f_name,'w',encoding='utf-8')
sys.stdout=f
time.sleep(1)
html=driver.page_source
soup=BeautifulSoup(html,'html.parser')
tag=soup.find('img')
srcList=tag.get('src')
tag2=soup.select('img')
tag3=soup.find_all('img')
hashTag_collector=soup.select('script')
hashTagList=[]
hashTagList2=[]


#for i in tag3:
#    print(i.get('src'))

driver.find_element_by_xpath("""//*[@id="react-root"]/section/main/article/div[1]/div/div/div[1]/div[1]""").click()
for i in range(5):
    time.sleep(2)
    data=driver.find_element_by_css_selector('.Mr508')
    tag_raw=data.text
    #tags=re.findall('#[A-Za-z0-9가-힣]+',tag_raw)
    #tag=''.join(tags).replace('#',' ')
    #tag_data=tag.split()
    print(tag_raw)


print("*"*50)
print(hashTagList2)
print("*"*50)
#3
#for i in hashTag_collector:
    #hashTagList.append(i.text.split("window._sharedData = {"))

#print("csv 파일 저장 경로 : %s" %fx_name)
#excelData=pd.DataFrame(aaa)
#excelData.to_csv(fx_name,encoding='utf-8-sig')


#print(aaa)
#print(ss)
#print(hashTagList[7])
sys.stdout=orig_stdout
f.close()
#print(type(ss))
#print(len(ss))
#print(ss.count('#valenciacf'))
#print(ss.count('#arsenal'))
#print(ss.count('#'))
#print('####')
#print(len(aaa))


