import os
import requests
from bs4 import BeautifulSoup

url = 'https://www.easyapi.com/highmall/service'
index = 0 #抓取的数目标号
maxPage = 1000 #访问次数（图片可能重复，所以也不清楚有多少不重复的图）
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0'}
picSaveDir = 'D:\QiWeiwei\learn\Learn_git\mySpider\mySpider\pics/'
# 'referer': 'https://www.easyapi.com/highmall/service', 

# 保存图片
def save_jpg(res_url):
    global index
    html = BeautifulSoup(requests.get(res_url, headers=headers).text)
    for link in html.find_all('img', {'title': '欣赏美女'}):
        if os.path.exists(picSaveDir + os.path.basename(link.get('src'))):
            print(os.path.basename(link.get('src')) + ' already exist')
            continue
        with open(picSaveDir + os.path.basename(link.get('src')), 'wb') as jpg:
            jpg.write(requests.get(link.get('src')).content)
        print("正在抓取第"+str(index)+"条数据")
        index += 1


#  抓取图片
if __name__ == '__main__':
    for i in range(0, maxPage):
        save_jpg(url)
