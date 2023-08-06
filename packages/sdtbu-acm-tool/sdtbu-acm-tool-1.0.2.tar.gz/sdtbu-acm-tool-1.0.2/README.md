# 山东工商学院acm辅助工具

## OJ网站账号移植

### **[ 介绍 ]** 
将一个账号所做过的所有题移植到另一个账号，部分题目无法转移  

### **[ 使用说明 ]** 
#### 1. 安装依赖
如果您的python版本大于3.9或者您的操作系统非Windows系统，则无法开启验证码自动识别模式，需要手动输入验证码  
如果确定您的python版本小于3.9且您的操作系统为Windows系统，则使用以下命令安装依赖
```bash
pip install ddddocr -i https://pypi.mirrors.ustc.edu.cn/simple
```
#### 2. 用户登录

#### **「 校内使用 」** 
必须保证您的电脑已经连接到校园网，然后使用以下代码登录
```python
from acm.oj import OJ

user = OJ(user_id='您的账号', 
          password='您的密码',
          mode='校内',           # 访问模式 [校内/校外]
          code_mode='自动',       # 验证码识别模式 [自动/手动]
          ).login()
```
或者使用以下代码登录
```python
from acm.oj import OJ

user = OJ('你的账号', '你的密码').login()
```
**注:校内模式还未经过测试**
#### **「 校外使用 」**
在使用之前，您需要先获取wvpn的token  
获取方法：  
1. 打开链接：[https://wvpn.sdtbu.edu.cn](https://wvpn.sdtbu.edu.cn)并扫码登录, 如果您已经登录过wvpn，则跳过此步骤[![zzuN0x.png](https://s1.ax1x.com/2022/12/27/zzuN0x.png)](https://imgse.com/i/zzuN0x)
2. 打开开发者工具(通常为F12)，切换到Network选项卡(中文为"网络")，然后点击刷新按钮(或者按下F5)[![zzuwtO.png](https://s1.ax1x.com/2022/12/27/zzuwtO.png)](https://imgse.com/i/zzuwtO)
3. 此时会出现大量网络请求，点击第一个网络请求,此时「 wengine_vpn_ticketwvpn_sdtbu_edu_cn 」的值便是我们所需的token，如果该值显示不完整，请调整窗口直至调整至完全显示为止(以下操作将采用图中的token值演示)[![zzu59g.md.png](https://s1.ax1x.com/2022/12/27/zzu59g.md.png)](https://imgse.com/i/zzu59g)
然后您可以使用以下代码进行登录
```python
from acm.oj import OJ

user = OJ(user_id='您的账号', 
          password='您的密码',
          mode='校外',           # 访问模式 [校内/校外]
          code_mode='自动',       # 验证码识别模式 [自动/手动]
          wvpn_token='39a7de9aad39f158'
          ).login()
```
或者使用以下代码登录
```python
from acm.oj import OJ

user = OJ('你的账号', '你的密码', wvpn_token='39a7de9aad39f158').login()
```
#### 3. 功能演示
### **[ 移植账号 ]**
注意：校外访问模式同时只能登录一个账号，如果您已经登录了一个账号，那么您将无法再登录另一个账号，如果您需要登录另一个账号，那么您需要先退出当前账号，然后再登录另一个账号
一个转移账号的例子:
```python
from acm.oj import OJ

user_1 = OJ('你的账号', '你的密码', wvpn_token='39a7de9aad39f158').login()
user_1.save('user_1.json')  # 保存账号信息

user_2 = OJ('你的账号', '你的密码', wvpn_token='39a7de9aad39f158').login()
user_2.load_and_submit(
    'user_1.json', 
    10 # 题目提交间隔时间（单位: 秒），速度过快可能会导致提交失败
)  # 加载账号信息并提交题目
```

### **[ 提交题目 ]**
一个提交题目的例子:

```python
from acm.oj import OJ

user = OJ('你的账号', '你的密码', wvpn_token='39a7de9aad39f158').login()
user.submit(
    10, # 题目ID
    '你的代码类型', # 代码类型
    '你的代码', # 代码
)
```
其中代码类型有以下几种:
> C  
> C++  
> Pascal  
> Java  
> Ruby  
> Python  

### **[ 获取已完成题目信息 ]**
一个获取已完成题目信息的例子:

```python
from acm.oj import OJ

user = OJ('你的账号', '你的密码', wvpn_token='39a7de9aad39f158').login()
datas = user.info()
print(datas)
```

### **[ 测试提交代码 ]**
一个测试提交代码的例子:

```python
from acm.oj import OJ

user = OJ('你的账号', '你的密码', wvpn_token='39a7de9aad39f158').login()
user.submit_test_code()
```
效果如下  
[![zzK1VP.png](https://s1.ax1x.com/2022/12/27/zzK1VP.png)](https://imgse.com/i/zzK1VP)  
[![zzKY8g.png](https://s1.ax1x.com/2022/12/27/zzKY8g.png)](https://imgse.com/i/zzKY8g)  

## 注意事项
请勿使用此项目进行非法操作，否则后果自负  
此仓库仅供学习交流使用，不得用于非法商业用途  

反馈邮箱:  [ 1838696034@qq.com ](mailto:1838696034@qq.com)
