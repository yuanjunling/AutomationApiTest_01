#!/bin/bash


file_path="/path/to/generate/file.txt"


file_size=1073741824  # 1GB


available_space=$(df -BM . | awk 'NR==2{print $4}' | tr -d 'M')
if [ $available_space -lt $file_size ]; then
    echo "磁盘空间不足，无法生成文件。"
    exit 1
fi


dd if=/dev/zero of=$file_path bs=1 count=1 seek=$((file_size-1))

echo "文件生成完成：$file_path"