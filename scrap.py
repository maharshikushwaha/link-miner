import requests
from bs4 import BeautifulSoup
import time
from termcolor import colored
print("Enter Address Of Web Page To Scrap All Links: ")
url = input()
r = requests.get(url)
htmlContent = r.content
msk = 0
# print(htmlContent)
soup = BeautifulSoup(htmlContent, 'html.parser')
title = soup.title.string
title = "We Are Scraping:" +title + "\n\n"
print(colored(title, "red"))
all_link = set()
paras = soup.find_all('a')
for link in paras:
    if (link.get('href') != '#'):
       all_link.add(link.get('href'))
for msk in all_link:
  print(colored(msk, "green"))
  time.sleep(0.4)



print("\n\n\n\nIt is done\n This is written by:", colored("Maharshi Kushwaha", "green"))
# print(paras)
# print(soup.find('p'))
# print(soup.find('p')["class"])
#
# print(soup.find_all("p", class_="lead"))

# print(soup.get_text())
