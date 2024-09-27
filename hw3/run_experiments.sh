#!/bin/bash

# 设置路径
DATA_DIR="../data/optimize/config"
OUTPUT_DIR="./tmp/branch"
EXPERIMENT_PY="./experiment.py"

# 确保输出目录存在
mkdir -p "$OUTPUT_DIR"

# 遍历数据文件夹中的所有csv文件
for file in "$DATA_DIR"/*.csv; do
    # 获取文件名（不包含路径）
    filename=$(basename "$file")
    
    # 调用experiment.py并将输出重定向到对应的文件
    python3.13 "$EXPERIMENT_PY" "$file"  | tee "$OUTPUT_DIR/$filename"
    
    # 在每个文件处理后添加一个分隔符，以符合rq.sh的要求
    echo "#" >> "$OUTPUT_DIR/$filename"
done

