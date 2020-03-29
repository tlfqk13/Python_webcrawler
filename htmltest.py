
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
import nltk
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
driver = webdriver.Chrome(path)
hashTag='valenciacf'
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
hashTag_collector=soup.select('script')
hashTagList=[]
hashTagList2=[]

#for i in tag3:
#    print(i.get('src'))

#print(srcList)
count=0

#3
for i in hashTag_collector:
    hashTagList.append(i.text.split("window._sharedData = {"))


#print(hashTagList[7])
#print("###"*30)
#print(hashTag_collector)
no=1
tknzr=TweetTokenizer()
tknzr2=word_tokenize(str(hashTagList[7]))
ss=tknzr.tokenize(str(hashTagList[7]))
sss=nltk.pos_tag(ss)

#sss=list(set(ss))

'''
for i in ss:
    print(i)
    print('번호 ',no)
    no+=1
'''
aaa= [i for i in ss if "#" in i]
print(aaa)
sys.stdout=orig_stdout
f.close()
print(type(ss))
print(len(ss))
print(ss.count('#valenciacf'))
print(ss.count('#arsenal'))
print(ss.count('#'))
print('####')
print(type(sss))
print(len(sss))

