import os
import subprocess
import tkinter as tk
from tkinter import filedialog

from ui import (
    HOME_DIR, TEXT, MUTED, RED,
    heading, make_button, make_entry, make_status,
    make_listbox, make_path_label, show_error
)

PLACEHOLDER = "Enter filename"


# ---------- LOGIC ----------
def search_file(path, filename):
    """Return full paths of files AND folders whose name contains filename."""
    query = filename.lower()
    results = []

    for root, dirs, files in os.walk(path):
        for name in files + dirs:
            if query in name.lower():
                results.append(os.path.join(root, name))

    return results


# ---------- UI ----------
def build(page):
    result_paths = []

    heading(
        page,
        "Search File",
        "Search for a filename inside a directory and its subfolders."
    )

    search_location = tk.StringVar(value=HOME_DIR)
    location_label = make_path_label(page)

    def load_folder_contents(path):
        results.delete(0, tk.END)
        result_paths.clear()

        try:
            for name in os.listdir(path):
                results.insert(tk.END, name)
                result_paths.append(os.path.join(path, name))

            status.config(text=f"{results.size()} item(s) found.", fg=MUTED)

        except OSError as error:
            show_error(error)

    def choose_location():
        path = filedialog.askdirectory(
            title="Choose where to search",
            initialdir=HOME_DIR
        )
        if path:
            search_location.set(path)
            location_label.config(text=path)
            load_folder_contents(path)

    make_button(page, "Choose Directory", choose_location)

    # Entry with placeholder
    entry = make_entry(page)
    entry.insert(0, PLACEHOLDER)
    entry.config(fg=MUTED)

    def clear_placeholder(event=None):
        if entry.get() == PLACEHOLDER:
            entry.delete(0, tk.END)
            entry.config(fg=TEXT)

    def restore_placeholder(event=None):
        if not entry.get().strip():
            entry.delete(0, tk.END)
            entry.insert(0, PLACEHOLDER)
            entry.config(fg=MUTED)

    entry.bind("<FocusIn>", clear_placeholder)
    entry.bind("<FocusOut>", restore_placeholder)

    def search_files(event=None):
        path = search_location.get()
        filename = entry.get().strip()

        if not path:
            status.config(text="Choose a directory first.", fg=RED)
            return

        if not filename or filename == PLACEHOLDER:
            load_folder_contents(path)
            return

        results.delete(0, tk.END)
        result_paths.clear()

        try:
            for full_path in search_file(path, filename):
                results.insert(tk.END, os.path.basename(full_path))
                result_paths.append(full_path)

            count = len(result_paths)

            if count:
                status.config(text=f"{count} matching item(s) found.", fg=MUTED)
            else:
                results.insert(tk.END, "No matching files or folders found.")
                status.config(text="0 items found.", fg=MUTED)

        except OSError as error:
            show_error(error)

    make_button(page, "Search Files", search_files)
    status = make_status(page)
    entry.bind("<Return>", search_files)

    results = make_listbox(page, 10)
    results.pack(fill="both", expand=True, padx=28, pady=(0, 20))

    def open_result(event=None):
        selection = results.curselection()
        if not selection:
            return

        index = selection[0]
        if index >= len(result_paths):
            return

        try:
            subprocess.Popen(["open", result_paths[index]])  # macOS
        except OSError as error:
            show_error(error)

    results.bind("<Double-Button-1>", open_result)