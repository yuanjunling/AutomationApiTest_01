import logging
from Driver.handle_init import handle_ini

rootpath = handle_ini.get_value("rootpath")
file_path = rootpath + "/Log/"

logging.basicConfig(
    level=logging.DEBUG,
    filename=file_path + "/logs.log",
    filemode="a",
    format="%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s",
)

# 创建一个handler,用于输出到控制台
console = logging.StreamHandler()
console.setLevel(logging.DEBUG)

# 设置日志输出格式
formatter = logging.Formatter("%(name)s - %(levelname)s - %(message)s")
console.setFormatter(formatter)

# 将定义好的console日志handler添加到root logger
logging.getLogger().addHandler(console)

logger = logging.getLogger()


