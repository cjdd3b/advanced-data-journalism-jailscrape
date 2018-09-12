import requests, mechanize
from bs4 import BeautifulSoup

url = 'https://report.boonecountymo.org/mrcjava/servlet/SH01_MP.I00290s?max_rows=500'

# Get the HTML of the page
br = mechanize.Browser()
br.open(url)
html = br.response().read()

# Transform the HTML into a BeautifulSoup object
soup = BeautifulSoup(html, "html.parser")

# Find the main table using both the "align" and "class" attributes
main_table = soup.find('tbody',
    {'id': 'mrc_main_table'}
)

row_list = main_table.find_all('tr')

# Now get the data from each table row
for r in row_list:

    cell_list = r.find_all('td')

    if len(cell_list) > 0:
        for c in cell_list:
            print c.text.strip()

        print '----------'

print 'IT WORKED!'