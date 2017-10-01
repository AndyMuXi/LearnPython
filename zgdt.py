import codecs
import os
import re
import urllib.request
import http.cookiejar
from bs4 import BeautifulSoup

folder_now = os.getcwd()

#爬取组工动态新闻网

#获取网页信息
def downzgdt(url,website):
    cj = http.cookiejar.CookieJar()
    opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
    urllib.request.install_opener(opener)

    html_doc = urllib.request.urlopen(url).read()

    ''' file_html = codecs.open('zgdt'+'.html','wb+')

    file_html.write(html_doc)

    file_html.close() '''

    #print(html_doc)

    #分析网页
    soup = BeautifulSoup(html_doc, 'html.parser' ,from_encoding='UTF-8')

    link_news = soup.find_all('a', class_='c138164')


    #保存文章建立文章目录

    link_new_num = 1
    link_new_title = ''
    folder_name=''
    for link_new in link_news:
        #print(link_new.name, link_new['class'],link_new.get_text())
        if len(link_new.get_text()) == 4:
            link_new_title = link_new.get_text()
            continue
        else:
            #创建目录
            link_new_title = link_new_title + link_new.get_text()
            folder_name=link_new_title
            link_new_title=''
            #print(folder_name)
            try:
                os.mkdir(folder_name)
            except:
                continue
            #print(link_new['href'][2:])
            #爬取二级目录
            url_new = website + link_new['href'][5:]
            html_new_doc = urllib.request.urlopen(url_new).read()

            #分析二级目录
            soup_new = BeautifulSoup(html_new_doc, 'html.parser' ,from_encoding='UTF-8')
            link_article = soup_new.find('div', id=re.compile(r'vsb_content'))
            link_img = soup_new.find_all('img', src = re.compile(r"media"))

            #保存文章
            #print(link_article.get_text())
            if link_article != None :
                os.chdir(folder_now+'/'+folder_name)
                file_article = codecs.open(folder_name+'.txt','wb+')
                file_article.write(link_article.get_text().encode())
                file_article.close
                os.chdir(folder_now)
            else:
                continue

            #保存图片
            if link_img != None:
                #print(link_img['src'][5:])
                os.chdir(folder_now+'/'+folder_name)
                img_num =0
                for link_img_ in link_img:
                    file_jpg = open(str(img_num)+'.jpg','wb+')
                    jpg_file = urllib.request.urlopen(website+link_img_['src'][5:]).read()
                    file_jpg.write(jpg_file)
                    file_jpg.close
                    img_num = img_num + 1
            else:
                pass
            os.chdir(folder_now)

class web(object):
    website ="http://dj.swpu.edu.cn"
# file_urls = open("urls.txt","r")  
# urls = file_urls.readlines()

for url in codecs.open('urls.txt'):
    downzgdt(url,web.website)