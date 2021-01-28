from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time

options = Options()
options.add_argument("--disable-notifications")
chrome = webdriver.Chrome('./chromedriver', chrome_options=options)
# chrome.get("https://www.facebook.com/")
# email = chrome.find_element_by_id("email")
# password = chrome.find_element_by_id("pass")
# email.send_keys('*********@gmail.com')
# password.send_keys('**********')
# password.submit()

chrome.get('https://www.facebook.com/learncodewithmike')
time.sleep(5)

for x in range(1, 4):
    chrome.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    time.sleep(5)

maybelater = chrome.find_element_by_id("expanding_cta_close_button")
maybelater.click()

soup = BeautifulSoup(chrome.page_source, 'html.parser')
titles = soup.find_all('a', {'class': '_52c6'})
for title in titles:
    print(title["aria-label"])   # dictionary的概念

chrome.quit()
