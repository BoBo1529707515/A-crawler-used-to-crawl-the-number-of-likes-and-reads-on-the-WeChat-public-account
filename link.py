import requests
import json
import re
import time
from openpyxl import Workbook

with open("cookies.txt", "r") as file:
    cookie = file.read()
cookies = json.loads(cookie)
url = "https://mp.weixin.qq.com"

response = requests.get(url, cookies=cookies)
print(response.url)
token = re.findall(r'token=(\d+)', str(response.url))[0]  # 从url中获取token

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36 Edg/94.0.992.50",
    "Referer": "https://mp.weixin.qq.com/cgi-bin/appmsg?t=media/appmsg_edit_v2&action=edit&isNew=1&type=77&createType=0&token="+token+"&lang=zh_CN",
    "Host": "mp.weixin.qq.com",
}

# 创建一个新的 Excel 工作簿
wb = Workbook()
ws = wb.active

# 添加表头
ws.append(["文章ID", "标题", "链接", "发布时间"])

for j in range(1, 30, 1):
    begin = (j-1)*5
    requestUrl = "https://mp.weixin.qq.com/cgi-bin/appmsg?action=list_ex&begin="+str(begin)+"&count=5&fakeid=Mzg3MzYyMzgzOA==&type=9&query=&token="+token+"&lang=zh_CN&f=json&ajax=1"
    search_response = requests.get(requestUrl, cookies=cookies, headers=headers)
    re_text = search_response.json()
    print(re_text)
    article_list = re_text.get("app_msg_list")
    for article in article_list:
        timestr = article["create_time"]
        timeArray = time.localtime(int(timestr))
        otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray) # 文章发布时间
        ws.append([article["aid"], article["title"], article["link"], otherStyleTime])

# 保存 Excel 文件
wb.save(r'C:\Users\15297\Desktop\articles——WST.xlsx')
