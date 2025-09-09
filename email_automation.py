import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


class EmailClient:
    def __init__(self, smtp_server, port, sender_email, password):
        self.smtp_server = smtp_server
        self.port = port
        self.sender_email = sender_email
        self.password = password
        self.server = None

    def connect(self):
        """Connect to SMTP server and login"""
        try:
            self.server = smtplib.SMTP(self.smtp_server, self.port)
            self.server.starttls()
            self.server.login(self.sender_email, self.password)
            print("✅ Connected to email server.")
        except Exception as e:
            print(f"❌ Connection failed: {e}")

    def disconnect(self):
        """Close SMTP connection"""
        if self.server:
            self.server.quit()
            print("🔌 Disconnected from email server.")

    def send_email(self, recipient, subject, body):
        """Send single email"""
        if not self.server:
            print("⚠️ Not connected. Call connect() first.")
            return

        msg = MIMEMultipart()
        msg["From"] = self.sender_email
        msg["To"] = recipient
        msg["Subject"] = subject
        msg.attach(MIMEText(body, "plain"))

        try:
            self.server.send_message(msg)
            print(f"📩 Email sent to {recipient}")
        except Exception as e:
            print(f"❌ Failed to send email: {e}")


class EmailMessage:
    def __init__(self, sender, recipient, subject, body):
        self.sender = sender
        self.recipient = recipient
        self.subject = subject
        self.body = body

    def format_message(self):
        """Return formatted email object (MIMEMultipart)"""
        msg = MIMEMultipart()
        msg["From"] = self.sender
        msg["To"] = self.recipient
        msg["Subject"] = self.subject
        msg.attach(MIMEText(self.body, "plain"))
        return msg


class EmailManager:
    def __init__(self, client):
        self.client = client
        self.messages = []

    def add_message(self, message: EmailMessage):
        """Add email message to queue"""
        self.messages.append(message)

    def send_all(self):
        """Send all queued emails"""
        if not self.client.server:
            print("⚠️ Not connected. Call connect() first.")
            return

        for msg in self.messages:
            try:
                self.client.server.send_message(msg.format_message())
                print(f"📩 Sent to {msg.recipient}")
            except Exception as e:
                print(f"❌ Failed to send {msg.recipient}: {e}")


# ---------------- Sample Run ----------------
if __name__ == "__main__":
    # ⚠️ Note: Replace with your real Gmail + App Password
    client = EmailClient(
        smtp_server="smtp.gmail.com",
        port=587,
        sender_email="your_email@gmail.com",
        password="your_app_password"
    )

    client.connect()

    # Single email test
    client.send_email("receiver@gmail.com", "Test Email", "Hello, this is a test.")

    # Multiple emails with EmailManager
    manager = EmailManager(client)
    manager.add_message(EmailMessage("your_email@gmail.com", "user1@gmail.com", "Hi User1", "Message for User1"))
    manager.add_message(EmailMessage("your_email@gmail.com", "user2@gmail.com", "Hi User2", "Message for User2"))
    manager.send_all()

    client.disconnect()
