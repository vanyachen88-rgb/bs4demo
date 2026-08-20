from bs4 import BeautifulSoup
import requests
from pprint import pprint

url = "https://mymis168.github.io/bs4demo/apple.html"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")
#尋找 class 為依據的條件
class_a = soup.find("div", class_="section-header")  # class_ 原因因為 python 有 class指令 衝突
print(f'c = {class_a.text}')