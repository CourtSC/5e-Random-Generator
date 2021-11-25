#! python3
#! dataPull.py - A program to scrape D&D 5e magic item info from various sources and save them to a database
#! Edge User-Agent - Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36 Edg/96.0.1054.29

import bs4, requests_html, sqlite3

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36 Edg/96.0.1054.29'}
session = requests_html.HTMLSession()

# Create database.
con = sqlite3.connect('Magic Item Tables/magicItem.db')
sql = 'INSERT INTO MAGICITEMS (name, rarity, type, subtype, attune, notes) values(?, ?, ?, ?, ?, ?)'
try:
    with con:
        con.execute("""
            CREATE TABLE MAGICITEMS (
                name TEXT,
                rarity TEXT,
                type TEXT,
                subtype TEXT,
                attune TEXT,
                notes TEXT
            );
        """)
except:
    pass

data = []
page = 1
nextPage = True
while nextPage:
    res = session.get('https://www.dndbeyond.com/magic-items?page=' + str(page), headers = headers)
    res.raise_for_status
    soup = bs4.BeautifulSoup(res.text, "html.parser")
    nextPage = soup.select('.b-pagination-item.b-pagination-item-next')
    page += 1
    # collect information from each magic item on the page.
    itemName = soup.select('.link span')
    itemRarity = soup.select('.rarity') # Need to strip whitespace.
    itemType = soup.select('.row.item-type .type') # Need to strip whitespace.
    itemSubType = soup.select('.row.item-type .subtype') # Need to strip whitespace.
    itemAttunement = soup.select('.row.requires-attunement') # Need to strip whitespace.
    itemNotes = soup.select('.row.notes') # Need to strip whitespace.
    # Create the data list of tuples.
    for i in range(len(itemName)):
        data.append((itemName[i].getText().strip(), itemRarity[i].getText().strip(), itemType[i].getText().strip(), itemSubType[i].getText().strip(), itemAttunement[i].getText().strip(), itemNotes[i].getText().strip()))
        # print(f'Added item {itemName[i].getText().strip()} to database.')

# Add new data to the MAGICITEMS table in the database.
def itemCheck(item):
    with con:
        dbItem = con.execute("SELECT * FROM MAGICITEMS WHERE name == " + item)
        if dbItem:
            return True
        else:
            return False
with con:
    for i in range(len(itemName)):
        if not itemCheck(itemName[i].getText().strip()):
            con.execute(sql, data[i])