import csv
from datetime import datetime
import pandas as pd

total_value = 0

now = datetime.now()
date = now.strftime("%d/%m/%Y %H:%M:%S")

html_table = open("/home/amiljan/python/cardscraper/index.html", "w")
html_table.write("<html>\n")
html_table.close()
html_table = open("/home/amiljan/python/cardscraper/index.html", "a")
html_table.write("<style>\n")
html_table.write("table, th, td {  border:1px solid black;}\n")
html_table.write("</style>\n")
html_table.write("<body>\n")
html_table.write("<h2>Magic Card Prices</h2>\n")
html_table.write('<table style="width:100%">\n')
html_table.close()

with open("/home/amiljan/python/cardscraper/valuable_cards.csv", newline="\n", encoding="utf-8") as cardlist:
    card_lines = csv.reader(cardlist, delimiter=';')
    firstline = True
    for line in card_lines:
        
        if firstline == True:
            firstline = False
            line.append("Gains")
            line.append("5 day")
            line.append("30 day")
            del line[2]
            
            html_table = open("/home/amiljan/python/cardscraper/index.html", "a")
            html_table.write("  <tr>\n")
            for row in range(len(line)):
                html_table.write(f"     <th>{line[row]}</th>\n")
            html_table.write("  </tr>\n")
            html_table.close()

            dates = ["Buy"]
            for date in range(2,len(line)-1):
                dates.append(line[date])
            
            continue
        
        

        del line[2]

        card_name = line[0]
        card_buy_price = line[1]
        card_current_price = line[-1]
        card_fiveday_price = line[-5]
        card_thirtyday_price = line[-30]
        card_value_change = float(card_current_price) - float(card_buy_price)
        total_value += float(card_current_price)
        five_day_change = float(card_current_price) - float(card_fiveday_price)
        thirty_day_change = float(card_current_price) - float(card_thirtyday_price)
        line.append(round(card_value_change,2))
        line.append(round(five_day_change,2))
        line.append(round(thirty_day_change,2))

        html_table = open("/home/amiljan/python/cardscraper/index.html", "a")
        html_table.write("  <tr>\n")
        for row in range(len(line)):
            html_table.write(f"     <td>{line[row]}</td>\n")
        html_table.write("  </tr>\n")
        html_table.close()

del dates[-2]
del dates[-1]
df = pd.read_csv("/home/amiljan/python/cardscraper/valuable_cards.csv",sep=';')

totals = ["TOTAL"]
for header in dates:
    sum_of_values = round(df[header].sum(),2)
    totals.append(sum_of_values)

html_table = open("/home/amiljan/python/cardscraper/index.html", "a")
html_table.write("  <tr>\n")
for row in range(len(totals)):
    html_table.write(f"     <td>{totals[row]}</td>\n")
html_table.write("  </tr>\n")
html_table.close()



html_table = open("/home/amiljan/python/cardscraper/index.html", "a")
html_table.write('</table>\n')
html_table.write(f"<p>The current total value of all the cards is {round(total_value,2)}. Date and Time: {date} </p>\n")
html_table.write('</body>\n')
html_table.write('</html>\n')
html_table.close()
