# -!- coding: utf-8 -!-
# login.py 用于保存微信帐号登录信息
# 以下代码中的微信登录帐号密码需要修改

import time
import json
from selenium.webdriver.edge.options import Options
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
edge_driver_path = r'F:\edgedriver_win32 (1)\msedgedriver.exe'

# 创建 EdgeOptions 对象
edge_options = Options()

# 创建 Edge 服务对象
service = Service(edge_driver_path)

# 创建 Edge 浏览器对象
driver = webdriver.Edge(service=service, options=edge_options)
driver = webdriver.Edge()
driver.get("https://mp.weixin.qq.com/") # 微信公众平台网址
time.sleep(15)


#此时会弹出扫码页面，需要微信扫码
cookies = driver.get_cookies()  # 获取登录后的cookies
print(cookies)
cookie = {}
for items in cookies:
    cookie[items.get("name")] = items.get("value")
# 将cookies写入到本地文件，供以后程序访问公众号时携带作为身份识别用
with open('cookies.txt', "w") as file:
    #  写入转成字符串的字典
    file.write(json.dumps(cookie))
