# 🔐 Pro Hash Cracker GUI

A beginner-friendly hash cracking tool built with Python and Tkinter. Supports multiple hash types and allows you to load your own wordlist to crack the given hash.

## 💡 Features
- GUI built with Tkinter
- Supports MD5, SHA1, SHA256, SHA512
- Auto-detects hash type based on length
- Custom wordlist support
- Easy to use, beginner-friendly interface

## 🚀 How to Use

1. Open terminal and run:
    ```bash
    python cracker_gui.py
    ```

2. In the GUI:
    - Paste the hash
    - Select or auto-detect the hash type
    - Choose a wordlist (sample `wordlist.txt` included)
    - Click **Crack Hash**

## 📂 Files
- `cracker_gui.py` — Main GUI application
- `wordlist.txt` — Sample wordlist file
- `README.md` — Project documentation

## 🧪 Example Hashes
- `5f4dcc3b5aa765d61d8327deb882cf99` → `password` (MD5)
- `5baa61e4c9b93f3f0682250b6cf8331b7ee68fd8` → `password` (SHA1)

## ⚠️ Disclaimer
This tool is for **educational purposes only**. Do not use it for unauthorized or illegal activity.
