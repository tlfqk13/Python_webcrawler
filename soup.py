from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import sys

query_text = input('크롤링할 키워드는 무엇입니까?')

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
# sys.stdout=f
# time.sleep(1)

full_html = driver.page_source
soup = BeautifulSoup(full_html, 'html.parser')

content_List=soup.find('li',id='sp_blog_1')

post_Title = content_List.select('dl>dt>a')
for i in post_Title:
    print(i.text)

#post_date = soup.select('dl>dd.txt_inline')
#post_exapmle = soup.select('dl>dd.sh_blog_passage')

