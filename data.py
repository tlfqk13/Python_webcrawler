
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

url='https://www.naver.com/'
driver=webdriver.Chrome('chromedriver.exe')
driver.get(url)
searchBar=driver.find_element_by_id('query')
time.sleep(2)
searchBar.send_keys('백예린 square')
searchBar.send_keys(Keys.ENTER)

elem=driver.find_element_by_link_text('블로그')
elem.click()

driver.find_elements_by_css_selector('.sh_blog_title._sp_each_url _sp_each_title')[1].click()

#sh_blog_title _sp_each_url _sp_each_title
#style-scope ytd-video-renderer
