import time
from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://google.com')
driver.find_element_by_name("q").send_keys(("Python\n"))
list = driver.find_elements_by_partial_link_text("tutorial")
print(len(list))
driver.quit()

