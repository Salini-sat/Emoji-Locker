# 😃 Emoji Expression Locker

A facial expression–based authentication system where users log in using emoji-like expressions via their webcam! Built with Python (Flask, OpenCV, MediaPipe) and a simple web interface.

---

## 🚀 Features

- 🔒 Facial expression-based **user registration and authentication**
- 🎭 Detects emoji-like expressions using webcam
- 🌐 Flask backend with HTML + JavaScript frontend
- 💾 Stores user expression "passwords" locally in JSON
- 🧠 Uses MediaPipe for real-time facial expression detection

---

## 📁 Project Structure

Emoji-Expression-Locker/
├── main.py # Flask server and routes
├── register_user.py # Registers new user expressions
├── authenticate_user.py # Authenticates expressions during login
├── expression_detection.py # Detects facial expressions from images
├── static/
│ └── index.html # Frontend UI (camera + buttons)
├── user_data/
│ └── passwords.json # Stores username → expression mappings
├── requirements.txt # Python dependencies
└── README.md # This file

