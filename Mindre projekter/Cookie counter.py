from bs4 import BeautifulSoup
import requests
url = "https://orteil.dashnet.org/cookieclicker/"
req = requests.get(url)
soup = BeautifulSoup(req.text, "html.parser")
print(soup.title)