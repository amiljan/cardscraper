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


for item in range(len(order_number_list)):
    driver.get(f"https://www.cardmarket.com/en/Magic/Orders/{order_number_list[item]}")
    for card in range(1, 100):
        try:
            #card_row = driver.find_element_by_xpath(f'/html/body/main/section/div/div[1]/div/div[6]/table/tbody/tr[{card}]').text
            #print(card_row)
            card_name = driver.find_element_by_xpath(f'/html/body/main/section/div/div[1]/div/div[6]/table/tbody/tr[{card}]/td[4]/a').text
            print(card_name)
            card_html = driver.find_element_by_xpath(f'/html/body/main/section/div/div[1]/div/div[6]/table/tbody/tr[{card}]/td[4]/a').get_attribute("href")
            print(card_html)
        except:
            break
    if item == 1:
        break
driver.close()

#name and price
#/html/body/main/section/div/div[1]/div/div[6]/table/tbody/tr[1]
#/html/body/main/section/div/div[1]/div/div[6]/table/tbody/tr[2]


#link 
#/html/body/main/section/div/div[1]/div/div[6]/table/tbody/tr[1]/td[4]/a
#/html/body/main/section/div/div[1]/div/div[6]/table/tbody/tr[2]/td[4]/a