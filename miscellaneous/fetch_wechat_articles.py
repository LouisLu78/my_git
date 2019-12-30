# -*- coding: utf-8 -*-
# author: Guangqiang Lu time:2019/12/30
# Email: gq4350lu@hotmail.com
# If not explicitly pointed out, all the codes are written by myself.

import bs4, requests
import re, os, shutil
import pdfkit

path_wkhtmltopdf=r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'
config=pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf)

def url_to_pdf(url, pdf_file):
    pdfkit.from_url(url, pdf_file, configuration=config)
    print('done')

res=requests.get('https://mp.weixin.qq.com/s/HMT2fwf1gE8SSNZKd1uf6A')
res.raise_for_status()
with open('p100.html', 'wb') as f:
    for chunk in res.iter_content(100000):
        f.write(chunk)
urls=[]
regex=re.compile(r'weixin')
pdffolder = "C:\\Users\\Basanwei\\Downloads\\pdf"
f=open('p100.html','r+', encoding='UTF-8')
soup=bs4.BeautifulSoup(f.read(),'html.parser')

tags=soup.find_all(href=regex)
for tag in tags:
    urls.append(tag['href'])
for i in range(79,103):
    pdffile = os.path.join(pdffolder, '0%d_.pdf' %(i-2))
    url_to_pdf(urls[i],'temp.pdf')
    shutil.copy("temp.pdf", pdffile)
    print('The No.%d file is downloaded.' %(i-2))
    os.unlink('temp.pdf')
