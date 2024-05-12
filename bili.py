from bs4 import BeautifulSoup
from selenium import webdriver
import time

# 设置Chrome浏览器驱动路径
chrome_driver_path = "/home/sc666/html/chromedriver-linux64"

# 接受用户输入的网页地址
url = input("请输入B站视频页面地址: ")

try:
    # 使用Selenium打开网页
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")  # 无界面模式
    webdriver = webdriver.Chrome(executable_path=chrome_driver_path, options=options)
    webdriver.get(url)

    # 等待页面加载
    time.sleep(5)

    # 使用Beautiful Soup解析网页内容
    soup = BeautifulSoup(webdriver.page_source, 'html.parser')

    # 查找所有包含视频链接的元素
    video_links = []
    for iframe in soup.find_all('iframe'):
        src = iframe.get('src')
        if src and 'player.bilibili.com' in src:
            video_links.append(src)

    if not video_links:
        print("未找到视频链接")
        exit()

    # 提取视频链接中的BV号
    bv_number = video_links[0].split('/')[-1].split('?')[0]

    # 输出视频链接
    video_url = f"https://www.bilibili.com/video/{bv_number}"
    print("视频链接:", video_url)

except Exception as e:
    print("发生异常:", e)

finally:
    # 关闭浏览器
    webdriver.quit()

