# Automate Bookmarked Websites using Python

A Python-based automation tool that opens frequently used bookmarked websites automatically using either a text file or a browser-exported HTML bookmarks file.

This project focuses on improving daily productivity by automating repetitive browser tasks.

---

## 🚀 Features

- Automatically opens multiple bookmarked websites in the default browser.
- Supports two input formats:
  - Plain text file (`.txt`).
  - Browser-exported bookmarks file (`.html`).
- Removes duplicate URLs before execution.
- Validates URLs to avoid broken or invalid links.
- Displays a summary of total, valid, and invalid links.
- Supports both CLI-based execution and one-click execution for HTML bookmarks.

---

## 🛠 Tech Stack

- **Python**
- **Standard Python Libraries**
- **BeautifulSoup** – HTML bookmark parsing

---

## 📂 Project Structure

```text
Automate-Bookmarked-Websited-using-Python/
│
├── bookmarks/
│   ├── bookmarks.txt
│   └── bookmarks.html
│
├── src/
│   ├── loader.py
│   ├── validator.py
│   └── opener.py
│
├── main.py
├── run_html.py
├── requirements.txt
└── README.md
```

---

## ▶️ Usage

### 1️⃣ Using Text File (CLI Mode)

```bash
python main.py --input-type txt --file bookmarks/bookmarks.txt
```

---

### 2️⃣ Using HTML Bookmarks File (CLI Mode)

```bash
python main.py --input-type html --file bookmarks/bookmarks.html
```

---

### 3️⃣ One-Click Execution for HTML Bookmarks

```bash
python run_html.py
```

This mode directly opens all valid bookmarks from the exported HTML file without requiring CLI arguments.

---

## ⚙️ How It Works

1. Loads URLs from the provided input file.
2. Cleans and removes duplicate entries.
3. Validates URLs to ensure correctness.
4. Opens all valid URLs in the default browser.
5. Displays execution summary in the terminal.

---

## ⚠️ Limitations

- Designed for personal productivity use.
- Does not handle authentication-based or session-dependent websites.
- Browser behavior depends on system default settings.

---

## 🔮 Future Enhancements

- GUI-based interface for non-technical users.
- Support for additional browser bookmark formats.
- Scheduling support for automatic daily execution.
- Logging and execution history tracking.

---

## 👤 Author & Ownership

This project is designed, developed, and maintained by **Shubham Mahajan**.

- GitHub: https://github.com/ShubhamMahajan880  
- LinkedIn: https://www.linkedin.com/in/shubham-mahajan-2a9a47220/

---

## ⭐ Why This Project Matters

This project demonstrates:
- Practical Python automation skills.
- Clean modular design.
- File parsing and validation logic.
- Real-world productivity improvement use case.

Suitable for showcasing Python automation fundamentals in interviews.
