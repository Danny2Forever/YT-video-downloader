import pytube
from pytube import YouTube
url = input("Enter url : ")
yt = YouTube(url)
print("***************************************************")
print(f"Title : {yt.title}")
print(f"Views : {yt.views}")
print(f"Channal : {yt.author}")
print("***************************************************")

path = input("Enter path : ")

pytube.YouTube(url).streams.get_highest_resolution().download(path)