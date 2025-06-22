from flask import Flask, send_file, request,redirect
from threading import Timer
import pyperclip
import os
import urllib
import random

files = os.listdir("../")
videos = []
images = []
for file in files:
    if file.endswith(".mp4"):
        videos.append(file)
    elif file.endswith((".jpg", ".png", ".webp")):
        images.append(file)

videos.sort()
print("Videos:")
for video in videos:
    print(f"{videos.index(video) + 1}. {video}")
images.sort
print("Images:")
for image in images:
    print(f"{images.index(image) + 1}. {image}")

app = Flask(__name__)

@app.route("/", methods =["GET"])
def sendVideo():
    return "add /v to play a video and /i to show an image"
    
@app.route("/v/<int:index>", methods = ["GET"])
def videoPlayer(index):
    try:
        return send_file(f"../{videos[int(index) - 1]}", as_attachment = True)
    except:
        return send_file(f"../{videos[0]}", as_attachment = True)
        
@app.route("/v", methods = ["GET"])
def defaultVideo(index):
    return send_file(f"../{videos[0]}", as_attachment = True)
    
@app.route("/i/<int:index>", methods = ["GET"])       
def imageSender(index):
    try:
        return send_file(f"../{images[int(index) - 1]}", as_attachment = True)
    except:
        return send_file(f"../{images[0]}", as_attachment = True)
        
@app.route("/i", methods = ["GET"])
def defaultImage(index):
    return send_file(f"../{images[0]}", as_attachment = True)

# This is stupid but it should work for getting a link that auto copies to clipboard ehe  
response = urllib.request.urlopen("https://www.mit.edu/~ecprice/wordlist.10000")
test = f"{response.read()}"
words = test.split("\\n")   
url = ""

for i in range(3):
    url= url + str((words[random.randint(0,len(words) - 1)]))
# You can change the {url} below to a custom name
pyperclip.copy(f"https://{url}.loca.lt/v/1")
thread = Timer(0, os.system, args=(f"lt --port 5000 --subdomain {url}",))
thread.daemon = True
thread.start()

if __name__ == "__main__":
    app.run(host='0.0.0.0')
