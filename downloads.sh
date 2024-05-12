#!/bin/bash

# 定义待执行的 Python 脚本列表
PYTHON_SCRIPTS=(
    "downloads_html.py"
    "downloads_path.py"
    "downloads_image.py"
)

# 遍历 Python 脚本列表，并等待用户确认是否执行每个脚本
for script in "${PYTHON_SCRIPTS[@]}"; do
    read -p "执行 $script，确认执行？(y/n): " choice
    case "$choice" in
        y|Y )
            # 如果用户选择执行，则执行相应的 Python 脚本
            echo "正在执行 $script ..."
            python3 "$script"
            ;;
        * )
            # 如果用户选择不执行，则提示并跳过当前脚本
            echo "跳过 $script ..."
            ;;
    esac
done


