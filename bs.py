from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver import ActionChains
import time


driver = webdriver.Chrome(executable_path="/Users/rajchhabria/Desktop/Selenium/chromedriver")