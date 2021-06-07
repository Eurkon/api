## 前言

由于 Vercel 搭建 API 的限制，为了实现根据业务请求返回不同的数据，需要以参数的形式调用不同的方法，如 `域名/api?api=weibo_top` 表示请求 `weibo_top` 方法

**请求示例**
  - 无其他参数：`https://api.eurkon.vercel.app/api?api=weibo_top`
  - 有其他参数：`https://api.eurkon.vercel.app/api?api=weibo_top&p1=v1&p2=v2...` 其中 `&p1=v1&p2=v2...` 为其他参数。

## 自建 API

| 模块 | 功能 | 请求地址 | 其他参数 | 返回格式 |
| --- | --- | --- | --- | --- |
| `/baidu/api` | 重定向请求百度统计网站，解决跨域问题 | `域名/api?api=baidu_tongji` | 与百度统计请求参数一致 | JSON |
| `/weibo/api` | 爬取微博热搜 | `域名/api?api=weibo_top` | 无 | JSON |

## 常用 API

| 功能 | 请求地址 | 返回格式 |
| --- | --- | --- |
| 根据月份 `month`（如 01）返回百度百科某个月份的历史今日 | `https://baike.baidu.com`<br>`/cms/home/eventsOnHistory/`month`.json` | JSON | 
| 返回 ip、行政区编码、地址 | `https://pv.sohu.com`<br>`/cityjson?ie=utf-8` | Text |
| 根据 `ip` 返回地址拼音、国家、天气、温度、湿度| `https://wttr.in`<br>`/`ip`?format="%l+\\+%c+\\+%t+\\+%h"` | Text |

## 常用 API 网站

- **[博天 API](https://api.btstu.cn/)**
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