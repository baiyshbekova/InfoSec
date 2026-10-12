import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


smtp_server = "smtp.gmail.com"
smtp_port = 587

sender_email = os.environ.get("LAB_SENDER_EMAIL")
sender_password = os.environ.get("LAB_SENDER_APP_PASSWORD")
receiver_email = os.environ.get("LAB_RECEIVER_EMAIL")


subject = "Payment Verification Required"

body = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Payment Verification</title>
</head>

<body style="font-family: Arial, sans-serif; background-color: #f5f5f5; padding: 30px;">

    <div style="
        max-width: 600px;
        margin: auto;
        background-color: white;
        padding: 30px;
        border-radius: 10px;
    ">

        <h2>Payment Verification</h2>

        <p>
            You have a new payment notification.
        </p>

        <p>
            Please follow the link below to continue:
        </p>

        <p>
            <a href="http://127.0.0.1:8080/index.html">
                Continue to payment verification
            </a>
        </p>

        <p style="color: #777;">
            If you did not request this notification,
            you can ignore this message.
        </p>

    </div>

</body>
</html>
"""


if not sender_email or not sender_password or not receiver_email:
    raise SystemExit(
        "Email settings are missing. "
        "Set LAB_SENDER_EMAIL, LAB_SENDER_APP_PASSWORD "
        "and LAB_RECEIVER_EMAIL first."
    )


message = MIMEMultipart()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = subject

message.attach(MIMEText(body, "html"))

try:
    print("Connecting to Gmail...")

    with smtplib.SMTP(smtp_server, smtp_port, timeout=30) as server:
        print("Connection established.")

        server.starttls()
        print("TLS started.")

        server.login(sender_email, sender_password)
        print("Authentication successful.")

        server.send_message(message)
        print("Email sent successfully!")

except Exception as error:
    print(f"Error type: {type(error).__name__}")
    print(f"Error details: {error}")
