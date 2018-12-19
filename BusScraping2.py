import requests
from bs4 import BeautifulSoup

target_html = "http://www.kanachu.co.jp/dia/diagram/timetable/cs:0000801156-1/nid:00129893/rt:0/k:%E6%B9%98%E5%8D%97%E5%8F%B0%E9%A7%85%E8%A5%BF%E5%8F%A3"
r = requests.get(target_html)
soup = BeautifulSoup(r.text, "html.parser")

table = soup.select('.timetable')[0].findAll("table")[0]
rows = table.select('tr')


f = open("t2.txt", mode="w")

for row in rows:
    tds = row.findAll('td')
    for td in tds:
        contents = td.select('.time')
        for content in contents:
            f.write("  ||||  ")
            for con in content:
                f.write(str(con.text)+",")
    f.write("\n----------------\n")
f.close()
