########## STEP 1: Import your libraries! ##########

import csv
import requests, mechanize
from bs4 import BeautifulSoup

csvfile = open('jail.csv', 'a')
jail_writer = csv.writer(csvfile)

########## STEP 2: Get the HTML! ##########

url = 'https://report.boonecountymo.org/mrcjava/servlet/RMS01_MP.I00030s?max_rows=500'

br = mechanize.Browser()
br.open(url)
html = br.response().read()

########## STEP 3: Make soup! ##########

soup = BeautifulSoup(html, "html.parser")

########## STEP 4: Dig through the HTML ##########

main_table = soup.find('tbody', {'id': 'mrc_main_table'})

row_list = main_table.find_all('tr')

for row in row_list:

    td_tags = row.find_all('td')

    output = []
    for td in td_tags:
        output.append(td.text.strip())

    jail_writer.writerow(output)