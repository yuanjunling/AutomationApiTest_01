# coding=utf-8
f = open("test.txt", 'r')  # 读模式
f = open("test.txt", 'w')  # 写模式
f = open("img.bmp",'r+')  # 可读可写
f = open("img.bmp",'w+')  # 可读可写
f = open("img.bmp",'rb')  # 二进制读取

#写入文件 write()方法
lines = ['line1', 'line2']
with open('filename.txt', 'w') as f:
    s = ''
    for data in lines:
        s += data
        s += '\n'
    f.write(s)

#join
lines = ['line1', 'line2']
with open('filename.txt', 'w') as f:
    f.write('\n'.join(lines))

#writelines()方法
lines = ['line1', 'line2']
with open('filename.txt', 'w') as f:
    new_lines = []
    for data in lines:
        new_lines.append(data+'\n')
    f.writelines(new_lines)

#使用生成器
lines = ['line1', 'line2']
with open('filename.txt', 'w') as f:
    f.writelines("%s\n" % l for l in lines)


