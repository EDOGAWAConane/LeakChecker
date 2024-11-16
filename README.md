# 🛡️ Password Leak Checker 🛡️
Welcome to the **Password Leak Checker**, a secure and fun way to see if your passwords have been compromised in data breaches! This project started as part of my learning journey at the **Zero To Mastery (ZTM) Academy**, where we had to build a password checker. I decided to expand on it by adding a simple, user-friendly front end using Flask.

---

## 📖 What Is This?

This app allows you to:
- 🔐 **Check your passwords securely**: No data is sent to anyone—everything runs locally on your computer.
- ✨ **Use a cute front-end interface**: Enter your password in a secure, local dialog box.
- ✅ **Get helpful feedback**: See if your password has been compromised and take action if needed.

---

## 🚀 How to Use It

### Prerequisites
- **Python 3.7+** installed on your computer.
- **Git** (optional but recommended for cloning the repository).

### Step 1: Clone the Repository
```bash
git clone https://github.com/EDOGAWAConane/LeakChecker.git
cd LeakChecker.git
```

### Step 2: Create a Virtual Environment
Set up an isolated Python environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### Step 3: Install Dependencies
Install the required Python packages:
```bash
pip install -r requirements.txt
```

### Step 4: Run the App
Start the Flask development server:
```bash
python app.py
```

### Step 5: Open the App in Your Browser
Visit `http://127.0.0.1:5000` in your browser to securely check your passwords!

---

## 💡 Why Is This Secure?

- 🔒 **Everything stays local**: This app runs entirely on your computer.
- 🧠 **Smart hashing**: Your password is hashed using SHA1 locally, and only the first 5 characters of the hash are sent to the Pwned Passwords API. This ensures your full password is never exposed.

---

## 📚 My Learning Journey
This project is part of my learning experience at the Zero To Mastery (ZTM) Academy, where I strengthened my foundational Python knowledge and learned how to build exciting, real-world projects. The original project involved creating a command-line password checker, and I found it so engaging that I decided to expand it by adding a front-end interface. This made it more accessible and fun to use!

If you're looking to enhance your programming skills or explore new areas of development, I highly recommend checking out Zero To Mastery. It’s a fantastic platform to learn and grow! 🚀

---

## 🛠️ Tech Stack
- **Backend**: Python, Flask
- **Frontend**: HTML, CSS
- **API**: Pwned Passwords API (for secure breach checks)

---

## 🤝 Contributions
Want to improve the app? Contributions are welcome! Here’s how you can contribute:
1. Fork this repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -m "Add feature"`).
4. Push to the branch (`git push origin feature-branch`).
5. Open a Pull Request.