from bs4 import BeautifulSoup as soup
from urllib2 import urlopen
#from urllib.request import urlopen as ureq
import re
data =[]
mydatasaved=''
my_url='https://www.rottentomatoes.com/'
client=urlopen(my_url)
page = client.read()
client.close()
page_soup=soup(page,'html.parser')
print (page_soup.title.text)
#table=page_soup.findAll('table' , attrs = {"id":"Opening"})

table=page_soup.findAll('table')[3]
#print table.findAll(string=re.compile('^[i]'))

rows = table.findAll('tr')
for row in rows:
    mydata=''
    for col in row.findAll('td'):
    #for text in col:
        #data.append(text.text)
        mydata=mydata +", " + (col.text).strip('\n\t')
    mydatasaved= mydatasaved + "\n"  +mydata[1:]
print mydatasaved
#body = table.findAll('tbody')
#print body

#for rows in table:
#    print rows.get_text().strip(' \n\t')


#print data
