# 微信公众号数据集爬取  
本项目用于爬取微信公众号，她主要由这三个部分构成  

- [cookies](#cookies)
- [link](#link)
- [main-wechat](#main-wechat)
	
# cookies   
本部分是为了获得访问公众号管理平台登录界面的cookie而设计的  
通过扫描二维码并登录，系统会自动获取所需的密钥  
**注意**：  
1.在扫描使用前，你需要首先自己注册一个微信公众号（可以参考:https://zhuanlan.zhihu.com/p/88147406)  
2.在使用前，你需要按所需位置安装edge driver (也可以根据你的喜好使用其他浏览器内核）
# link  
本部分用于获取你所需公众号发文的标题链接与时间  
你需要使用Fillder抓包工具获得"User-Agent":与**fakeid**，这里的fakeid就是你所需公众号的唯一标识。  
项目最后会将数据以xlsx格式存储在你所指定的目录下  
Fillder工具的使用可以参考：https://zhuanlan.zhihu.com/p/410150022

# main-wechat  
本部分用于获得点赞数与阅读数，界面会实时的打印出数据
**注意**：link项目中所得到的文件在这里是必须的  
由于微信有反爬取机制，请将爬取时间的间隔设定略大些  
在出现访问问题时，及时更改对应的4个参数：1.uin  2.pass_ticket 3.appmsg_token 4.key   
他们需要自己从抓的包里面的请求头里面去获取  

# WeChat Official Account Data Scraping
This project is used to scrape data from WeChat official accounts. It mainly consists of these three parts:  
- [cookies-EN](#cookies-EN)
- [link-EN](#link-EN)
- [main-EN](#main-EN)
# cookies-EN:  
This part is designed to obtain cookies for accessing the login page of the WeChat official account management platform. By scanning the QR code and logging in, the system will automatically obtain the required keys.   
Before scanning, you need to register a WeChat official account yourself (you can refer to: https://zhuanlan.zhihu.com/p/88147406)  
Before use, you need to install the edge driver in the required location (you can also use other browser kernels according to your preference).  
# link-EN:  
This part is used to obtain the title links and time of the articles published by the WeChat official account you need. You need to use the Fillder capture tool to obtain "User-Agent" and fakeid, where fakeid is the unique identifier of the WeChat official account you need.  
The project will store the data in xlsx format in the directory you specified.  
You can refer to: https://zhuanlan.zhihu.com/p/410150022 for the usage of the Fillder tool.  

# main-wechat-EN:    
This part is used to obtain the number of likes and readings, and the interface will print out the data in real-time.  
Note: The files obtained in the link project are required here.  
Due to WeChat's anti-scraping mechanism, please set the interval of scraping time slightly longer.  
When encountering access issues, promptly change the corresponding 4 parameters: 1. uin 2. pass_ticket 3. appmsg_token 4. key.  
You need to obtain them from the request header in the captured packet.  




