import tkinter as tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

root = tk.Tk()
root.title("Chart Test")

# Create a figure
fig = Figure(figsize=(4, 3), dpi=100)
ax = fig.add_subplot(111)
ax.pie([30, 20, 50], labels=["Food", "Transport", "Other"], autopct="%1.1f%%")
ax.set_title("Test Pie Chart")

# Embed into Tkinter
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.get_tk_widget().pack(fill="both", expand=True)
canvas.draw()

root.mainloop()
