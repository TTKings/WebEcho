# WebEcho
WebEcho 是一个简单而强大的网络爬虫工具，用于快速收集和分析指定域名下的链接。

1. 准备工作

确保你的环境中已经安装了 Python 3，并且具备以下依赖库：

requests
beautifulsoup4
fake_useragent
可以使用以下命令安装依赖：
pip install requests beautifulsoup4 fake_useragent

2. 编写域名列表

在当前目录下创建一个名为 domains.txt 的文本文件，将待爬取的域名一行一个写入文件中

3. 运行 WebEcho

使用以下命令运行 WebEcho：

python WebEcho.py

4. 查看结果

WebEcho 会在当前目录下生成一个 output_links.txt 文件，其中包含了爬取到的链接。同时，程序会将结果在屏幕上显示一遍。

高级用法

使用代理：如果你的网络环境需要使用代理，可以通过添加 --use-proxy 参数来启用代理。例如：

python WebEcho.py --use-proxy
