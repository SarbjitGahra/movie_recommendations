#importing dependcies
from bs4 import BeautifulSoup as soup
from urllib2 import urlopen
import csv

mydatasaved=''
# the url to be crawled
my_url='https://www.rottentomatoes.com/'

#using urlopen to open and read the url
client=urlopen(my_url)
page = client.read()
client.close()

#The file to be outputted to
filename="movies.csv"
f =open(filename, "w")
headers = "Ratings ,Titles, Release_date"
f.write(headers)

#File to be parsed in html format using BeautifulSoup
page_soup=soup(page,'html.parser')
#finding the table we require
table=page_soup.findAll('table')[4]

#finding all the rows in the table
rows = table.findAll('tr')
# for each row
for row in rows:
    mydata=''
    for col in row.findAll('td'):
        mydata=mydata +", " + (col.text).strip()
    mydatasaved= mydatasaved + "\n"  +mydata[1:]
    f.write(mydatasaved)
f.close()
print mydatasaved
