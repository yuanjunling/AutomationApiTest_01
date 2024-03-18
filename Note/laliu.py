import threading
import os


def laliu_ffmpeg(i):
    command = f"ffplay rtmp://10.0.2.187/live/livestream{i} -fflags nobuffer -flags low_delay -framedrop -strict experimental"
    os.system(command)


threads = []
for i in range(2):
    t = threading.Thread(target=laliu_ffmpeg, args=(i,))
    threads.append(t)
    t.start()


for thread in threads:
        thread.join()
