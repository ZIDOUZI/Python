from bs4 import BeautifulSoup as bs

with open("1.html", "r") as f:
    text = bs(f.read(), "html.parser")
print(text.find("head").text)
print(text.find("body").text)
print(text.find(id="Hi").text)
