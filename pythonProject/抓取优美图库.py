# 1.拿到主页面的源代码. 然后提取到子页面的链接地址, href
# 2.通过href拿到子页面的内容. 从子页面中找到图片的下载地址 img -> src
# 3.下载图片

import requests
from bs4 import BeautifulSoup
import time

domain = 'https://www.umeitu.com/'
url = "https://www.umeitu.com/bizhitupian/weimeibizhi"

resp = requests.get(url)
resp.encoding = 'utf-8'
# print(resp.text)

main_page = BeautifulSoup(resp.text,"html.parser")
alist = main_page.find('div',attrs = {'class':'TypeList'}).find_all('a')
print(alist)

for a in alist:
    href = a.get('href') # 直接通过get就可以拿到属性的值
    child_href = domain + href.strip("/") #拼接处子页面链接
    # 拿到子页面的源代码
    child_page_resp = requests.get(child_href)
    child_page_resp.encoding = 'utf-8'
    child_page_text = child_page_resp.text
    # 从子页面中拿到图片的下载路径
    child_page = BeautifulSoup(child_page_text,'html.parser')
    d = child_page.find('div',class_="ImageBody")
    img = d.find('img')
    src = img.get('src')
    # 下载图片
    img_resp = requests.get(src)
    # img_resp.content # 这里拿到的是字节
    img_name = src.split('/')[-1] # 拿到url中的最后一个/以后的内容
    # print(src)
    with open('img/'+img_name,'wb') as f:
        f.write(img_resp.content)

    print("over!!!", img_name)
    time.sleep(1)

print("all over!!!")



