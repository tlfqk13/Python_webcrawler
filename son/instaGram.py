
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

#step 2. 검색어 키워드를 입력 받고 저장할 폴더와 파일명을 설정
print("="*80)
print("8. instagram 헤쉬테그 정보 수집하기")
print("="*80)
print("\n")

query_text='instagram 헤쉬테그'

#cnt=int(input('1.크롤링 할 건수는 몇건입니까?'))
#f_dir=input('2.파일을 저장할 폴더명만 쓰세요: ')

#저장할 파일위치와 이름을 지정합니다
now=time.localtime()
s='%04d-%02d-%02d-%02d-%02d-%02d'%(now.tm_year,now.tm_mon,now.tm_mday,now.tm_hour,now.tm_min,now.tm_sec)

#os.makedirs(f_dir+s+'-'+query_text)
#os.chdir(f_dir+s+'-'+query_text)

#ff_name=f_dir+s+'-'+query_text+'\\'+s+'-'+query_text+'.txt'

#step 3. 크롬 드라이버를 사용해서 웹 브라우저를 실행합니다
s_time=time.time()
#인스타그램 로그인 URL
loginUrl='https://www.instagram.com/accounts/login/'

path = 'C:\\Users\\tlfqk\\PycharmProjects\\untitled3\\chromedriver.exe'
driver = webdriver.Chrome(path)

driver.get(loginUrl)
driver.implicitly_wait(3)



#사전 계정 정보 정의
username='01049020719'
userpw='ahqltm36@@'
hashTag='Liverpoolfc'

#로그인 정보 입력
driver.find_element_by_name('username').send_keys(username)
driver.find_element_by_name('password').send_keys(userpw)
time.sleep(2)
driver.find_element_by_xpath('/html/body/div[1]/section/main/div/article/div/div[1]/div/form/div[4]/button/div').click()

time.sleep(2)
tagurl = 'https://www.instagram.com/explore/tags/'+hashTag+'/'
driver.get(tagurl)

# 스크롤 기능 구현 (인스타그램처럼 무한 스크롤같은 플랫폼에 적합)
SCROLL_PAUSE_TIME = 5
last_height = driver.execute_script('return document.body.scrollHeight')
while True:
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
    time.sleep(SCROLL_PAUSE_TIME)

    new_height = driver.execute_script("return document.body.scrollHeight")

    if new_height == last_height:
        break
    last_height = new_height
