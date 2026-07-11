# 🤖 AI Email Assistant

<p align="center">
  <img src="assets/banner.png" alt="AI Email Assistant Banner" width="100%">
</p>

<p align="center">

![Python](https://img.shields.io/badge/Python-3.14-blue?style=for-the-badge&logo=python)
![Gemini](https://img.shields.io/badge/Google-Gemini%20AI-4285F4?style=for-the-badge&logo=google)
![Gmail API](https://img.shields.io/badge/Gmail-API-EA4335?style=for-the-badge&logo=gmail)
![GitHub](https://img.shields.io/badge/GitHub-Version%201.0.0-black?style=for-the-badge&logo=github)

</p>

An intelligent Gmail assistant powered by **Google Gemini AI** that automatically reads unread emails, analyzes their content, prioritizes important messages, generates concise summaries, creates reminders for deadlines, and sends desktop notifications.

---

## 🌟 Overview

Managing emails can be time-consuming, especially when important messages are mixed with promotions and newsletters.

AI Email Assistant automates this process by continuously monitoring your Gmail inbox, understanding email content using Google's Gemini AI, identifying important emails, extracting actionable information, and notifying you only when necessary.

The project is designed with a modular architecture, making it easy to extend with additional AI features in the future.

## ✨ Features

### 📧 Gmail Integration
- Secure Gmail authentication using OAuth 2.0
- Automatically monitors unread emails
- Marks processed emails as read
- Prevents duplicate email processing

### 🤖 AI-Powered Email Analysis
- Summarizes long emails using Google Gemini AI
- Classifies emails into categories (Placement, Security, Finance, Shopping, College, etc.)
- Assigns priority levels (High, Medium, Low)
- Calculates an importance score
- Detects whether an email requires action or a reply
- Extracts deadlines and suggested next actions

### 🔔 Smart Notifications
- Displays Windows desktop notifications
- Notifies only for important emails
- Skips unnecessary promotional emails

### 📅 Reminder Management
- Automatically creates reminders from emails containing deadlines
- Displays pending reminders at startup
- Removes expired reminders automatically
- Prevents duplicate reminders

### 🧠 Memory System
- Keeps track of processed emails
- Prevents the same email from being analyzed multiple times
- Stores reminders persistently using JSON

### 🏗️ Modular Architecture
- Separate modules for Gmail, AI, Memory, Notifications, and Configuration
- Easy to maintain and extend
- Clean project structure following Python best practices

## 🛠️ Tech Stack

| Category | Technologies |
|----------|--------------|
| Programming Language | Python 3 |
| AI Model | Google Gemini 2.5 Flash |
| Email Service | Gmail API |
| Authentication | OAuth 2.0 |
| Notifications | win11toast |
| Configuration | python-dotenv |
| Data Storage | JSON |
| Development Environment | Visual Studio Code |
| Version Control | Git |
| Repository Hosting | GitHub |

## 📂 Project Structure

```text
AI_Email_Assistant/
│
├── ai/
│   ├── ai_helper.py
│   └── prompts.py
│
├── gmail/
│   ├── email_parser.py
│   ├── email_processor.py
│   └── gmail_helper.py
│
├── memory/
│   ├── memory.py
│   ├── reminder.py
│   ├── processed.json
│   ├── reminders.json
│
├── notification/
│   └── notifier.py
│
├── .env
├── .gitignore
├── config.py
├── credentials.json
├── main.py
├── README.md
├── requirements.txt
└── token.json
```

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/Hari567-hub/AI_Email_Assistant.git
cd AI_Email_Assistant
```

### 2️⃣ Create a Virtual Environment

**Windows**

```bash
python -m venv .venv
.venv\Scripts\activate
```

**Linux / macOS**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Configure Environment Variables

Create a `.env` file in the project root.

```env
GEMINI_API_KEY=your_gemini_api_key
```

### 5️⃣ Configure Gmail API

- Create a Google Cloud project.
- Enable the Gmail API.
- Download the OAuth client credentials.
- Rename the downloaded file to:

```
credentials.json
```

Place it in the project root.

### 6️⃣ Run the Application

```bash
python main.py
```

## 🚀 How It Works

1. Authenticate with Gmail using OAuth 2.0.
2. Continuously monitor unread emails.
3. Extract the email body (HTML or plain text).
4. Send the email content to Google Gemini AI.
5. Generate:
   - Summary
   - Category
   - Priority
   - Importance Score
   - Action Items
   - Deadline (if present)
6. Create reminders for emails with deadlines.
7. Display desktop notifications for important emails.
8. Mark processed emails as read.
9. Store processed email IDs to prevent duplicate processing.


## 📸 Screenshots


### Application Startup

![Startup](screenshots/startup.png)

### AI Email Analysis

![Analysis](screenshots/eamil_analysis.png)

### Desktop Notification

![Notification](screenshots/desktop_notification.png)

### Project Structure

![Structure](screenshots/project_structure.png)

## 🔮 Future Improvements

- 📱 Android companion application
- 🌐 Web dashboard for email management
- ☁️ Cloud deployment
- 🤖 AI-generated email replies
- 📅 Google Calendar integration
- 📊 Daily email summary reports
- 🎙️ Voice notifications
- 🌙 Dark mode dashboard
- 📈 Email analytics and insights
- 🌍 Multi-language support

## 🤝 Contributing

Contributions, suggestions, and feedback are welcome.

If you'd like to improve this project:

1. Fork the repository.
2. Create a feature branch.
3. Commit your changes.
4. Open a Pull Request.

## 📄 License

This project is licensed under the MIT License.

## 👨‍💻 Author

**Hari**

Computer Science Engineering Student

GitHub: https://github.com/Hari567-hub

---

⭐ If you found this project interesting, consider giving it a star on GitHub!