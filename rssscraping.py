import feedparser,json

urls = ["http://rss.asahi.com/rss/asahi/digital.rdf","https://headlines.yahoo.co.jp/rss/zdn_n-c_sci.xml"]


def getrss():
    for url in urls:
        for entry in feedparser.parse(url).entries:
            
            title = entry["title"]

            pubdate = entry["updated"]

            link = entry["link"]

            print(title,pubdate,link)


def getrss_tojson():
    for url in urls:
        for entry in feedparser.parse(url).entries:
            
            title = entry["title"]

            pubdate = entry["updated"]

            link = entry["link"]

            dic = {"title":title,"pubdate":pubdate,"link":link}

            print(json.dumps(dic,indent=2,ensure_ascii=False))


getrss_tojson()
