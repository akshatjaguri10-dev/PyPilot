import tkinter as tk

import app_page
import create_page
import search_page
import delete_page
import list_page
from ui import BG, DARK, SIDEBAR, SIDEBAR_HOVER, flat_button


PAGES = {
    "Open App": app_page,
    "Create Folder": create_page,
    "Search File": search_page,
    "Delete File": delete_page,
    "List Folders": list_page,
}

# WINDOW
window = tk.Tk()
window.title("PyPilot - Desktop Tool")
window.geometry("1000x650")
window.minsize(800, 520)
window.configure(bg=BG)

# HEADER
header = tk.Frame(window, bg=DARK, height=65)
header.pack(fill="x")
header.pack_propagate(False)

tk.Label(header, text="PyPilot", font=("Arial", 23, "bold"),
         bg=DARK, fg="white").pack(side="left", padx=22)
tk.Label(header, text="DESKTOP TOOL", font=("Arial", 10, "bold"),
         bg=DARK, fg="#B6BBC6").pack(side="right", padx=22)

# BODY
body = tk.Frame(window, bg=BG)
body.pack(fill="both", expand=True)

sidebar = tk.Frame(body, bg=SIDEBAR, width=185)
sidebar.pack(side="left", fill="y")
sidebar.pack_propagate(False)

content = tk.Frame(body, bg=BG)
content.pack(side="left", fill="both", expand=True)

# BUILD PAGES
pages = {}
for name, module in PAGES.items():
    page = tk.Frame(content, bg=BG)
    page.place(x=0, y=0, relwidth=1, relheight=1)
    module.build(page)
    pages[name] = page


def show_page(name):
    pages[name].tkraise()


# SIDEBAR NAVIGATION
tk.Label(sidebar, text="WORKSPACE", font=("Arial", 10, "bold"),
         bg=SIDEBAR, fg="#B6BBC6").pack(anchor="w", padx=16, pady=(25, 15))

for name in PAGES:
    flat_button(
        sidebar, name,
        lambda n=name: show_page(n),
        bg=SIDEBAR, hover=SIDEBAR_HOVER,
        fg="white", font=("Arial", 12),
        anchor="w", padx=16, pady=12
    ).pack(fill="x", padx=8, pady=3)

show_page("Open App")
window.mainloop()