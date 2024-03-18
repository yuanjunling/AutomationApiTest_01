#!/bin/bash


file_path="/path/to/generate/file.txt"


file_size=1073741824  # 1GB


available_space=$(df -BM . | awk 'NR==2{print $4}' | tr -d 'M')
if [ $available_space -lt $file_size ]; then
    echo "���̿ռ䲻�㣬�޷������ļ���"
    exit 1
fi


dd if=/dev/zero of=$file_path bs=1 count=1 seek=$((file_size-1))

echo "�ļ�������ɣ�$file_path"