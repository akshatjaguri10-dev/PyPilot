import os
import subprocess
import tkinter as tk
from tkinter import filedialog

from ui import (
    HOME_DIR, MUTED,
    heading, make_button, make_status, make_listbox, show_error
)


# ---------- LOGIC ----------
def list_folders(path):
    return [
        name for name in os.listdir(path)
        if os.path.isdir(os.path.join(path, name))
    ]


# ---------- UI ----------
def build(page):
    folder_paths = []

    heading(
        page,
        "List Folders",
        "Choose a directory to see the folders inside it. "
        "Double-click a folder to open it in Finder."
    )

    def show_folders():
        path = filedialog.askdirectory(
            title="Choose a directory",
            initialdir=HOME_DIR
        )
        if not path:
            return

        folder_list.delete(0, tk.END)
        folder_paths.clear()

        try:
            folders = list_folders(path)

            for name in folders:
                folder_list.insert(tk.END, "📁  " + name)
                folder_paths.append(os.path.join(path, name))

            if not folders:
                folder_list.insert(tk.END, "No folders found.")

            folder_status.config(text=f"Location: {path}", fg=MUTED)

        except OSError as error:
            show_error(error)

    make_button(page, "Choose Directory", show_folders)
    folder_status = make_status(page)

    folder_list = make_listbox(page, 11)
    folder_list.pack(fill="both", expand=True, padx=28, pady=(0, 20))

    def open_folder(event=None):
        selection = folder_list.curselection()
        if not selection:
            return

        index = selection[0]
        if index >= len(folder_paths):  # the "No folders found." row
            return

        try:
            subprocess.Popen(["open", folder_paths[index]])  # macOS Finder
        except OSError as error:
            show_error(error)

    folder_list.bind("<Double-Button-1>", open_folder)