import tkinter as tk
from tkinter import scrolledtext
import threading
import queue
import subprocess
import platform


class PingsButtons:
    def __init__(self, master):
        self.master = master
        self.popup_window = None
        self.result_queue = queue.Queue()

        # Button to open the ping tool in a popup window
        open_button = tk.Button(master, text="ping包", command=self.show_ping_tool)
        open_button.grid(row=14, column=1)

        # Check the platform and set the ping command accordingly
        self.ping_command = "ping" if platform.system().lower() == "windows" else "ping -c"

    def show_ping_tool(self):
        self.popup_window = tk.Toplevel(self.master)
        self.popup_window.title("Ping Tool")

        tk.Label(self.popup_window, text="Enter the host to ping:").grid(row=0, column=0)
        self.target_host_entry = tk.Entry(self.popup_window)
        self.target_host_entry.grid(row=0, column=1)

        tk.Label(self.popup_window, text="Enter the number of pings (1-500):").grid(row=1, column=0)
        self.ping_count_entry = tk.Entry(self.popup_window, width=10)
        self.ping_count_entry.grid(row=1, column=1)
        self.ping_count_entry.insert(0, "4")

        ping_button = tk.Button(self.popup_window, text="Ping", command=self.on_ping_button_click)
        ping_button.grid(row=2, column=0, columnspan=2)

        self.result_text = scrolledtext.ScrolledText(self.popup_window, wrap=tk.WORD, width=60, height=15)
        self.result_text.grid(row=3, column=0, columnspan=2)

        # Check the result queue periodically and update the result text if there's any new message
        self.check_result_queue()

    def on_ping_button_click(self):
        target_host = self.target_host_entry.get()
        try:
            ping_count = int(self.ping_count_entry.get())
            if ping_count < 1 or ping_count > 500:
                raise ValueError("Ping count must be between 1 and 500.")
        except ValueError as e:
            self.add_result(f"Warning: {e}")
            return

        if target_host:
            self.result_text.delete('1.0', tk.END)
            ping_thread = threading.Thread(target=self.ping_target, args=(target_host, ping_count))
            ping_thread.start()
        else:
            self.add_result("Warning: Please enter a valid host address")

    def ping_target(self, target_host, ping_count):
        try:
            if platform.system().lower() == "windows":
                completed_process = subprocess.run([self.ping_command, target_host, '-n', str(ping_count)],
                                                   capture_output=True, text=True)
            else:
                completed_process = subprocess.run([self.ping_command, str(ping_count), target_host],
                                                   capture_output=True, text=True)

            output = completed_process.stdout
            if completed_process.returncode != 0:
                output += "\n" + completed_process.stderr

            self.add_result(output)
        except Exception as e:
            self.add_result(f"Error: {e}")

    def add_result(self, text):
        self.result_queue.put(text)

    def check_result_queue(self):
        try:
            while True:
                result = self.result_queue.get_nowait()
                self.result_text.insert(tk.END, result + "\n")
                self.result_text.see(tk.END)
        except queue.Empty:
            self.popup_window.after(100, self.check_result_queue)

        # Create the main window and run the app


root = tk.Tk()
ping_buttons = PingsButtons(root)
root.mainloop()