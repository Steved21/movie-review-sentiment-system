from tkinter import *
from PIL import Image, ImageTk
import threading
import time
import webbrowser
from app import app

# START FLASK SERVER
def run_flask():
    app.run()

# OPEN BROWSER
def open_browser():
    time.sleep(10)
    webbrowser.open("http://127.0.0.1:5000")

# CLOSE SPLASH SCREEN
def close_splash():
    splash.destroy()

# CREATE WINDOW
splash = Tk()

splash.title("Movie Review Sentiment Analizer")

# REMOVE TITLE BAR
splash.overrideredirect(True)

# WINDOW SIZE
width = 1500
height = 780

screen_width = splash.winfo_screenwidth()
screen_height = splash.winfo_screenheight()

x = int((screen_width / 2) - (width / 2))
y = int((screen_height / 2) - (height / 2))

splash.geometry(f"{width}x{height}+{x}+{y}")

# BACKGROUND COLOR
splash.configure(bg="#020817")
# Frame = Frame(splash, bg="#020817")
# Frame.pack(expand=True, fill="both")

# LOGO IMAGE
logo = Image.open("static/image/logo.png")

logo = logo.resize((220, 220))

logo_image = ImageTk.PhotoImage(logo)

logo_label = Label(
    splash,
    image=logo_image,
    bg="#020817"
)

logo_label.pack(pady=20)

# TITLE
title = Label(
    splash,
    text="AI MOVIE REVIEW",
    font=("Arial", 28, "bold"),
    fg="white",
    bg="#020817"
)

title.pack()

# SUBTITLE
subtitle = Label(
    splash,
    text="Sentiment Analysis System",
    font=("Arial", 14),
    fg="#9ca3af",
    bg="#020817"
)

subtitle.pack(pady=10)

# LOADING TEXT
loading = Label(
    splash,
    text="Loading...",
    font=("Arial", 12),
    fg="#facc15",
    bg="#020817"
)

loading.pack(pady=20)

# START FLASK
threading.Thread(target=run_flask).start()

# OPEN BROWSER
threading.Thread(target=open_browser).start()

# CLOSE AFTER 5 SECONDS
splash.after(90000, close_splash)

splash.mainloop()