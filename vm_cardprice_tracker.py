from os import sep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import csv
from selenium.webdriver.chrome.options import Options
from datetime import datetime
import os
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Remote("http://127.0.0.1:4444/wd/hub", DesiredCapabilities.CHROME,options=chrome_options)
date = datetime.today().strftime('%Y-%m-%d')



with open("valuable_cards.csv", newline="\n", encoding="utf-8") as cardlist:
    card_lines = csv.reader(cardlist, delimiter=';')
    firstline = True
    for line in card_lines:
        if firstline == True:
            firstline = False
            line.append(date)
            valuable_card_list = open("valuable_cards1.csv", "w")
            mySeparator = ";"
            card_data = mySeparator.join(line) + "\n"
            valuable_card_list.write(card_data)
            valuable_card_list.close()
            continue
        url = line[2]
        driver.get(url)
        if line[0][0:3] == "Box":
            current_price = driver.find_element_by_xpath('/html/body/main/div[4]/section[2]/div/div[2]/div[1]/div/div[1]/div/div[2]/dl/dd[3]/span').text
        else:
            try:
                current_price = driver.find_element_by_xpath('/html/body/main/div[4]/section[2]/div/div[2]/div[1]/div/div[2]/div/div[2]/dl/dd[7]/span').text
            except:
                try:
                    for number in range(10):
                        try:
                            current_price = driver.find_element_by_xpath(f'/html/body/main/div[4]/section[2]/div/div[2]/div[1]/div/div[{number}]/div/div[2]/dl/dd[7]/span').text
                        except:
                            continue
                except: 
                    continue
        current_price_clean = current_price.replace(" €", "").replace(",",".")
        line.append(current_price_clean)
        valuable_card_list = open("valuable_cards1.csv", "a")
        mySeparator = ";"
        card_data = mySeparator.join(line) + "\n"
        valuable_card_list.write(card_data)
        valuable_card_list.close()
        time.sleep(2)

driver.close()

#os.remove("valuable_cards.csv")
#os.rename("valuable_cards1.csv","valuable_cards.csv")