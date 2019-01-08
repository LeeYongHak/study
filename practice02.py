import bs4
import urllib.request

u = "https://www.naver.com"
h = urllib.request.urlopen(u)

o = bs4.BeautifulSoup(h,"html.parser")
a = o.find("ul",{"class":"an_l"})
b = a.findAll("li")

print(b)


