import requests
import openpyxl
import time
import pandas as pd
read_all = []

like_all = []
def getMoreInfo(link):
    # 获得mid,_biz,idx,sn 这几个在link中的信息。
    mid = link.split("&")[1].split("=")[1]
    idx = link.split("&")[2].split("=")[1]
    sn = link.split("&")[3].split("=")[1]
    _biz = link.split("&")[0].split("_biz=")[1]

    # 该4个参数，需要自己从抓的包里面的请求头里面去获取，
    uin = 'MjY0MTc0NzIzOQ%3D%3D'
    pass_ticket = '0PqG7qEJMXh9BcPHSiyx%252FTIApmfZPs%252FZ5ZmeKjdgq1EqP7h6JmslTjsyc0txZ4JA1CKrAVWB7cxW5VQ0ix04OQ%253D%253D'
    appmsg_token = '1267_nuhII7YMCKxbwj9dWlv4YgSdb4iyOUertfeUpqu_od8qggpaCsJRUL1DDDLRoEqUgfzG8vhLM8_9rAKh'
    key = "88226e006e9bd97ae3163df10b785436fe7aa5e578d6a58385aec84e6fd332b9cd1e8d811353240b999dbeb1eb10cc8cb23a5373577f9b2f3d1fcd904630cceaee133908e3e0aac420265816fb92a135e594a3a9b7e005d170d83613f650635cf35b3c89a715a49a4193e7e75b5cd036229a2ed3dc38f58049701504e27914fa"

    # 目标url
    url = "http://mp.weixin.qq.com/mp/getappmsgext"

    # 添加Cookie避免登陆操作。Cookie需要自己从抓的包里面去获取
    phoneCookie = "appmsg_token=1267_nuhII7YMCKxbwj9dWlv4YgSdb4iyOUertfeUpqu_od8qggpaCsJRUL1DDDLRoEqUgfzG8vhLM8_9rAKh;rewardsn=;;wxtokenkey=777;wxuin=2641747239;devicetype=Windows11x64;version=63090a13;lang=zh_CN;pass_ticket=0PqG7qEJMXh9BcPHSiyx/TIApmfZPs/Z5ZmeKjdgq1GveyoCHhPwQIT7H/p6wjzjmTejS4NnYJL4jErXtiYT2Q==;wap_sid2=CKe61+sJEooBeV9ISXR0NlFNczh5eWh1OWdQbkhqTFBNUS1pY0NCNWExbzhmeWhqYl9mQ2tnTTk5NTAxZlV6NjZ4T0pkY0RNMU8wdFBmSDQzSHQyWUE1SzlKMHFrVHJZV0FVMmJWd3NteVRCQzdlS0tEb05hdVN3U2hDY1ZjQ0M2Y2xLMzdkMXdTeUR0RVNBQUF+MO26urEGOA1AAQ=="

    # 这里的"User-Agent"最好为手机浏览器的标识
    headers = {
        "Cookie": phoneCookie,
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36 MicroMessenger/6.5.2.501 NetType/WIFI WindowsWechat QBCore/3.43.901.400 QQBrowser/9.0.2524.400"
    }

    # 添加data，`req_id`、`pass_ticket`。
    data = {
        "is_only_read": "1",
        "is_temp_url": "0",
        "appmsg_type": "9",
        'reward_uin_count': '0'
    }

    # 根据获取到的参数，构造PSOT请求的params
    params = {
        "__biz": _biz,
        "mid": mid,
        "sn": sn,
        "idx": idx,
        "key": key,
        "pass_ticket": pass_ticket,
        "appmsg_token": appmsg_token,
        "uin": uin,
        "wxtoken": "777",
    }
    # post请求提交后，将返回的respone转为json
    json = requests.post(url, headers=headers, data=data, params=params).json()

    # 获取到阅读数
    read_num = json['appmsgstat']['read_num']
    read_all.append(read_num)
    # 获取到在看书
    like_num = json["appmsgstat"]["like_num"]
    print(read_num, like_num)
    time .sleep(3)
    like_all.append(like_num)
def read_urls_from_excel(file_path):
    wb = openpyxl.load_workbook(file_path)
    sheet = wb.active

    # 从第三列第二行开始逐行读取 URL
    for row in sheet.iter_rows(min_row=2, min_col=3, max_col=3, values_only=True):
        url = row[0]
        yield url


# Excel 文件路径
file_path = r"C:\Users\15297\Desktop\前400.xlsx"

# 读取 Excel 文件中的 URL 并逐个调用 getMoreInfo 函数
for url in read_urls_from_excel(file_path):
    getMoreInfo(url)
data = pd.DataFrame({
    '阅读数':read_all,
    '点赞':like_all,


})
data.to_excel(r'C:\Users\15297\Desktop\4.29.xlsx', index=False)





data.head()
