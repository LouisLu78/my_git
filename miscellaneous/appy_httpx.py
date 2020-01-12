# -*- coding: utf-8 -*-
# author: Guangqiang Lu time:2020/1/12
# Email: gq4350lu@hotmail.com
# If not explicitly pointed out, all the codes are written by myself.

import httpx
import pdfkit

def html_to_pdf(html, pdf_file):
    path_wkhtmltopdf = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'
    config = pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf)
    pdfkit.from_file(html, pdf_file, configuration=config)
    print('done')

with httpx.Client() as client:
    res = client.get('https://www.python-httpx.org/api/')
res.raise_for_status()
with open('api.html', 'wb') as f:
    f.write(res.content)

html_to_pdf('api.html','api.pdf')

