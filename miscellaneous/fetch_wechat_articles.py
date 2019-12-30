# -*- coding: utf-8 -*-
# author: Guangqiang Lu time:2019/12/30
# Email: gq4350lu@hotmail.com
# If not explicitly pointed out, all the codes are written by myself.

import bs4, requests
import re, os, shutil
import pdfkit, threading

def url_to_pdf(url, pdf_file):
    path_wkhtmltopdf = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'
    config = pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf)
    pdfkit.from_url(url, pdf_file, configuration=config)
    print('done')

def downfile(start, end):
    for i in range(start, end):
        pdffile = os.path.join(pdffolder, '0%d_.pdf' %i)
        url_to_pdf(urls[i],pdffile)

        print('The No.%d file is downloaded.' %i)


def main():
    global pdffolder, urls
    downthreads, urls= [], []

    res=requests.get('https://mp.weixin.qq.com/s/HMT2fwf1gE8SSNZKd1uf6A')
    res.raise_for_status()
    with open('p100.html', 'wb') as f:
        for chunk in res.iter_content(100000):
            f.write(chunk)

    regex=re.compile(r'weixin')
    pdffolder = "C:\\Users\\Basanwei\\Downloads\\pdf"
    f=open('p100.html','r+', encoding='UTF-8')
    soup=bs4.BeautifulSoup(f.read(),'html.parser')
    tags=soup.find_all(href=regex)
    for tag in tags:
        urls.append(tag['href'])

    for i in range(0,100,20):
        downthread=threading.Thread(target=downfile, args=(i, i+20))
        downthreads.append(downthread)
        downthread.start()

    for t in downthreads:
        t.join()
    print('The download task finished.')

if __name__=="__main__":
    main()