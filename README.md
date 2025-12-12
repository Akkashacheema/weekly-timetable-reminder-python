# weekly-timetable-reminder-python
Weekly Timetable &amp; Reminder Manager is a Python-based desktop application built with Tkinter that allows users to manage weekly tasks and set time-based reminders. It uses JSON for persistent storage and provides Windows notifications with optional voice alerts for effective personal time management.
# Weekly Timetable & Reminder Manager

A Python-based desktop application built with **Tkinter** that allows users to manage weekly schedules and set time-based reminders. The application uses **JSON-based persistent storage** and provides **Windows toast notifications** with optional **voice alerts** to support effective personal time management.

---

## 📌 Project Description

**Weekly Timetable & Reminder Manager** is a lightweight and user-friendly desktop scheduling system designed to help users organize their daily activities efficiently. Users can create a structured weekly timetable, add reminders using a 24-hour time format, and receive timely alerts while the application is running.

The system stores all timetable entries and reminders locally using JSON files, ensuring data persistence across sessions. A background thread continuously monitors reminder times and triggers notifications without interrupting the user interface.

This project demonstrates practical implementation of GUI development, file handling, multithreading, and event-driven programming in Python.

---

## ✨ Features

### Weekly Timetable
- Add tasks for any day of the week
- View all scheduled tasks in a single interface
- Persistent storage using JSON

Reminders
- Add reminders with custom messages and time (HH:MM format)
- Windows toast notifications
- Optional text-to-speech voice alerts
- Background reminder checking using threading

---

Tech Stack

- **Python**
- **Tkinter** (GUI)
- **JSON** (Data Storage)
- **Threading** (Background tasks)
- **win10toast** (Windows notifications)
- **pyttsx3** (Offline text-to-speech)

---

 📁 Project Structure

```text
weekly-timetable-reminder/
│
├─ src/
│  └─ app.py
│
├─ data/
│  ├─ weekly_schedule.json
│  └─ reminders.json
│
├─ assets/
│  ├─ poster.jpg
│  └─ screenshot.png
│
├─ docs/
│  └─ project.pptx
│
├─ requirements.txt
├─ .gitignore
├─ LICENSE
└─ README.md
