from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import sys
import pandas as pd

query_text = input('크롤링할 키워드는 무엇입니까?')
#fc_name=input("검색 결과를 저장할 csv 파일 경로를 입력 하시오 : ")

path = 'C:\\Users\\tlfqk\\PycharmProjects\\untitled3\\chromedriver.exe'
driver = webdriver.Chrome(path)

url = 'https://www.naver.com'
driver.get(url)
time.sleep(2)

searchBar = driver.find_element_by_id('query')

searchBar.send_keys(query_text)
searchBar.send_keys(Keys.ENTER)

elem = driver.find_element_by_link_text('블로그')
elem.click()


# STEP 5 현재 페이지에 있는 내용을 txt 형식으로 파일에 저장하기
#sys.stdout=f
#time.sleep(1)

full_html = driver.page_source
soup = BeautifulSoup(full_html, 'html.parser')

post_Title = soup.select('ul>li>dl')
post_Date=soup.select('dl>dd.txt_inline')
post_Example=soup.select('dl>dd.sh_blog_passage')

title2=[]
date2=[]
example2=[]

for i in post_Title:
    title=i.find('a',{'class':'sh_blog_title _sp_each_url _sp_each_title'}).get_text()
    title2.append(title)
    print('제목 ',title.strip())
    date=i.find('dd',{'class':'txt_inline'}).get_text()
    date2.append(date)
    print('날짜 : ',date.strip())
    example=i.find('dd',{'class':'sh_blog_passage'}).get_text()
    example2.append(example)
    print('썸네일 ',example.strip())
    print("\n")



'''
for i in post_Date:
    print(i.text)

for i in post_Example:
    print(i.text)


post_Data=pd.DataFrame()
post_Data['제목']=post_Title
post_Data['내용']=post_Example

post_Data.to_csv(fc_name,encoding='utf-8-sig')
print("csv 파일 저장 경로 : %s"%fc_name)
'''