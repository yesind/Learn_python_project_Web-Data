import chromedriver_binary
from selenium import webdriver
import time

browser = webdriver.Chrome()
browser.get('http://auto.ru')
time.sleep(5)
browser.close()
