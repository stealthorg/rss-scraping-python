import bs4
import os
from urllib.request import urlopen

#https://headlines.yahoo.co.jp/hl?a=20200330-00000049-zdn_n-sci
#https://rdsig.yahoo.co.jp/rss/l/headlines/sci/zdn_n/RV=1/RU=aHR0cHM6Ly9oZWFkbGluZXMueWFob28uY28uanAvaGw_YT0yMDIwMDMzMC0wMDAwMDA1Ny16ZG5fbi1zY2k-
#http://www.asahi.com/articles/ASN3P6SJYN3PUCVL006.html?ref=rss
#http://www.asahi.com/articles/ASN3S7SQZN3SOIPE027.html?ref=rss

"""
links = ["https://headlines.yahoo.co.jp/hl?a=20200330-00000049-zdn_n-sci","https://rdsig.yahoo.co.jp/rss/l/headlines/sci/zdn_n/RV=1/RU=aHR0cHM6Ly9oZWFkbGluZXMueWFob28uY28uanAvaGw_YT0yMDIwMDMzMC0wMDAwMDA1Ny16ZG5fbi1zY2k-","http://www.asahi.com/articles/ASN3P6SJYN3PUCVL006.html?ref=rss","http://www.asahi.com/articles/ASN3S7SQZN3SOIPE027.html?ref=rss"]


#print(links)


r = urlopen(links[0])

tag = "img"

bs4parser = bs4.BeautifulSoup(r.read(),"html.parser")

#print(bs4parser.img)
elements = bs4parser.select("img")

for element in elements:
    #print(element["src"])
    #print(os.path.basename(element["src"]))
    path = os.path.basename(element["src"])

    if path.split('.')[1] == "jpg":
        print(element["src"])
"""        