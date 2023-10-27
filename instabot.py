from instapy import InstaPy
from instapy import smart_run
import time

# specify the username and password for your Instagram account
username = 'legendofhanumanji'
password = '12122001@siddhu'

# specify the file path to the reel you want to upload
file_path = 'C:\\Users\\Siddhartha Yadav\\Desktop\\ramreel.mp4'

# create a new InstaPy session and set the Instagram username and password
session = InstaPy(username=username, password=password, headless_browser=True)

# log in to Instagram
session.login()

# define a function that uploads the reel and sets it to private
def upload_reel():
    session.upload_reel(file_path, caption='testing', is_sidecar=True)
    time.sleep(5)

# schedule the reel upload to run daily at 7 AM
def job():
    upload_reel()

schedule.every().day.at("07:00").do(job)

# run the script until you stop it
while True:
    schedule.run_pending()
    time.sleep(1)