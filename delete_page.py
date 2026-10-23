import os
import tkinter as tk
from tkinter import filedialog, messagebox

from ui import (
    HOME_DIR, DANGER, DANGER_HOVER, GREEN, RED,
    heading, make_button, make_status, make_path_label
)


# ---------- LOGIC ----------
def delete_file(path):
    if not os.path.isfile(path):
        return False, "The selected file does not exist."

    try:
        os.remove(path)
    except OSError as error:
        return False, f"Could not delete file: {error}"

    return True, "File deleted successfully."


# ---------- UI ----------
def build(page):
    heading(
        page,
        "Delete File",
        "Select a file and confirm before deleting it."
    )

    selected_file = tk.StringVar()
    delete_label = make_path_label(page, "No file selected")

    def choose_file():
        path = filedialog.askopenfilename(
            title="Choose a file to delete",
            initialdir=HOME_DIR
        )
        if path:
            selected_file.set(path)
            delete_label.config(text=path)
            delete_status.config(text="")

    make_button(page, "Choose File", choose_file)

    def remove_file():
        path = selected_file.get()

        if not path:
            delete_status.config(text="Choose a file first.", fg=RED)
            return

        confirm = messagebox.askyesno(
            "Confirm Delete",
            f"Are you sure you want to delete this file?\n\n{path}"
        )
        if not confirm:
            return

        success, message = delete_file(path)
        delete_status.config(text=message, fg=GREEN if success else RED)

        if success:
            selected_file.set("")
            delete_label.config(text="No file selected")

    make_button(
        page, "Delete Selected File", remove_file,
        color=DANGER, hover=DANGER_HOVER
    )
    delete_status = make_status(page)