#!/usr/bin/python3

#!/usr/bin/python3
import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse
import argparse
from fake_useragent import UserAgent

def get_links(url, use_proxy=False):
    try:
        headers = {'User-Agent': UserAgent().random}
        proxies = {'http': 'http://your_proxy_here', 'https': 'https://your_proxy_here'} if use_proxy else None

        response = requests.get(url, headers=headers, proxies=proxies, timeout=10)
        soup = BeautifulSoup(response.text, 'html.parser')
        links = [a.get('href') for a in soup.find_all('a', href=True)]
        return links
    except Exception as e:
        print(f"获取 {url} 链接时出错：{e}")
        return []

def crawl_and_save(domain, use_proxy=False):
    links = get_links(domain, use_proxy)
    all_links[domain] = links

    # 在处理每个链接时，只保留主域名
    filtered_links = [urlparse(link)._replace(path='', params='', query='', fragment='').geturl() for link in links]
    filtered_links = list(set(filtered_links))

    # 输出到 output_links.txt
    with open("output_links.txt", "a", encoding="utf-8") as output_file:
        output_file.write(f"域名 {domain} 的链接：\n")
        output_file.write("\n".join(filtered_links) + "\n\n")

    # 输出到屏幕
    print(f"域名 {domain} 的链接：\n")
    print("\n".join(filtered_links) + "\n\n")

if __name__ == "__main__":
    # 解析命令行参数
    parser = argparse.ArgumentParser(description="Web scraping script")
    parser.add_argument("--use-proxy", action="store_true", help="使用代理进行请求")
    args = parser.parse_args()

    # 从 domains.txt 读取域名
    with open("domains.txt", "r", encoding="utf-8") as file:
        domains = [line.strip() for line in file]

    # 存储每个域名及其链接的字典
    all_links = {}

    for domain in domains:
        crawl_and_save(domain, args.use_proxy)

