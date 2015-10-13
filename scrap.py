from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

links = []
query_event = raw_input('Enter query, for instance event\n')
query_sity = raw_input('Enter query, for instance San-Diego\n')

driver = webdriver.Firefox()
driver.set_window_size(1024, 768)
driver.get('http://meetup.com/')
search_element_event = driver.find_element_by_xpath('//*[@id="mainKeywords"]')
search_element_event.send_keys(query_event)
search_element = driver.find_element_by_xpath('//*[@id="searchForm"]/div[5]/a')
search_element.click()
search_element_sity = driver.find_element_by_name('userFreeform')
search_element_sity.send_keys(query_sity)
search_element_sity.send_keys(Keys.RETURN)

time.sleep(10)
#driver.save_screenshot('screen.png')

search_elements = driver.find_elements_by_class_name('display-none')
for link in search_elements:
	#print(link.get_attribute('href'))
	links.append(link)

driver.close()

