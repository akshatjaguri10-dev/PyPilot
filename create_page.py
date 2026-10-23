import os
import tkinter as tk
from tkinter import filedialog

from ui import (
    HOME_DIR, BG, TEXT, GREEN, RED,
    heading, make_button, make_entry, make_status, make_path_label
)


# ---------- LOGIC ----------
def create_folder(path, folder_name):
    folder_path = os.path.join(path, folder_name)

    if os.path.exists(folder_path):
        return False, "A file or folder with that name already exists."

    try:
        os.makedirs(folder_path)
    except OSError as error:
        return False, f"Could not create folder: {error}"

    return True, f"Folder created: {folder_name}"


# ---------- UI ----------
def build(page):
    heading(
        page,
        "Create Folder",
        "Choose a location and give your new folder a name."
    )

    create_location = tk.StringVar(value=HOME_DIR)
    location_label = make_path_label(page)

    def choose_location():
        path = filedialog.askdirectory(
            title="Choose where to create the folder",
            initialdir=HOME_DIR
        )
        if path:
            create_location.set(path)
            location_label.config(text=path)

    make_button(page, "Choose Location", choose_location)

    tk.Label(
        page, text="Folder name",
        bg=BG, fg=TEXT,
        font=("Arial", 11, "bold")
    ).pack(anchor="w", padx=28, pady=(12, 0))

    create_entry = make_entry(page)

    def make_folder():
        path = create_location.get()
        name = create_entry.get().strip()

        if not path or not name:
            create_status.config(
                text="Choose a location and enter a folder name.",
                fg=RED
            )
            return

        success, message = create_folder(path, name)
        create_status.config(text=message, fg=GREEN if success else RED)

        if success:
            create_entry.delete(0, tk.END)

    make_button(page, "Create Folder", make_folder)
    create_status = make_status(page)