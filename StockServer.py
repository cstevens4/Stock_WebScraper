import requests
from socket import *
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as request

serverPort = 8000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1) 

print('Server is up and ready!')

client = request('https://markets.businessinsider.com/index/market-movers/dow_jones')
html_page = client.read() 
client.close()

soup_page = soup(html_page, "html.parser")

#Parsing company name
#html_table_name = 
split1 = html_table_name.split(">")
split2 = split1.split("<")
companyName = split2[0] 

#Parsing percentage
#html_table_today = 
split3 = html_table_today('>')
split4 = split3.split("<")
todayPercent = split4[0]

#Parsing 3 month data
#html_table_three = 
split5 = html_table_three('>')
split6 = split5.split("<")
todayPercent = split6[0]

#Parsing 6 month data
#html_table_six = 
split7 = html_table_six('>')
split8 = split7.split("<")
todayPercent = split8[0]

#Parsing 1 year data
#html_table_year = 
split9 = html_table_year('>')
split10 = split9.split("<")
todayPercent = split10[0]