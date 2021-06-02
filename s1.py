from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver import ActionChains
import time

driver = webdriver.Chrome(executable_path="/Users/rajchhabria/Desktop/Selenium/chromedriver")

driver.maximize_window()

driver.get("http://result.ganpatuniversity.ac.in/")
print(driver.title)

select = Select(driver.find_element_by_name('ddlInst'))

# select by visible text
select.select_by_visible_text('16 - ICT')

degree = Select(driver.find_element_by_name('ddlDegree'))

degree.select_by_visible_text('B.TECH-CSE(BDA)')

sem = Select(driver.find_element_by_name('ddlSem'))

sem.select_by_visible_text('III')

exam = Select(driver.find_element_by_name('ddlScheduleExam'))

exam.select_by_visible_text('NOV - DEC 2020 [ REGULAR ]')


search = driver.find_element_by_name("txtEnrNo")
search.send_keys("19162121003")


search.send_keys(Keys.RETURN)

time.sleep(10)


driver.quit()