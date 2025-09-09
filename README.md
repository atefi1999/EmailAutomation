# 📧 Email Automation

### A Python project for automating sending emails using **SMTP**. It supports:

- Sending single emails  
- Queuing multiple emails and sending them in bulk  
- Secure connection using TLS  

---

## 🚀 Features
- Connect to SMTP server (tested with Gmail)
- Send individual emails
- Manage and send multiple emails via queue
- Disconnect safely from the server

---

## 🛠️ Installation
1. Clone the repository:
   
   ```bash
   git clone https://github.com/yourusername/EmailAutomation.git
   cd EmailAutomation
   ```


2. Install dependencies (Python standard library, no extra install needed):

- smtplib
- email

---

## ▶️ Usage
1. Single Email

```backtick
from email_client import EmailClient

client = EmailClient(
    smtp_server="smtp.gmail.com",
    port=587,
    sender_email="your_email@gmail.com",
    password="your_app_password"  # Use App Password for Gmail
)

client.connect()
client.send_email("receiver@gmail.com", "Test Subject", "Hello, this is a test.")
client.disconnect()
```

2. Multiple Emails (with Queue)

```backtick
from email_client import EmailClient, EmailMessage, EmailManager

client = EmailClient(
    smtp_server="smtp.gmail.com",
    port=587,
    sender_email="your_email@gmail.com",
    password="your_app_password"
)
client.connect()

manager = EmailManager(client)
manager.add_message(EmailMessage("your_email@gmail.com", "user1@gmail.com", "Hi User1", "Message for User1"))
manager.add_message(EmailMessage("your_email@gmail.com", "user2@gmail.com", "Hi User2", "Message for User2"))
manager.send_all()

client.disconnect()
```
---

## 📂 Project Structure

```markdown
.
├── email_client.py      # Main program
├── README.md            # Project documentation
```
---

## ✅ Example Output

```backtick
✅ Connected to email server.
📩 Email sent to receiver@gmail.com
📩 Sent to user1@gmail.com
📩 Sent to user2@gmail.com
🔌 Disconnected from email server.

```

---

## ⚠️ Notes

- If using Gmail, you must enable App Passwords (not your main password).
- Make sure "Less secure app access" is handled properly in your email provider.
- Always keep your credentials safe (don’t hardcode them in public repos).

