# -*- coding: utf-8 -*-
# author: Guangqiang Lu time:2020/1/3
# Email: gq4350lu@hotmail.com
# If not explicitly pointed out, all the codes are written by myself.

import bs4, requests
import re, os
import pdfkit, threading

def url_to_pdf(url, pdf_file):
    path_wkhtmltopdf = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'
    config = pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf)
    pdfkit.from_url(url, pdf_file, configuration=config)
    print('done')

urls= []
original_url=""
bookdir=r"C:\Users\Basanwei\Downloads\pdf\pycb"
pdffolder = "C:\\Users\\Basanwei\\Downloads\\pdf"


headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:70.0) Gecko/20100101 Firefox/70.0'}
res=requests.get(original_url, headers=headers)
res.raise_for_status()
with open('pypage.html', 'wb') as f:
    for chunk in res.iter_content(100000):
        f.write(chunk)

regex=re.compile(r'[^a-zA-Z0-9(). :_\u4e00-\u9fa5]')
f=open('pypage.html','r', encoding='UTF-8')
soup=bs4.BeautifulSoup(f.read(),'html.parser')
tags=soup.find_all(class_="reference internal")
for tag in tags:
    u=original_url+tag['href']
    text = regex.sub(' ', tag.text)
    urls.append((u, text))

f.close()

files=[os.path.splitext(filename)[0] for filename in os.listdir(bookdir)]

for i in range(len(urls)):
    if urls[i][1] not in files:
        pdffile = os.path.join(pdffolder, "%s.pdf" % urls[i][1])
        url_to_pdf(urls[i][0],pdffile)
        print('The No.%d file is downloaded.' %i)

print('The download task finished.')


