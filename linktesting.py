import csv
from time import sleep
from selenium import webdriver
from parsel import Selector
from selenium.webdriver.common.keys import Keys


writer = csv.writer(open('result_file.csv', 'a'))
writer.writerow(['name', 'job_title', 'location', 'company_name', 'ln_url'])

driver = webdriver.Chrome("C:/Users/Sagar/Downloads/chromedriver.exe")
driver.maximize_window()

sleep(0.5)

driver.get("https://www.linkedin.com/")
sleep(5)

driver.find_element_by_xpath('//a[text()="Sign in"]').click()
sleep(3)

username_input = driver.find_element_by_name('session_key')
username_input.send_keys('sn.himanshu.paliwal@gmail.com')
sleep(0.5)

password_input = driver.find_element_by_name('session_password')
password_input.send_keys('linkedin^123')
sleep(2)


driver.find_element_by_xpath('//button[text()="Sign in"]').click()
sleep(5)

driver.get("https://www.google.com/")
sleep(5)

search_input = driver.find_element_by_name('q')
search_input.send_keys('site:linkedin.com/in/ AND "python developer" AND "New York"')
sleep(1)

search_input.send_keys(Keys.RETURN)
sleep(3)

for i in range(20):
	google_next = driver.find_elements_by_xpath('//*[@id="nav"]//*[@class="fl"]')
	google_next = [google.get_attribute('href') for google in google_next]
	for google in google_next:

		profiles = driver.find_elements_by_xpath('//*[@class="r"]/a[1]')
		profiles = [profile.get_attribute('href') for profile in profiles]
		for profile in profiles:
			driver.get(profile)
			sleep(5)

			sel = Selector(text=driver.page_source)
			try:
				name = sel.xpath('//title/text()').extract_first().split('|')[0]
				job_title = sel.xpath('//h2/text()').extract_first().strip()
				location = sel.xpath('//*[contains(@class, "t-16 t-black t-normal inline-block")]/text()').extract_first()
				company_name =  sel.xpath('//*[starts-with(@class,"text-align-left ml2 t-14 t-black t-bold full-width lt-line-clamp lt-line-clamp--multi-line ember-view")]/text()').extract_first()
				if company_name:
					company_name = company_name.strip()
				#education =  sel.xpath('//*[contains(@class,"top-card-link__description")]/text()').extract()[1]
				ln_url = driver.current_url
			except:
				print('pass')

			print(name)
			print(job_title)
			print(location)
			print(company_name)
			#print(education)
			print(ln_url)

			writer.writerow([name, job_title, location, company_name, ln_url])
			sleep(5)
		driver.get(google)
		sleep(5)
		
driver.quit()



#profile = profiles[1]
#driver.get(google)

#google = google_next[1]

#google_next = driver.find_elements_by_xpath('//*[@id="pnnext"]')
#google_next = [google.get_attribute('href') for google in google_next]

#google_next = sel.xpath('//*[@id="pnnext"]')
#driver.find_elements_by_xpath('//span[contains(text(),"Next")]')
#for google in google_next:
#driver.get(google)
	#sleep(5)
	#if google == google_next:
		google_next = driver.find_elements_by_xpath('//*[@id="nav"]//*[@class="fl"]')
		google_next = [google.get_attribute('href') for google in google_next]
		sleep(2)
		driver.get(google)


#google_next = driver.find_elements_by_xpath('//*[@id="nav"]//*[@class="fl"]')
	google_next = [google.get_attribute('href') for google in google_next]
	for google in google_next:
		driver.get(google)
		for google in google_next: