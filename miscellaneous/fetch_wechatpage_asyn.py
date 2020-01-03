# -*- coding: utf-8 -*-
# author: Guangqiang Lu time:2020/1/3
# Email: gq4350lu@hotmail.com
# If not explicitly pointed out, all the codes are written by myself.

import bs4, requests
import re, os
import pdfkit, asyncio

async def url_to_pdf(url, pdf_file):
    path_wkhtmltopdf = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'
    config = pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf)
    pdfkit.from_url(url, pdf_file, configuration=config)
    print('done')

async def downfile(i):

    pdffolder = "C:\\Users\\Basanwei\\Downloads\\pdf"
    pdffile = os.path.join(pdffolder, "%s.pdf" % urls[i][1])
    await url_to_pdf(urls[i][0], pdffile)
    print('The No.%d file is downloaded.' %i)

async def main():

    global urls
    urls= []
    regex = re.compile(r'[^a-zA-Z0-9(). :_\u4e00-\u9fa5]')
    f = open('p100.html', 'r', encoding='UTF-8')
    soup = bs4.BeautifulSoup(f.read(), 'html.parser')

    tags = soup.find_all(attrs={'data-linktype': '2'})
    for tag in tags:
        text = regex.sub(' ', tag.text)
        urls.append((tag['href'], text))

    tasks=[downfile(i) for i in range(len(urls))]
    await asyncio.gather(*tasks)

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(main())
    finally:
        loop.close()