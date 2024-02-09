from urllib.request import urlopen
from bs4 import BeautifulSoup
import wget
import os

url = "http://www.pgnmentor.com/files.html"
links = []
final_links = []
page = urlopen(url)
soup = BeautifulSoup(page, "html.parser")

if os.name == "nt":
    print("Can't run on Windows, sorry!")
    exit()
try:
    os.mkdir("pgn")
except:
    pass

for link in soup.find_all("a", href=True):
    if link["href"][:6] == "player":
        links.append(link["href"])

for i in links:
    if i not in final_links and i[-4:] == ".zip":
        final_links.append(i)

for i in final_links:
    wget.download("http://www.pgnmentor.com/" + i, out="pgn")
os.chdir("pgn")
os.system("unzip '*.zip'")
os.system("rm *.zip")
os.system("clear")
