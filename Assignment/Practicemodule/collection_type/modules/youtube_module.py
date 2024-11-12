from pytubefix import YouTube

url="https://www.youtube.com/watch?v=u7fbqWxeq4I"
YouTube(url).streams.filter().download()
