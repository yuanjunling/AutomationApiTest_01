from ratelimit import rate_limited
import shutil


@rate_limited(0.1 * 1024)  # 500K/s 限速
def copyfile(src, dst):
    with open(src, "rb") as sf:
        with open(dst, "wb") as tf:
            shutil.copyfileobj(sf, tf)


copyfile("F://硬盘测试相关文件//1G", "F://硬盘测试相关文件//2G")
