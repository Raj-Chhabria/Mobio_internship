from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver import ActionChains
import time

product = input("Enter product name: ")


driver = webdriver.Chrome(executable_path="/Users/rajchhabria/Desktop/Selenium/chromedriver")

driver.maximize_window()

driver.get("https://www.amazon.in/ref=nav_logo")

search_bar = driver.find_element_by_id("twotabsearchtextbox")
search_bar.send_keys(product)

search_button = driver.find_element_by_id("nav-search-submit-button")
search_button.click()

time.sleep(50)

driver.quit()