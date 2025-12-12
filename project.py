import tkinter as tk
from tkinter import messagebox
import datetime
import time
import threading
import json
from win10toast import ToastNotifier
import pyttsx3
import os

# ---------- Setup ----------
toaster = ToastNotifier()
engine = pyttsx3.init()
engine.setProperty('rate', 165)
voices = engine.getProperty('voices')
if len(voices) > 1:
    engine.setProperty('voice', voices[1].id)  # female voice if available

schedule_file = "weekly_schedule.json"
reminder_file = "reminders.json"

# ---------- File Handling ----------
def load_data(file):
    if os.path.exists(file):
        with open(file, "r") as f:
            return json.load(f)
    return {}

def save_data(file, data):
    with open(file, "w") as f:
        json.dump(data, f, indent=4)

weekly_schedule = load_data(schedule_file)
reminders = load_data(reminder_file)

# ---------- Functions ----------
def add_schedule():
    day = day_var.get()
    task = task_entry.get().strip()
    if not task:
        messagebox.showwarning("Empty", "Please enter a task.")
        return

    weekly_schedule.setdefault(day, []).append(task)
    save_data(schedule_file, weekly_schedule)
    task_entry.delete(0, tk.END)
    messagebox.showinfo("Added", f"Task added to {day}!")
    refresh_schedule()

def refresh_schedule():
    schedule_list.delete(0, tk.END)
    for day, tasks in weekly_schedule.items():
        schedule_list.insert(tk.END, f"📅 {day}:")
        for t in tasks:
            schedule_list.insert(tk.END, f"   - {t}")

def add_reminder():
    msg = reminder_entry.get().strip()
    time_str = reminder_time_entry.get().strip()
    if not msg or not time_str:
        messagebox.showwarning("Empty", "Please fill both fields.")
        return
    try:
        h, m = map(int, time_str.split(":"))
    except:
        messagebox.showerror("Invalid", "Use 24-hour format (HH:MM)")
        return

    reminders[msg] = time_str
    save_data(reminder_file, reminders)
    reminder_entry.delete(0, tk.END)
    reminder_time_entry.delete(0, tk.END)
    messagebox.showinfo("Added", f"Reminder set for {time_str}")
    refresh_reminders()

def refresh_reminders():
    reminder_list.delete(0, tk.END)
    for msg, t in reminders.items():
        reminder_list.insert(tk.END, f"⏰ {t} - {msg}")

# ---------- Reminder Voice Function ----------
def speak_message(msg):
    try:
        engine.say(f"Reminder: {msg}")
        engine.runAndWait()
    except Exception as e:
        print("Speech error:", e)

# ---------- Background Thread ----------
def check_reminders():
    while True:
        now = datetime.datetime.now().strftime("%H:%M")
        for msg, t in reminders.items():
            if now == t:
                toaster.show_toast("Reminder Alert", msg, duration=10)
                # Voice safely triggered in main thread
                root.after(0, lambda m=msg: speak_message(m))
                time.sleep(60)  # avoid multiple alerts in same minute
        time.sleep(30)

# ---------- GUI ----------
root = tk.Tk()
root.title("Weekly Schedule & Reminder Manager")
root.geometry("700x500")
root.config(bg="#E8F0FE")

# --- Schedule Frame ---
frame1 = tk.LabelFrame(root, text="Weekly Schedule", padx=10, pady=10, bg="#E8F0FE")
frame1.pack(padx=10, pady=10, fill="both", expand=True)

day_var = tk.StringVar(value="Monday")
days = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
tk.OptionMenu(frame1, day_var, *days).grid(row=0, column=0, padx=5)
task_entry = tk.Entry(frame1, width=40)
task_entry.grid(row=0, column=1, padx=5)
tk.Button(frame1, text="Add Task", command=add_schedule, bg="#4CAF50", fg="white").grid(row=0, column=2, padx=5)

schedule_list = tk.Listbox(frame1, width=80, height=10)
schedule_list.grid(row=1, column=0, columnspan=3, pady=10)

# --- Reminder Frame ---
frame2 = tk.LabelFrame(root, text="Reminders", padx=10, pady=10, bg="#E8F0FE")
frame2.pack(padx=10, pady=10, fill="both", expand=True)

tk.Label(frame2, text="Message:", bg="#E8F0FE").grid(row=0, column=0)
reminder_entry = tk.Entry(frame2, width=25)
reminder_entry.grid(row=0, column=1)

tk.Label(frame2, text="Time (HH:MM):", bg="#E8F0FE").grid(row=0, column=2)
reminder_time_entry = tk.Entry(frame2, width=10)
reminder_time_entry.grid(row=0, column=3)

tk.Button(frame2, text="Add Reminder", command=add_reminder, bg="#2196F3", fg="white").grid(row=0, column=4, padx=10)

reminder_list = tk.Listbox(frame2, width=80, height=8)
reminder_list.grid(row=1, column=0, columnspan=5, pady=10)

# ---------- Load Data ----------
refresh_schedule()
refresh_reminders()

# ---------- Thread for checking reminders ----------
thread = threading.Thread(target=check_reminders, daemon=True)
thread.start()

root.mainloop()
