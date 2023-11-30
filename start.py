import schedule
import time
import subprocess

def job():
    subprocess.call(["python", "your_timer_script.py"])

# 每天的9:00开始专注时钟
schedule.every().day.at("09:00").do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
