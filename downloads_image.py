import os

def download_images(image_paths_file, save_folder):
    # 确保保存图像的文件夹存在
    if not os.path.exists(save_folder):
        os.makedirs(save_folder)

    with open(image_paths_file, 'r', encoding='utf-8') as file:
        for line in file:
            img_url = line.strip()
            if img_url:
                # 获取图像在网页中的相对路径
                img_path = img_url.split('/')[-1]  # 获取最后一部分作为文件名
                img_path0 = img_url.split('/')[-2]  # 获取最后一部分作为文件名
                img_name = f"{img_path0}_{img_path}"  # 图像文件名
                img_file_path = os.path.join(save_folder, img_name)
                # 使用 wget 命令下载图像，并使用自定义命名保存
                os.system(f"wget -P {save_folder} -O {img_file_path} {img_url}")

if __name__ == "__main__":
    image_paths_file = "image_paths.txt"  # 包含图像路径的文本文件
    save_folder = "downloaded_images"  # 图像保存的文件夹路径
    download_images(image_paths_file, save_folder)

