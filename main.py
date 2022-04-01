#!/usr/bin/python3
from bs4 import BeautifulSoup
import requests



     

URL = input("Enter URL :")
print("URl is : " + URL)
page = requests.get(URL)


text = page.content


soup = BeautifulSoup(text, "html.parser")


with open("output/output.html", "w", encoding = 'utf-8') as file:
	
	
	file.write(str(soup.prettify()))
 
     

