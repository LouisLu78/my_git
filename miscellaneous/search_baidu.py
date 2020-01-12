# -*- coding: utf-8 -*-
# author: Guangqiang Lu time:2020/1/12
# Email: gq4350lu@hotmail.com
# If not explicitly pointed out, all the codes are written by myself.

import httpx
import pdfkit
import bs4

def html_to_pdf(html, pdf_file):
    path_wkhtmltopdf = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'
    config = pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf)
    pdfkit.from_file(html, pdf_file, configuration=config)
    print('done')

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:70.0) Gecko/20100101 Firefox/70.0'}
params={"wd":"python library"}
with httpx.Client() as client:
    res = client.get('https://www.baidu.com/s', headers=headers, params=params)
res.raise_for_status()
with open('baidu.html', 'wb') as f:
    f.write(res.content)
f=open('baidu.html','r', encoding='UTF-8')
soup=bs4.BeautifulSoup(f.read(),'html.parser')
print(soup.prettify())