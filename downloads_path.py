from bs4 import BeautifulSoup
import os

def save_image_paths(html_file_path, output_file):
    with open(html_file_path, 'r', encoding='utf-8') as file:
        html_content = file.read()

    soup = BeautifulSoup(html_content, 'html.parser')

    # 找出所有图像标签（<img>）
    images = soup.find_all('img')

    # 将图像路径写入文件
    with open(output_file, 'w', encoding='utf-8') as out_file:
        for img in images:
            img_url = img.get('src')
            if img_url:
                out_file.write(img_url + '\n')
    
    print("图像路径已保存到文件:", output_file)

if __name__ == "__main__":
    html_file_path = "page_content.html"  # 更改为你保存的 HTML 文件的路径
    output_file = "image_paths.txt"  # 结果保存的文件路径
    save_image_paths(html_file_path, output_file)
