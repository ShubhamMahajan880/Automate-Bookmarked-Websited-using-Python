# Automate Bookmarked Websites using Python

A Python-based local automation tool that allows users to open all their bookmarked websites at once using either a text file or a browser-exported HTML bookmarks file.

This tool is designed to be **reusable by anyone** by simply replacing the bookmarks file with their own.

---

## 🎯 What This Tool Solves

Many users open the same set of websites daily (Gmail, GitHub, LinkedIn, dashboards, etc.).  
Opening them one by one is repetitive and time-consuming.

This project automates that process by opening **all bookmarked websites in a single run**.

---

## 🚀 Key Features

- Opens multiple bookmarked websites in the default browser automatically.
- Supports two input formats:
  - Plain text file (`.txt`)
  - Browser-exported bookmarks file (`.html`)
- Removes duplicate URLs.
- Validates URLs before opening.
- Displays a summary of total, valid, and invalid links.
- Designed as a **portable local tool** — no hosting required.

---

## 🛠 Tech Stack

- **Python**
- **Standard Python Libraries**
- **BeautifulSoup** – for parsing HTML bookmark files

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

## 👥 How Anyone Can Use This Tool (IMPORTANT)

This project is **not tied to one machine or one user**.

Any user can use it by following these steps:

### Step 1: Clone the Repository
```bash
git clone https://github.com/ShubhamMahajan880/Automate-Bookmarked-Websited-using-Python.git
cd Automate-Bookmarked-Websited-using-Python
```

---

### Step 2: Export Your Own Bookmarks

From your browser:
- Export bookmarks as an **HTML file**.
- Rename it to `bookmarks.html`.

Place it inside:
```
bookmarks/bookmarks.html
```

You can replace the existing file — **no code changes required**.

---

### Step 3: Install Dependencies
```bash
python -m pip install -r requirements.txt
```

---

## ▶️ Usage Options

### 1️⃣ One-Click Execution (Recommended)

```bash
python run_html.py
```

This will:
- Read `bookmarks/bookmarks.html`
- Validate all URLs
- Open all valid websites in the default browser

---

### 2️⃣ CLI Execution (Advanced)

Using text file:
```bash
python main.py --input-type txt --file bookmarks/bookmarks.txt
```

Using HTML file:
```bash
python main.py --input-type html --file bookmarks/bookmarks.html
```

---

## ⚙️ How It Works (Internally)

1. Loads URLs from the provided bookmarks file.
2. Cleans and removes duplicate entries.
3. Validates URLs to avoid broken links.
4. Opens all valid URLs in the default browser.
5. Prints a summary of execution results.

---

## ⚠️ Design Note (Why This Is a Local Tool)

This tool is intentionally designed for **local execution** because:
- Browsers run on the user’s machine.
- System-level automation cannot be hosted remotely.
- This ensures user privacy and full control.

This is expected behavior for automation tools and CLI utilities.

---

## 🔮 Possible Enhancements

- GUI interface for non-technical users.
- Scheduled execution (daily startup automation).
- Support for additional bookmark formats.
- Logging and execution history.

---

## 👤 Author & Ownership

This project is designed, developed, and maintained by **Shubham Mahajan**.

- GitHub: https://github.com/ShubhamMahajan880  
- LinkedIn: https://www.linkedin.com/in/shubham-mahajan-2a9a47220/

---

## ⭐ Why This Project Matters

This project demonstrates:
- Practical Python automation.
- File parsing and validation.
- Modular and reusable design.
- Real-world productivity improvement.

It is intended as a **local automation utility**, not a hosted web application.
