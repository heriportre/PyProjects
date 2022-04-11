import requests

from bs4 import BeautifulSoup

url = "https://www.imdb.com/chart/top/"

response = requests.get(url)

html_icerigi = response.content

soup = BeautifulSoup(html_icerigi, "html.parser")

heading = soup.find_all("td", {"class": "titleColumn"})
rating = soup.find_all("td", {"class": "ratingColumn imdbRating"})


query = float(input("imdb ...'den yüksekleri getir:"))



for head,rate in zip(heading,rating):

    head = head.text
    rate = rate.text

    head  = head.replace("\n","")
    head = head.strip()

    rate = rate.strip()
    rate.replace("\n","")
    if float(rate)>= query:
        print(head,"\t",rate)















