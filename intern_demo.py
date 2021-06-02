#Made By Meet and Raj
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

all_enr = ['19162121001','19162121002','19162121003']

list_mrk = []
dist_data = {}
all_list = []

opt=Options()
opt.add_argument("start-maximized")
opt.add_argument("--disable-extensions")
opt.add_experimental_option("useAutomationExtension", False)
opt.add_experimental_option("excludeSwitches",["enable-automation"])
opt.add_experimental_option("prefs", { \
"profile.default_content_setting_values.media_stream_mic": 1,
"profile.default_content_setting_values.media_stream_camera":1,
"profile.default_content_setting_values.geolocation": 1,
"profile.default_content_setting_values.notifications": 1
})

driver=webdriver.Chrome(options=opt, executable_path='chromedriver.exe')
driver.get('https://result.ganpatuniversity.ac.in/frmuniresult.aspx')
wait = WebDriverWait(driver, 10)

i = 0
for en in all_enr:

	
	

	list_mrk.clear()

	select_tag1= Select(driver.find_element_by_id('ddlInst'))
	select_tag1.select_by_value('17')
	
	select_tag2= Select(driver.find_element_by_id('ddlDegree'))
	select_tag2.select_by_value('127')
	
	select_tag3= Select(driver.find_element_by_id('ddlSem'))
	select_tag3.select_by_value('3')
	
	select_tag4= Select(driver.find_element_by_id('ddlScheduleExam'))
	select_tag4.select_by_value('8900')
	
	driver.find_element_by_id('txtEnrNo').send_keys(all_enr[i])
	
	driver.find_element_by_id('btnSearch').click()
	
	
	
	
	
	stu_name = driver.find_element_by_id('uclGrd_lblStudentName').text


	
	
	rows = len(driver.find_elements_by_xpath('/html/body/form/div[3]/div[1]/div/div[2]/table/tbody/tr'))
	columns = len(driver.find_elements_by_xpath('/html/body/form/div[3]/div[1]/div/div[2]/table/tbody/tr[2]/td'))
	
	before_XPath = "/html/body/form/div[3]/div[1]/div/div[2]/table/tbody/tr["
	aftertd_XPath = "]/td["
	aftertr_XPath = "]"
	
	for t_row in range(2, (rows + 1)):
		for t_column in range(1, (columns + 1)):
		    FinalXPath = before_XPath + str(t_row) + aftertd_XPath + str(t_column) + aftertr_XPath
		    cell_text = driver.find_element_by_xpath(FinalXPath).text
		    list_mrk.append(cell_text)

	

	

	result = driver.find_element_by_id('uclGrd_lblResult').text
	sgpa = driver.find_element_by_id('uclGrd_lblSGPA').text
	cgpa = driver.find_element_by_id('uclGrd_lblPrgCGPA').text
	sem_r = driver.find_element_by_id('uclGrd_lblSemester').text

	if sem_r == 'III':
		sem = 3

	dist_data.update({'name' : stu_name, 'enrol' : all_enr[i], 'marks' : list_mrk,'sem' : sem, 'result' : result, 'sgpa' : sgpa, 'cgpa' : cgpa})
	print(dist_data)
	
	del dist_data['name']
	del dist_data['enrol']
	del dist_data['marks']
	del dist_data['sem']
	del dist_data['result']
	del dist_data['sgpa']
	del dist_data['cgpa']

	
	

	driver.find_element_by_id('btnBack').click()
	i = i+1
driver.quit()

