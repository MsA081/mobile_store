# فایل buttons.py
# این فایل مسئول ساخت دکمه‌هاست

import tkinter as tk

BUTTON_CONFIG = {
    "bg": "#23F02F",
    "fg": "white",
    "font": ("Arial", 20),
}

BUTTONS_TEXT = [
    "List products and searchings ...",
    "List your sells",
    "Info user account",
    "Log out"
]

def create_buttons(root):
    """
    این تابع یک فریم در سمت راست پنجره می‌سازد و دکمه‌ها را داخل آن قرار می‌دهد.
    خروجی: لیست دکمه‌ها
    """
    # ابتدا پنجره را آپدیت می‌کنیم تا اندازه واقعی داشته باشد
    root.update_idletasks()
    width = root.winfo_width()
    frame_width = int(width * 0.4)   # حدود 40 درصد عرض پنجره

    # ساخت فریم در سمت راست
    frame = tk.Frame(root, bg="black", width=frame_width)
    frame.pack(side="right", fill="y")

    # جلوگیری از تغییر اندازه فریم
    frame.grid_propagate(False)
    frame.columnconfigure(0, weight=1)

    buttons = []
    for i, text in enumerate(BUTTONS_TEXT):
        btn = tk.Button(frame, text=text, **BUTTON_CONFIG)
        # دکمه‌ها کل عرض ستون را پر می‌کنند
        btn.grid(row=i, column=0, sticky="ew", padx=10, pady=10)
        buttons.append(btn)

    return buttons
