from lxml.html import parse

page = parse("20170718125316206976000.html")
data = list()
for i in range(18):
    rows = page.xpath("body/table")[i].findall("tr")
    for row in rows:
        data.append([c.text for c in row.getchildren()])

# s = sum([float(row[3]) for row in data[4:] if len(row) > 4 and row[2] == 'Premium GPRS 1000'])
# print(s)
for row in data[4:]:
    if len(row) > 4 and row[2] == 'Premium GPRS 1000':
        print '{} {}'.format(row[0], row[3])
