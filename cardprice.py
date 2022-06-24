from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import csv
from selenium.webdriver.chrome.options import Options

 
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome(options=chrome_options)




#card_prices = open("card_prices.csv", "w")
#card_prices.write("Name;Buy;Current;Gain;URL\n")
#card_prices.close()

with open("card_list.csv", newline="\n", encoding="utf-8") as cardlist:
    card_lines = csv.reader(cardlist, delimiter=';')
    for line in card_lines:
        url = line[1]
        driver.get(url)
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
                current_price = "Manual check"
                continue
        current_price_clean = current_price.replace(" €", "").replace(",",".")
        gain = float(current_price_clean) - float(line[2])
        line.append(current_price_clean)
        card_prices = open("card_prices.csv", "a")
        card_prices.write(f"{line[0]};{line[2]};{line[3]};{gain:.2f};{line[1]}\n")
        card_prices.close()
        time.sleep(2)

driver.close()


