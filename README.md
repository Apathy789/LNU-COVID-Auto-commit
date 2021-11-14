<h1 align="center"><a href="https://github.com/JessyTsu1/LNU-COVID-Auto-commit" target="_blank">辽宁大学疫情自动填报脚本</a></h1>
<p align="center">
<a href="https://github.com/JessyTsu1/LNU-COVID-Auto-commit/issues"><img alt="license" src="https://img.shields.io/badge/license-Apache--2.0-blue"/></a>
<a href="https://github.com/JessyTsu1/LNU-COVID-Auto-commit/issues"><img alt="stars" src="https://img.shields.io/github/stars/JessyTsu1/LNU-COVID-Auto-commit"></a>
<a href="https://github.com/JessyTsu1/LNU-COVID-Auto-commit/issues"><img alt="PR" src="https://img.shields.io/badge/PRs-welcome-green"></a>
<a href="https://github.com/JessyTsu1/LNU-COVID-Auto-commit/issues"><img alt="Travis CI" src="https://img.shields.io/badge/build-done-blue"/></a>
</p>

<h1 align="center"><a href="blog.jessytsui.cn" target="_blank">阑干</a></h1>

> 欢迎来我的博客游玩



## 简介

    该脚本可以帮助您操作辽大「疫情填报」，自动完成每日上报。

**注意：此脚本仅用于研究交流学习，使用请自行承担后果**

-------------------------------------------------------------------------------

### 提供bug反馈或建议

提交问题反馈请说明正在使用的python以及相关依赖库版本。

- [Github issue](https://github.com/JessyTsu1/LNU-COVID-Auto-commit/issues)



### **日志**
---
2021/11/14更新：
验证码搞了一下当图像处理大作业了，顺便版本更新了一下，之前的博客也不用了

放在服务器上，后台运行selenium的话，需要加上这些参数：

```
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument('--headless')
browser = webdriver.Chrome(chrome_options=chrome_options)
```

部署过程看这个：

https://blog.csdn.net/weixin_44128602/article/details/113621036



---

2020/11/24更新：
一直懒得搞...说下验证码的解决思路吧

+ 搭个cnn模型训练一下，然后每次启动webdrive调用一下训练好的模型接口。问题是没找到现成好用的代码，得自己从头写，太麻烦了...
+ 保存每个账号的cookie，每次访问的时候带上cookie，可以直接get到/inputExt.asp这个页面，然后有✅的选项就是在<div class="weui-cell__ft"><input>里加了一个 checked='checked'属性

---

2020/11/11更新：
学校增加了图形验证码，我做完Java大作业后会尽快找模型解决一下。另外，我的个人博客由hexo换成了halo，之前的使用方法打不开了，也会尽快部署一下

# **实现操作**

+ 自动上报健康信息

# **脚本依赖**

+ Python 3.6或以上
+ selenium库
+ chrome及chromedriver驱动程序

# 使用方法

+ 首先下载文件![](http://q7nlxgqi3.bkt.clouddn.com/GithubClone.png)
+ 到本地压缩之后创建一个同名txt文件，然后改成bat文件，即`辽大打卡.bat`，不需要写入东西
+ 之后的操作详见[我的博客]([https://jessytsui.cn/2020/03/27/python%E6%AF%8F%E6%97%A5%E8%87%AA%E5%8A%A8%E5%A1%AB%E6%8A%A5/](https://jessytsui.cn/2020/03/27/python每日自动填报/))https://jessytsui.cn/2020/03/27/python%E6%AF%8F%E6%97%A5%E8%87%AA%E5%8A%A8%E5%A1%AB%E6%8A%A5/
