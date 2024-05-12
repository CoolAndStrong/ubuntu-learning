from bs4 import BeautifulSoup
import requests
import os

def get_valid_url():
    while True:
        url = input("请输入网页地址：")
        if url.strip():  # 检查是否输入了有效的非空网址
            return url
        else:
            print("无效的网页地址，请输入有效的URL。")

def save_webpage_content(url):
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
        }

        response = requests.get(url, headers=headers)
        response.raise_for_status()  

        print("网页请求成功")
        
        html_content = response.text

        # 保存网页内容到文件
        file_name = "page_content.html"
        with open(file_name, 'w', encoding='utf-8') as file:
            file.write(html_content)

        print("网页内容已保存到文件:", file_name)

    except requests.exceptions.RequestException as e:
        print("网络请求错误:", e)

    except Exception as e:
        print("发生异常:", e)

if __name__ == "__main__":
    url = get_valid_url()
    save_webpage_content(url)
