import codecs
import urllib.request
import http.cookiejar
from bs4 import BeautifulSoup

#以Bilibili首页图片进行爬取
url = "http://www.bilibili.com"

#获取网页信息
cj = http.cookiejar.CookieJar()
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
urllib.request.install_opener(opener)

html_doc = urllib.request.urlopen(url).read()

file_html = codecs.open('bilibili.com'+'.html','wb+')

file_html.write(html_doc)

file_html.close()

#print(html_doc)

#分析网页
soup = BeautifulSoup(html_doc, 'html.parser' ,from_encoding='UTF-8')

link_jpgs = soup.find_all('img')

# file_link_jpgs = codecs.open('bilibili'+'.txt','wb+')

# file_link_jpgs.write(link_jpgs)

# file_link_jpgs.close()
#保存图片
JpgNum=1
for link_jpg in link_jpgs:
    #print (link_jpg.name, link_jpg['src'], link_jpg['alt'])
    file_jpg = open(str(JpgNum)+".jpg",'wb+')
    jpg_file = urllib.request.urlopen('http:'+link_jpg['src']).read()
    file_jpg.write(jpg_file)
    file_jpg.close
    JpgNum=JpgNum+1
