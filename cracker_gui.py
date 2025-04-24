import hashlib
import tkinter as tk
from tkinter import filedialog, messagebox
import os

# Supported hash types
HASH_TYPES = {
    32: 'md5',
    40: 'sha1',
    64: 'sha256',
    128: 'sha512'
}

# Function to detect hash type by length
def detect_hash_type(hash_string):
    return HASH_TYPES.get(len(hash_string))

# Cracking function
def crack_hash(hash_to_crack, hash_type, wordlist_path):
    hash_func = getattr(hashlib, hash_type, None)
    if not hash_func:
        return "Unsupported hash type"

    if not os.path.isfile(wordlist_path):
        return "Wordlist not found"

    try:
        with open(wordlist_path, "r", encoding="utf-8", errors="ignore") as f:
            for word in f:
                word = word.strip()
                if hash_func(word.encode()).hexdigest() == hash_to_crack:
                    return f"Password found: {word}"
        return "Password not found."
    except Exception as e:
        return f"Error: {str(e)}"

# GUI App
class HashCrackerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("🔐 Hash Cracker GUI")
        self.root.geometry("500x300")

        # Widgets
        tk.Label(root, text="Enter hash:").pack()
        self.hash_entry = tk.Entry(root, width=60)
        self.hash_entry.pack(pady=5)

        tk.Label(root, text="Select hash type (optional):").pack()
        self.hash_type_var = tk.StringVar()
        self.hash_type_entry = tk.Entry(root, textvariable=self.hash_type_var)
        self.hash_type_entry.pack(pady=5)

        tk.Button(root, text="Choose Wordlist", command=self.load_wordlist).pack(pady=5)
        self.wordlist_path = tk.StringVar()
        tk.Label(root, textvariable=self.wordlist_path, fg="blue").pack()

        tk.Button(root, text="Crack Hash", command=self.run_cracker).pack(pady=10)
        self.result_label = tk.Label(root, text="", font=("Helvetica", 12))
        self.result_label.pack(pady=10)

    def load_wordlist(self):
        path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
        if path:
            self.wordlist_path.set(path)

    def run_cracker(self):
        hash_value = self.hash_entry.get().strip()
        hash_type = self.hash_type_var.get().strip().lower()

        if not hash_type:
            hash_type = detect_hash_type(hash_value)
            if not hash_type:
                messagebox.showerror("Error", "Could not detect hash type. Please enter it manually.")
                return

        wordlist = self.wordlist_path.get()
        if not hash_value or not wordlist:
            messagebox.showwarning("Missing Info", "Please provide hash and wordlist.")
            return

        result = crack_hash(hash_value, hash_type, wordlist)
        self.result_label.config(text=result)

# Run the app
if __name__ == "__main__":
    root = tk.Tk()
    app = HashCrackerApp(root)
    root.mainloop()
