from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import os
import time

driver = webdriver.Chrome()

username = "neohellpoet"
password = os.getenv('MKM')

driver.get("https://www.cardmarket.com/en/Magic/")
driver.find_element_by_name("username").send_keys(username)
driver.find_element_by_name("userPassword").send_keys(password)
driver.find_element_by_name("userPassword").send_keys(Keys.ENTER)


for number in range(1,11):
    driver.get(f"https://www.cardmarket.com/en/Magic/Orders/Purchases/Arrived?site={number}")
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
                card_price = driver.find_element_by_xpath(f'/html/body/main/section/div/div[1]/div/div[6]/table/tbody/tr[{card}]').get_attribute("data-price")
                card_name = driver.find_element_by_xpath(f'/html/body/main/section/div/div[1]/div/div[6]/table/tbody/tr[{card}]/td[4]/a').text
                card_html = driver.find_element_by_xpath(f'/html/body/main/section/div/div[1]/div/div[6]/table/tbody/tr[{card}]/td[4]/a').get_attribute("href")

                card_string = f"{card_name};{card_html};{card_price}\n"

                card_list = open("card_list.csv","a")
                card_list.write(card_string)
                card_list.close()
            except:
                break
        time.sleep(3)
        
driver.close()



