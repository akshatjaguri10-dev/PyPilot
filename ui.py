import os
import tkinter as tk
from tkinter import messagebox

HOME_DIR = os.path.expanduser("~")

# COLORS
BG = "#F4F5F8"
DARK = "#20232B"
SIDEBAR = "#292D37"
SIDEBAR_HOVER = "#414958"
BLUE = "#4788D9"
BLUE_HOVER = "#3274BD"
DANGER = "#C43D48"
DANGER_HOVER = "#A8323C"
TEXT = "#20232B"
MUTED = "#687386"
GREEN = "#16803C"
RED = "#D13D3D"


def heading(page, title, description):
    tk.Label(
        page, text=title,
        font=("Arial", 24, "bold"),
        bg=BG, fg=TEXT
    ).pack(anchor="w", padx=28, pady=(25, 5))

    tk.Label(
        page, text=description,
        font=("Arial", 11),
        bg=BG, fg=MUTED,
        wraplength=700
    ).pack(anchor="w", padx=28, pady=(0, 18))


def flat_button(parent, text, command, bg, hover, **options):
    button = tk.Label(parent, text=text, bg=bg, cursor="hand2", **options)
    button.bind("<Button-1>", lambda event: command())
    button.bind("<Enter>", lambda event: button.config(bg=hover))
    button.bind("<Leave>", lambda event: button.config(bg=bg))
    return button


def make_button(parent, text, command, color=BLUE, hover=BLUE_HOVER):
    button = flat_button(
        parent, text, command,
        bg=color, hover=hover,
        fg="white",
        font=("Arial", 11, "bold"),
        padx=18, pady=9
    )
    button.pack(anchor="w", padx=28, pady=8)
    return button


def make_entry(parent, width=42):
    entry = tk.Entry(
        parent,
        font=("Arial", 12),
        width=width,
        bg="white",
        fg=TEXT,
        insertbackground=TEXT,
        relief="flat",
        highlightthickness=1,
        highlightbackground="#CDD3DE",
        highlightcolor=BLUE
    )
    entry.pack(anchor="w", padx=28, pady=9, ipady=7)
    return entry


def make_status(parent):
    label = tk.Label(
        parent,
        text="",
        font=("Arial", 10),
        bg=BG,
        fg=MUTED,
        wraplength=700,
        justify="left"
    )
    label.pack(anchor="w", padx=28, pady=8)
    return label


def make_listbox(parent, font_size):
    return tk.Listbox(
        parent,
        font=("Arial", font_size),
        bg="white",
        fg=TEXT,
        selectbackground=BLUE,
        selectforeground="white",
        relief="flat",
        highlightthickness=1,
        highlightbackground="#CDD3DE"
    )


def make_path_label(parent, text=HOME_DIR):
    label = tk.Label(parent, text=text, bg=BG, fg=MUTED, wraplength=700)
    label.pack(anchor="w", padx=28)
    return label


def show_error(error):
    messagebox.showerror("PyPilot", str(error))