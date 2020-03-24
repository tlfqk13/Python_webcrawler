from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import sys


query_text=input('크롤링할 키워드는 무엇입니까?')
f_name=input('검색 결과를 저장할 txt 파일경로와 이름을 지정하세요 : ')
#fc_name=input('검색 결과를 저장할 csv 파일경로와 이름을 지정하세요 : ')
#fx_name=input('검색 결과를 저장할 xls 파일경로와 이름을 지정하세요 : ')


path='C:\\Users\\tlfqk\\PycharmProjects\\untitled3\\chromedriver.exe'
driver=webdriver.Chrome(path)

url='https://www.naver.com'
driver.get(url)
time.sleep(2)

searchBar=driver.find_element_by_id('query')

searchBar.send_keys(query_text)
searchBar.send_keys(Keys.ENTER)

elem=driver.find_element_by_link_text('블로그')
elem.click()

#STEP 4 현재 페이지에 있는 내용을 화면에 출력하기
'''full_html=driver.page_source
soup=BeautifulSoup(full_html,'html.parser')
post_title=soup.select('dl > dt > a')

for i in post_title:
    print(i.text.strip())
    print("\n")
'''
#STEP 5 현재 페이지에 있는 내용을 txt 형식으로 파일에 저장하기
orig_stdout=sys.stdout
f=open(f_name,'w',encoding='UTF-8')
sys.stdout=f
time.sleep(1)

no=1
no2=[]

post_Title2=[]
post_date2=[]
post_example2=[]
full_html=driver.page_source

soup=BeautifulSoup(full_html,'html.parser')

#post_Title=soup.select('dl>dt>a')

content_List=soup.find('div',class_='blog section _blogBase _prs_blg')
print(content_List)


print("++++++++++++++++++++++++++++++++++")
'''
post_Title2=content_List.find('a',class_='sh_blog_title _sp_each_url _sp_each_title').get_text()
print("제목: ",post_Title2.strip())
post_date=content_List.find('dd','txt_inline').get_text()
print("날짜: ",post_date.strip())
post_exapmle2=content_List.find('dd',class_='sh_blog_passage').get_text()
print('썸네일: ',post_exapmle2)
'''
print("+++++++++++++++++++++++++++++++++++")

for i in content_List:
    no2.append(no)
    print('번호 ',no)

    post_Title = content_List.find('a', class_='sh_blog_title _sp_each_url _sp_each_title').get_text()
    post_Title2.append(post_Title)
    print('내용 : ',post_Title.strip())

    post_date=content_List.find('dd','txt_inline').get_text()
    post_date2.append(post_date)
    print('날짜 : ',post_date.strip())

    post_example=content_List.find('dd',class_='sh_blog_passage').get_text()
    post_example2.append(post_example)
    print('썸네일 : ',post_example.strip())

    no+=1

sys.stdout=orig_stdout
f.close()

#STEP 5 각 항목별로 분리하여 추출하고 변수에 할당하기
