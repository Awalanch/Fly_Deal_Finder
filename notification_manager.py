import smtplib
import os

MY_EMAIL = os.getenv("MY_EMAIL")
MY_PASSWORD = os.getenv("MY_PASSWORD")

class NotificationManager:

    def __init__(self):
        self.connection = smtplib.SMTP("smtp.gmail.com")
        self.connection.starttls()
        self.connection.login(MY_EMAIL, MY_PASSWORD)

    def send_notification(self, subject, message):
        try:
            self.connection.sendmail(from_addr=MY_EMAIL,
                                      to_addrs=MY_EMAIL,
                                      msg=f"Subject:{subject}\n\n{message}.")

        except Exception as e:
            print(f"I can't send the e-mail: {e}")
        else:
            print("E-mail was sent.")

