# import urllib
# # import urllib2
# from bs4 import BeautifulSoup
# import sys
# from urllib.request import urlopen

# flag = 0
# textToSearch = 'hello world'
# query = sys.argv[1].strip("\"").replace(" ","+")
# # print(query)
# url = "https://www.youtube.com/results?search_query=" + query
# # print(url)
# response = urlopen(url)
# # print(response)
# html = response.read()
# # print("html : ", html)
# soup = BeautifulSoup(html,"lxml")
# print("soup : ", soup.findAll(attrs={'class':'yt-uix-tile-link'}))
# for vid in soup.findAll(attrs={'class':'yt-uix-tile-link'}):
# 	# print(vid)
# 	if ('https://www.youtube.com' + vid['href']).startswith("https://www.youtube.com/watch?v="):
# 		flag = 1
# 		print('https://www.youtube.com' + vid['href'])
# if flag == 0:
# 	print("No results found")



from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
import sys

query = sys.argv[1].strip("\"").replace(" ","+")

Path = 'C:\\Users\\abc\\Downloads\\chromedriver_win32\\chromedriver.exe'
driver = webdriver.Chrome(Path)
driver.implicitly_wait(30)

def you_search(srch):
    driver.get('https://www.youtube.com/')
    Search = driver.find_element_by_xpath('//input[@id="search"]')
    #Search = driver.find_element_by_id("search")
    Search.send_keys(srch)
    Search.send_keys(Keys.RETURN)
    print("search complete")

you_search(query)
actions = ActionChains(driver)
video = driver.find_element_by_xpath('//a[@id="video-title"]')
actions.click(video)
    
actions.perform() 
time.sleep(5)









