from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

links = []
query = raw_input('Enter query, for instance Warzsaw\n')

driver = webdriver.Firefox()
driver.set_window_size(1024, 768)
driver.get('http://meetup.com/')
search_element = driver.find_element_by_xpath('//*[@id="searchForm"]/div[5]/a')
search_element.click()
search_element_2 = driver.find_element_by_name('userFreeform')
#search_element = driver.find_element_by_id('simple-view-selector-event')
#search_element.click()
search_element_2.send_keys(query)
search_element_2.send_keys(Keys.RETURN)
#search_element.click()
time.sleep(10)
#driver.save_screenshot('screen.png')

search_elements = driver.find_elements_by_css_selector('p.small.ellipsize')
for link in search_elements:
	print(link.get_attribute('href'))
	links.append(link)

print links	

driver.close()

