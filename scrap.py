from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

from bs4 import BeautifulSoup
import csv
import urllib2

links = []
row = []
query_event = raw_input('Enter query, for instance python\n')
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
	links.append(link.get_attribute('href'))

driver.close()

USER_AGENT = "Mozilla/5.0 (Windows; U; Windows NT 5.2; en-CA; rv:1.9.2.4) Gecko/20100523 Firefox/3.6.4"

for link in links:
    if link:
        with open('out.csv', 'a') as f:
            csvwriter = csv.writer(f, delimiter=',', dialect='excel')
            url = link
            try:
		hdr = {'User-Agent': USER_AGENT}
	        req = urllib2.Request(link, headers=hdr)
                page = urllib2.urlopen(req)
            except urllib2.HTTPError, error:
                print error
	    soup = BeautifulSoup(page, 'html.parser')
	    div = soup.find("div", {"id": "groupDesc"})
	    row.append(link)
	    row.append(div.text.encode('utf-8'))
	    csvwriter.writerow(row)
	    row = []

print "scraping complete"