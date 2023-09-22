import ffmpeg
import threading


def push_stream(input_file, server_url, stream_key):
    ffmpeg.input(input_file).output(
        f"{server_url}/{stream_key} -flvflags no_duration_filesize -re -s 640x360",
        format="flv",
        vcodec="libx265",
        preset="ultrafast",
        b="2000k",
        bufsize="4000k",
    ).run()


def pull_stream(server_url, stream_key, output_file):
    ffmpeg.input(f"{server_url}/{stream_key} ").output(
        output_file, vcodec="copy", acodec="copy"
    ).run()


if __name__ == "__main__":
    input_file = "F:/video/source.flv"  # 本地视频文件路径
    server_url = "rtmp://10.0.2.187/live/"  # 服务器地址和应用名称
    stream_key = "stream_key"  # 推流的流名称或密钥
    output_file = "F:/video/laliu/output1.mp4"  # 拉流后保存的本地文件路径

    # 在线程中启动推流
    push_thread = threading.Thread(
        target=push_stream, args=(input_file, server_url, stream_key)
    )
    push_thread.start()
    # 在主线程中启动拉流
    pull_stream(server_url, stream_key, output_file)
