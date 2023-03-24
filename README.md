# 使用说明
一切的一切，都是得益于Openai最近也限制了Openai这个库请求时的IP，我将其放到我的R2S中并通过DDNS-GO去进行解析。

准备：
1. 一个国外的网络环境
2. 一个Python环境

# 使用过程
## 1.安装依赖
```bash
pip3 install -r requirements.txt
```
## 2.运行
```bash
python3 main.py
```
## 3.端口
默认端口为65111
## 请求
请求：http://IP:65111/?q=xxx