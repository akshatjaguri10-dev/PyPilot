import subprocess

from ui import (
    GREEN, RED,
    heading, make_button, make_entry, make_status, show_error
)

# ---------- DATA ----------
apps = {
    "chrome": "Google Chrome",
    "safari": "Safari",
    "whatsapp": "WhatsApp",
    "calculator": "Calculator",
    "notes": "Notes",
    "music": "Music",
    "finder": "Finder",
    "calendar": "Calendar",
    "mail": "Mail",
    "terminal": "Terminal",
    "pycharm": "PyCharm",
}


# ---------- LOGIC ----------
def open_apps(command):
    name = command.strip().lower()

    # Accept both "chrome" and "open chrome"
    if name.startswith("open "):
        name = name[5:].strip()

    if not name:
        return False, "Type an app name, for example: chrome"

    if name not in apps:
        return False, f"App not found: {name}"

    try:
        subprocess.Popen(["open", "-a", apps[name]])  # macOS
        return True, f"Opening {apps[name]}..."
    except OSError:
        return False, "Could not launch the application."


# ---------- UI ----------
def build(page):
    heading(
        page,
        "Open an application",
        "Type an application name, such as chrome, safari or notes."
    )

    app_entry = make_entry(page)

    def run_command(event=None):
        success, message = open_apps(app_entry.get())

        if success:
            app_status.config(text=message, fg=GREEN)
        else:
            show_error(message)
            app_status.config(text=message, fg=RED)

    make_button(page, "Open App", run_command)
    app_status = make_status(page)
    app_entry.bind("<Return>", run_command)