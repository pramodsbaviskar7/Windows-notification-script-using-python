import time
#pip install plyer
from plyer import notification

if __name__ == "__main__":
    while True:
        notification.notify(
            title="Notification title",
            message="notification message here",
            #you can add your own logo to the alert notification by providing location of the folder 
            app_icon="C:\Users\pramo\PycharmProjects\\notification\\appicon.ico",
            #time of notification
            timeout=10


        )
        #time of sleep i.e. upto which time you want the notfication to pop next
        time.sleep(6)
