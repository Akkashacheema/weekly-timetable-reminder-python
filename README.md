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
<img width="1920" height="1080" alt="output" src="https://github.com/user-attachments/assets/a23a5f35-b12d-4d07-be90-af641ae08a50" />

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
⚙️ Installation & Setup
Step 1: Clone the Repository
git clone <your-github-repo-url>
cd weekly-timetable-reminder

Step 2: Create Virtual Environment (Recommended)
python -m venv .venv


Activate the environment:

Windows PowerShell

.venv\Scripts\Activate.ps1


Windows CMD

.venv\Scripts\activate

Step 3: Install Dependencies
pip install -r requirements.txt

Step 4: Run the Application
python src/app.py

🗂️ Data Storage

The application automatically creates and manages the following files:

weekly_schedule.json – stores weekly timetable entries

reminders.json – stores reminder messages and times

These files ensure that user data persists between sessions.

⚠️ Notes & Limitations

Reminder notifications work only while the application is running

Time format must be 24-hour (HH:MM)

Windows notifications require a Windows OS

📦 Optional: Build Executable (Windows)

To convert the application into a standalone .exe file:

pip install pyinstaller
pyinstaller --onefile --windowed src/app.py


The executable will be generated in the dist/ folder.

📄 License

This project is licensed under the MIT License.
You are free to use, modify, and distribute this project with proper attribution.

🙏 Acknowledgements

Python Tkinter Documentation

win10toast (Windows Notifications)

pyttsx3 (Text-to-Speech Engine)

👩‍💻 Author

Akkasha Latif
PhD Researcher in Artificial Intelligence

⭐ If you find this project useful, consider giving it a star on GitHub!



