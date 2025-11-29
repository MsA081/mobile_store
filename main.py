# فایل main.py
# این فایل نقطه شروع برنامه است و پنجره اصلی را می‌سازد

import tkinter as tk
from buttons import create_buttons   # ایمپورت تابع ساخت دکمه‌ها

def make_main_page(screen):
    """
    این تابع دکمه‌ها را روی صفحه اصلی قرار می‌دهد
    """
    return create_buttons(screen)

if __name__ == "__main__":
    # ساخت پنجره اصلی
    master_screen = tk.Tk()
    master_screen.geometry("1000x1200")
    master_screen.title("Phone Store")
    master_screen.configure(bg="black")

    # اضافه کردن دکمه‌ها
    make_main_page(master_screen)

    # اجرای برنامه
    master_screen.mainloop()
