import requests
import csv
from bs4 import BeautifulSoup as bs

url=requests.get("https://quirky-lichterman-ddef4e.netlify.app/")
soup=bs(url.content,'html.parsar')
filename='test.csv'
csv_writer=csv.writer(open(filename,'w'))
heading=soup.find('h2')
print(heading.text)
