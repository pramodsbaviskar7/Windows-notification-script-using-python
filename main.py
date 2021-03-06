import time
from plyer import notification

if __name__ == "__main__":
    while True:
        notification.notify(
            title="Notification title",
            message="notification message here",
            app_icon="C:\Users\pramo\PycharmProjects\\notification\\appicon.ico",
            timeout=10


        )
        time.sleep(6)
