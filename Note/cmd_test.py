# import multiprocessing
# import os


# def run_ffmpeg(i):
#     command = f"ffmpeg -re -i F:/video/source.flv -flvflags no_duration_filesize -c copy -f flv rtmp://10.0.2.187/live/livestream{i}"
#     os.system(command)


# if __name__ == "__main__":
#     processes = []
#     for i in range(10):
#         p = multiprocessing.Process(target=run_ffmpeg, args=(i,))
#         processes.append(p)
#         p.start()

#     for process in processes:
#         process.join()

import threading
import os


def run_ffmpeg(i,Filepath,encoder,server_url):
    command = f"ffmpeg -re -i {Filepath} -flvflags no_duration_filesize {encoder} -f flv {server_url}{i}"
    os.system(command)


if __name__ == "__main__":
    Filepath = "E://video//source.flv"
    encoder = "-c:v libx264"
    server_url= "rtmp://10.0.2.187/live/livestream"
    threads = []
    for i in range(10):
        t = threading.Thread(target=run_ffmpeg, args=(i, Filepath, encoder))
        threads.append(t)
        t.start()

    for thread in threads:
        thread.join()
