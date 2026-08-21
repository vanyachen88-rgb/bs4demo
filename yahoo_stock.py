from bs4 import BeautifulSoup
import requests
from pprint import pprint

url = "https://tw.stock.yahoo.com/quote/2609.TW"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")
accton2609 = soup.find("span", class_="Fw(n) Fz(16px)--mobile Fz(14px) D(f) Ai(c)")
print(f'陽明股價是: {accton2609.text}')