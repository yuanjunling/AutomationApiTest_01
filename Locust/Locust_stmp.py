from locust import User, task, between
import subprocess


class WebsiteUser(User):
    wait_time = between(5, 15)

    def on_start(self):
        self.subproc = subprocess.Popen(
            [
                "ffmpeg",
                "-re",
                "-i",
                "E:\\video\\source.flv",
                "-c",
                "copy",
                "-f",
                "flv",
                "-flvflags",
                "no_duration_filesize",
                "rtmp://10.0.2.187/live/livestream",
            ]
        )

    @task
    def view_items(self):
        pass

    def on_stop(self):
        self.subproc.kill()
