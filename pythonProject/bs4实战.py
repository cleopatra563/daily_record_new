import re

import requests
from bs4 import BeautifulSoup
import csv

#BeautifulSoup对象获取html内容
#find_all("标签",attrs = {"属性":"属性值"}),find()
f = open("菜价.csv",'w',encoding= 'utf-8',newline='')
csvwriter = csv.writer(f)

#利用BeautifulSoup检索页面源代码
url = 'https://zhujia.zhuwang.cc/lists.shtml'
resp = requests.get(url)
#print(resp.text)

page = BeautifulSoup(resp.text,"html.parser")
#print(page)

#定位页面源代码数据
table_list = page.find_all("table",attrs = {"class":"jgphdata_list"})
#print(table_list)
for table in table_list:
    tr_list = table.find_all('tr')[1:]
    #print(tr_list)
    for tr in tr_list:
        tds = tr.find_all('td')
        index = tds[0].text
        region = tds[1].text
        province = tds[2].text
        price_high = tds[3].text
        price_low = tds[4].text
        # print(index,region,province,price_high,price_low)
        csvwriter.writerow([index, region, province, price_high, price_low])

