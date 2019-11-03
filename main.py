from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time
import random
#predefine constants
comments = ['I like this, this is the best', 'Wow, great I love this', 'Really great!!! Aha~~~~']

visited = {}

browser = webdriver.Chrome()
browser.get("https://www.instagram.com/accounts/login/?source=auth_switcher")
while True:
	try:
		nameElm = browser.find_element_by_name("username")
		break
	except Exception as e:
		pass

nameElm.send_keys("jhonwilliam1995")
passElm = browser.find_element_by_name("password")
passElm.send_keys("notouch1995")
loginBtn = browser.find_element_by_class_name("L3NKy")
loginBtn.click()
while True:
	try:
		browser.find_element_by_class_name("bIiDR")
		break
	except Exception as e:
		pass
browser.get('https://www.instagram.com/explore/locations/3800652/flushing-new-york/')

time.sleep(3)
# while True:
# 	container = browser.find_element_by_xpath('/html/body/span/section/main/article/div[2]')
# 	posts = container.find_elements_by_class_name('eLAPa')
# 	for post in posts:
# 		post.click()
# 		time.sleep(1.5)
# 		a = browser.find_element_by_xpath('/html/body/div[3]/div[2]/div/article/div[2]/section[1]/span[1]/button/span')
# 		if a.get_attribute('aria-label') == 'Unlike':
# 			a.click()
# 		else :
# 			time.sleep(1.5)
# 			browser.back()
# 			return	
# 		time.sleep(1.5)
# 		browser.back()
flag = True
while flag == True:
	container = browser.find_element_by_xpath('/html/body/span/section/main/article/div[2]')
	posts = container.find_elements_by_class_name('_bz0w')
	for post in posts:
		a_tag = post.find_element_by_tag_name('a')
		link = a_tag.get_attribute('href')
		if link in visited.keys():
			continue
		visited[link] = True
		eLAPa = post.find_element_by_class_name('eLAPa')
		eLAPa.click()
		time.sleep(1.5)
		like_span = browser.find_element_by_xpath('/html/body/div[3]/div[2]/div/article/div[2]/section[1]/span[1]/button/span')
		if like_span.get_attribute('aria-label') == 'Like':
			like_span.click()
			time.sleep(1.2)
			comment = comments[random.randint(0, len(comments)) - 1]
			browser.find_element_by_xpath('/html/body/div[3]/div[2]/div/article/div[2]/section[1]/span[2]/button/span').click()
			comment_input = browser.find_element_by_xpath('/html/body/div[3]/div[2]/div/article/div[2]/section[3]/div/form/textarea')
			comment_input.send_keys(comment)
			time.sleep(1.3)
			btn = browser.find_element_by_xpath('/html/body/div[3]/div[2]/div/article/div[2]/section[3]/div/form/button')
			btn.click()
		else :
			time.sleep(1.5)
			browser.back()
			flag = False
			break
		time.sleep(1.5)
		browser.back()
