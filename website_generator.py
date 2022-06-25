import csv

total_value = 0

html_table = open("index.html", "w")
html_table.write("<html>\n")
html_table.close()
html_table = open("index.html", "a")
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
            line.append("Gain/Loss")
            
            html_table = open("index.html", "a")
            html_table.write("  <tr>\n")
            for row in range(len(line)):
                html_table.write(f"     <th>{line[row]}</th>\n")
            html_table.write("  </tr>\n")
            html_table.close()
            
            continue
        
        card_name = line[0]
        card_buy_price = line[1]
        card_current_price = line[-1]
        card_value_change = float(card_current_price) - float(card_buy_price)
        total_value += float(card_current_price)
        line.append(round(card_value_change,2))

        html_table = open("index.html", "a")
        html_table.write("  <tr>\n")
        for row in range(len(line)):
            html_table.write(f"     <td>{line[row]}</td>\n")
        html_table.write("  </tr>\n")
        html_table.close()

html_table = open("index.html", "a")
html_table.write('</table>\n')
html_table.write(f"<p>The current total value of all the cards is {round(total_value,2)}.</p>\n")
html_table.write('</body>\n')
html_table.write('</html>\n')
html_table.close()