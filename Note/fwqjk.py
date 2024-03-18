import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt


class HoverLineChartApp:
    def __init__(self, master, data):
        self.master = master
        self.data = data
        self.popup_window = None

        # Button to open the line chart in a popup window
        open_button = tk.Button(master, text="Open Line Chart", command=self.show_line_chart)
        open_button.pack()

    def show_line_chart(self):
        # Create a new toplevel window
        self.popup_window = tk.Toplevel(self.master)
        self.popup_window.title("稳定性信噪比折线图")

        # Create a matplotlib figure
        self.fig, self.ax = plt.subplots(figsize=(5, 3), dpi=100)

        # Embed the matplotlib figure into the Toplevel window
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.popup_window)
        self.widget = self.canvas.get_tk_widget()
        self.widget.pack(fill=tk.BOTH, expand=True)

        # Data for the line chart
        self.x_data = range(len(self.data))
        self.y_data = self.data

        # Plot the line chart
        self.line, = self.ax.plot(self.x_data, self.y_data, marker='o', pickradius=5)
        self.ax.set_title("Hover over a point to see details")
        self.ax.set_xlabel("X-axis")
        self.ax.set_ylabel("Y-axis")

        # Annotation for hover details
        self.annot = self.ax.annotate("", xy=(0, 0), xytext=(20, 20),
                                      textcoords="offset points",
                                      bbox=dict(boxstyle="round", fc="w"),
                                      arrowprops=dict(arrowstyle="->"))
        self.annot.set_visible(False)

        # Connect the event handler for motion events
        self.canvas.mpl_connect("motion_notify_event", self.hover)

        # Refresh the canvas
        self.canvas.draw()

    def hover(self, event):
        if event.inaxes == self.ax:
            cont, ind = self.line.contains(event)
            if cont:
                self.update_annot(ind)
                self.annot.set_visible(True)
                self.canvas.draw_idle()
            else:
                if self.annot.get_visible():
                    self.annot.set_visible(False)
                    self.canvas.draw_idle()

    def update_annot(self, ind):
        pos = self.line.get_path().vertices[ind["ind"][0]]
        self.annot.xy = pos
        text = f"x={pos[0]:.2f}, y={pos[1]:.2f}"
        self.annot.set_text(text)
        if self.annot.get_visible():
            self.canvas.draw_idle()

        # Example usage


if __name__ == "__main__":
    root = tk.Tk()
    data = [1, 2, 3, 2, 4, 6, 5, 4, 3, 5, 7, 6]
    app = HoverLineChartApp(root, data)
    root.mainloop()