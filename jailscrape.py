import csv
import requests, mechanize
from bs4 import BeautifulSoup

##########

########## SETUP CSV ##########

csvfile = open('jail.csv', 'a')
jail_writer = csv.writer(csvfile)

url = 'https://report.boonecountymo.org/mrcjava/servlet/SH01_MP.I00290s?max_rows=500'

br = mechanize.Browser()
br.open(url)
html = br.response().read()

###########

soup = BeautifulSoup(html, "html.parser")

##########

main_table = soup.find('tbody',
    {'id': 'mrc_main_table'}
)

row_list = main_table.find_all('tr')

for r in row_list:

    output = []
    cell_list = r.find_all('td')

    if len(cell_list) > 0:
        for c in cell_list:

            ##########

            print(c.text.strip())

        print('----------')
        jail_writer.writerow(output_row)

print('IT WORKED!')
