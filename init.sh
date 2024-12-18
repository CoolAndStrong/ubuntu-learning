#!/bin/bash

# 当前目录
current_directory=$(pwd)
# 创建虚拟环境
python3 -m venv "${current_directory}/Beautiful"

# 激活虚拟环境
source "${current_directory}/Beautiful/bin/activate"

# 安装所需的包
pip install requests
pip install beautifulsoup4


# 在此处添加您的其他任务
# 例如：python your_script.py
