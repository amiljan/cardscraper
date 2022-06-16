from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import os

driver = webdriver.Chrome()

username = "neohellpoet"
password = os.getenv('MKM')

driver.get("https://www.cardmarket.com/en/Magic/")
driver.find_element_by_name("username").send_keys(username)
driver.find_element_by_name("userPassword").send_keys(password)
driver.find_element_by_name("userPassword").send_keys(Keys.ENTER)
driver.get("https://www.cardmarket.com/en/Magic/Orders/Purchases/Arrived")
order_table = driver.find_element_by_xpath('//*[@id="StatusTable"]').text
order_list = list(order_table.split("\n"))
order_number_list = []
count = 7
for item in range(len(order_list)):
    if item == count:
        order_number_list.append(order_list[item])
        count += 5

print(order_number_list)
driver.close()