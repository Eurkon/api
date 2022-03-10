## 前言

本文收集了常用的 API 接口以及自己部署于 Vercel 的 Python API 合集。

## 自建 API

### 百度

#### 百度统计

**接口地址：** /baidu/tongji

**描述：** 重定向请求百度统计，解决跨域问题

**请求方式：** GET

**请求参数说明：** [百度统计用户手册](https://tongji.baidu.com/api/manual/)

**请求示例：** 无

#### 百度翻译

**接口地址：** /baidu/translate

**描述：** 百度翻译

**请求方式：** GET

**请求参数说明：**

| 字段名 | 字段说明 | 字段类型 | 默认值 | 是否必填 |
| --- | --- | --- | --- | --- |
| fr | 源语言 | string | 英语 | 否 |
| to | 翻译语言 | string | 中文 | 否 |
| content | 源语言 | string | Hello World | 否 |

**请求示例：** https://api.eurkon.com/baidu/translate?fr=英语&to=中文&content=helloworld


### 谷歌

#### 谷歌翻译

**接口地址：** /google/translate

**描述：** 谷歌翻译

**请求方式：** GET

**请求参数说明：**

| 字段名 | 字段说明 | 字段类型 | 默认值 | 是否必填 |
| --- | --- | --- | --- | --- |
| fr | 源语言 | string | 英语 | 否 |
| to | 翻译语言 | string | 中文 | 否 |
| content | 翻译内容 | string | Hello World | 否 |

**请求示例：** https://api.eurkon.com/google/translate?fr=英语&to=中文&content=helloworld


### 微博

#### 微博热搜

**接口地址：** /weibo/top

**描述：** 爬取微博热搜

**请求方式：** GET

**请求参数说明：** 无

**请求示例：** https://api.eurkon.com/weibo/top

### 工具

#### 生成二维码

**接口地址：** /tools/qrcode

**描述：** 重定向请求百度统计，解决跨域问题

**请求方式：** GET

**请求参数说明：**

| 字段名 | 字段说明 | 字段类型 | 默认值 | 是否必填 |
| --- | --- | --- | --- | --- |
| content | 二维码内容 | string | Hello World | 否 |

**请求示例：** https://api.eurkon.com/api?api=tools_qrcode&content=HelloWorld


### 有道

#### 有道翻译

**接口地址：** /youdao/translate

**描述：** 有道翻译

**请求方式：** GET

**请求参数说明：**

| 字段名 | 字段说明 | 字段类型 | 默认值 | 是否必填 |
| --- | --- | --- | --- | --- |
| content | 翻译内容 | string | Hello World | 否 |

**请求示例：** https://api.eurkon.com/youdao/translate?content=helloworld


## 常用 API

### 百度百科历史今日

**接口地址：** https://baike.baidu.com/cms/home/eventsOnHistory/

**描述：** 百度百科历史今日

**请求方式：** GET

**请求参数说明：**

| 字段名 | 字段说明 | 字段类型 | 默认值 | 是否必填 |
| --- | --- | --- | --- | --- |
| month | 月份 | string | 无 | 是 |

**请求示例：** https://baike.baidu.com/cms/home/eventsOnHistory/01.json

### IP、行政区编码、地址

**接口地址：** https://pv.sohu.com/cityjson

**描述：** 获取当前 IP 地址信息

**请求方式：** GET

**请求参数说明：** 无

**请求示例：** https://pv.sohu.com/cityjson?ie=utf-8

### 地区、国家、天气、温度、湿度

**接口地址：** https://wttr.in/ip

**描述：** 获取当前 IP 地址和天气信息

**请求方式：** GET

**请求参数说明：**

| 字段名 | 字段说明 | 字段类型 | 默认值 | 是否必填 |
| --- | --- | --- | --- | --- |
| format | 返回格式 | string | 无 | 否 |

**请求示例：** https://wttr.in/ip?format="%l+\\+%c+\\+%t+\\+%h"

### 腾讯天气接口

**接口地址：** https://wis.qq.com/weather/common

**描述：** 获取当前 IP 地址和天气信息

**请求方式：** GET

**请求参数说明：**

| 字段名 | 字段说明 | 字段类型 | 默认值 | 是否必填 |
| --- | --- | --- | --- | --- |
| source | 请求类型 pc/wx | string | 无 | 是 |
| weather_type | 查询类型，多个用 &#124; 分隔<br>observe（当前天气）<br>forecast_1h<br>forecast_24h<br> index 穿衣，舒适度等<br>alarm（预警）<br>tips（天气介绍）<br>air（空气质量）<br>rise（日出）| string | 无 | 是 |
| province | 省份 | string | 无 | 是 |
| city | 城市 | string | 无 | 是 |
| county | 县区 | string | 无 | 否 |
| callback | 回调函数，不传直接返回 json | string | 无 | 否 |

**请求示例：** https://wis.qq.com/weather/common?source=xw&weather_type=forecast_1h|forecast_24h|index|alarm|limit|tips&province=广东&city=广州&county=天河

### 豆瓣电影接口

**接口地址：** https://movie.douban.com/j/search_subjects

**描述：** 获取当前 IP 地址和天气信息

**请求方式：** GET

**请求参数说明：**

参考页面：https://movie.douban.com/explore

| 字段名 | 字段说明 | 字段类型 | 默认值 | 是否必填 |
| --- | --- | --- | --- | --- |
| tag | 标签 | string | 无 | 否 |
| type | 类型 | string | movie | 否 |
| sort | 排序 | string | recommend | 否 |
| page_limit | 返回个数 | integer | 20 | 否 |
| page_start | 开始索引 | integer | 0 | 否 |

**请求示例：** https://movie.douban.com/j/search_subjects?type=movie&tag=热门&sort=recommend&page_limit=20&page_start=0

## 常用 API 网站

### [博天 API](https://api.btstu.cn/)

- **随机壁纸**：随机输出各类壁纸
- **毒鸡汤**：随机输出毒鸡汤
- **随机头像**：随机输出各类头像
- **获取 QQ 昵称和头像**：获取 QQ 昵称和头像
- **ICP 备案查询**：在线查询网站 ICP 备案
- **QQ 信息查询**：查询 QQ 的信息
- **QQ 域名报毒检测**：检测域名在 QQ 是否报毒
- **二维码解码**：解析二维码图片
- **Qrcode 二维码**：生成在线二维码
- **域名注册查询**：查询域名是否已被注册
- **搜狗收录量**：查询搜狗收录数量
- **在线 ping**：在线 ping 网站
- **百度收录量**：查询域名百度收录总量
- **IP 签名档**：输出精美 IP 信息图
- **抖音网址检测**：检测网址是否可以在抖音直接打开
- **百度收录判断**：判断网址是否已被百度收录
- **QQ 强制聊天**：无需添加 QQ 好友，直接进入聊天
- **域名过期查询**：查询域名的注册时间与到期时间
- **抖音解析**：解析抖音链接，获取无水印链接
- **语言翻译**：自动识别并翻译
- **QQ 电脑在线状态**：查询 QQ 的电脑在线状态
- **微信域名安全检测**：检测域名在微信是否报毒
- **mrw.so 短网址**：提供 mrw.so 短网址的生成与还原服务
- **机器人云黑名单**：查询各类自动进群机器人等等
- **网站 favicon 图标获取**：获取网站的 favicon.ico 图标
- **网易云音乐解析**：在线解析网易云音乐
- **QQ 手游+微视一键加速**：QQ 手游+微视一键加速（0.2+0.5）天
- **三合一收款码**：合并 QQ，微信和支付宝收款码为一个二维码
- **获取 QQ 群加群链接**：只需要 QQ 群号码即可获取加群链接

## 持续更新中...
