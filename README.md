## 前言

由于 Vercel 搭建 API 的限制，为了实现根据业务请求返回不同的数据，需要以参数的形式调用不同的方法，如 `域名/api?api=weibo_top` 表示请求 `weibo/api/weibo_top` 方法

**请求示例**
  - 无其他参数：`https://api.eurkon.vercel.app/api?api=weibo_top`
  - 有其他参数：`https://api.eurkon.vercel.app/api?api=weibo_top&p1=v1&p2=v2...` 其中 `&p1=v1&p2=v2...` 为其他参数。

## 自建 API

### 百度
#### 百度统计
  - 文件路径：`/baidu/api/tongji`
  - 请求地址：`域名/api?api=baidu_tongji`
  - 其他参数：百度统计请求参数
  - 返回格式：JSON
  - 请求示例：

### 谷歌

#### 谷歌翻译
  - 文件路径：`/google/api/translate`
  - 请求地址：`域名/api?api=google_translate`
  - 其他参数：
    - from【必填】：源语言
    - to【必填】：翻译语言
    - content【必填】：翻译内容，长度不超过 4891
  - 返回格式：JSON
  - 请求示例：https://api.eurkon.vercel.app/api?api=google_translate&from=英语&to=中文&content=helloworld

### 微博

#### 爬取微博热搜
  - 文件路径：`/weibo/api/top`
  - 请求地址：`域名/api?api=weibo_top`
  - 其他参数：无
  - 返回格式：JSON
  - 请求示例：https://api.eurkon.vercel.app/api?api=weibo_top

### 工具

#### 生成二维码
  - 文件路径：`/tools/api/QRCode`
  - 请求地址：`域名/api?api=tools_qrcode`
  - 其他参数：content【必填】：二维码内容
  - 返回格式：PNG
  - 请求示例：https://api.eurkon.vercel.app/api?api=tools_qrcode&content=https://blog.eurkon.com/

### 模块

#### 功能
  - 文件路径：
  - 请求地址：`域名/api?api=`
  - 其他参数：
  - 返回格式：
  - 请求示例：

## 常用 API

### 百度百科历史今日
  - 请求地址：`https://baike.baidu.com/cms/home/eventsOnHistory/`month`.json`
  - 请求参数：month【必填】
  - 返回格式：JSON
  - 请求示例：https://baike.baidu.com/cms/home/eventsOnHistory/01.json

### IP、行政区编码、地址
  - 请求地址：`https://pv.sohu.com/cityjson?ie=utf-8`
  - 请求参数：无
  - 返回格式：JSON
  - 请求示例：https://pv.sohu.com/cityjson?ie=utf-8

### 地区、国家、天气、温度、湿度
  - 请求地址：`https://wttr.in/`ip`?format="%l+\\+%c+\\+%t+\\+%h"`
  - 请求参数：ip【可填】
  - 返回格式：Text
  - 请求示例：https://wttr.in/?format="%l+\\+%c+\\+%t+\\+%h"

### 腾讯天气接口
  - 请求地址：`https://wis.qq.com/weather/common?source=xw&weather_type=forecast_1h|forecast_24h|index|alarm|limit|tips&province=`province`&city=`city`&county=`county
  - 请求参数：
    - province【必填】：省份
    - city【必填】：城市
    - county【选填】：地区
  - 返回格式：JSON
  - 请求示例：https://wis.qq.com/weather/common?source=xw&weather_type=forecast_1h|forecast_24h|index|alarm|limit|tips&province=广东&city=广州&county=天河

### 豆瓣电影接口
  - 请求地址：`https://movie.douban.com/j/search_subjects?`
  - 请求参数：
    - tag【必填】：标签
    - type【选填】：类型
    - sort【选填】：排序
    - page_limit【选填】：返回个数
    - page_start【选填】：开始索引
  - 返回格式：JSON
  - 请求示例：https://movie.douban.com/j/search_subjects?type=movie&tag=热门&sort=recommend&page_limit=20&page_start=0
  - 备注信息：参考链接填写参数 https://movie.douban.com/explore#!type=movie&tag=热门&sort=recommend&page_limit=20&page_start=0

### API
  - 请求地址：
  - 请求参数：
  - 返回格式：
  - 请求示例：

## 常用 API 网站

### [博天 API](https://api.btstu.cn/)

- **随机壁纸**：随机输出各类壁纸
- **毒鸡汤**：随机输出毒鸡汤
- **随机头像**：随机输出各类头像
- **获取QQ昵称和头像**：获取QQ昵称和头像
- **ICP备案查询**：在线查询网站ICP备案
- **QQ信息查询**：查询QQ的信息
- **QQ域名报毒检测**：检测域名在QQ是否报毒
- **二维码解码**：解析二维码图片
- **Qrcode二维码**：生成在线二维码
- **域名注册查询**：查询域名是否已被注册
- **搜狗收录量**：查询搜狗收录数量
- **在线ping**：在线ping网站
- **百度收录量**：查询域名百度收录总量
- **IP签名档**：输出精美IP信息图
- **抖音网址检测**：检测网址是否可以在抖音直接打开
- **百度收录判断**：判断网址是否已被百度收录
- **QQ强制聊天**：无需添加QQ好友，直接进入聊天
- **域名过期查询**：查询域名的注册时间与到期时间
- **抖音解析**：解析抖音链接，获取无水印链接
- **语言翻译**：自动识别并翻译
- **QQ电脑在线状态**：查询QQ的电脑在线状态
- **微信域名安全检测**：检测域名在微信是否报毒
- **mrw.so短网址**：提供mrw.so短网址的生成与还原服务
- **机器人云黑名单**：查询各类自动进群机器人等等
- **网站favicon图标获取**：获取网站的favicon.ico图标
- **网易云音乐解析**：在线解析网易云音乐
- **QQ手游+微视一键加速**：QQ手游+微视一键加速（0.2+0.5）天
- **三合一收款码**：合并QQ，微信和支付宝收款码为一个二维码
- **获取QQ群加群链接**：只需要QQ群号码即可获取加群链接

## 持续更新中...
