from pytubefix import YouTube
from pytubefix import Channel
from pytubefix import Playlist
from pytubefix.cli import on_progress
import os

### Download a video with highest resolution
def DownloadAsMP4(url, path):
    try:
        yt = YouTube(url, on_progress_callback = on_progress)
        print(yt.title)
        yt.streams.get_highest_resolution().download(path)
    except Exception as e:
        print(e)
        
    
### Download a video as .mp3
def DownloadAsMP3(url, path):
    try:
        yt = YouTube(url, on_progress_callback = on_progress)
        print(yt.title)
        ys = yt.streams.get_audio_only()
        ys.download(path, mp3=True)
    except Exception as e:
        print(e)
    
### Download a whole playlist
def DownloadPlaylist(url, path, filetype):
    try:
        pl = Playlist(url)
        title = pl.title
        if not os.path.exists(title):
            os.mkdir(title)
        path = os.path.join(path, title)
        print(str(len(pl.videos)) + ' video(s) in the playlist')
        for video in pl.videos:
            print(video.title)
            if filetype == 1:
                ys = video.streams.get_audio_only()
                ys.download(path, mp3=True)
            if filetype == 2:
                video.streams.get_highest_resolution().download(path)
    except Exception as e:
        print(e)
            
    
### Download all video from a channel
def DownloadAllVideo(url, path, filetype):
    try:
        c = Channel(url)
        print(f'Downloading videos from channel: {c.channel_name}')
        print(str(len(c.videos)) + ' video(s) in the channel')
        for video in c.videos:
            print(video.title)
            if filetype == 1:
                ys = video.streams.get_audio_only()
                ys.download(path, mp3=True)
            if filetype == 2:
                video.streams.get_highest_resolution().download(path)
    except Exception as e:
        print(e)
        
def show():
    print('Here is a downloader supporting following four functions:')
    print('1. Download a video with highest resolution')
    print('2. Download a video as a .mp3 file')
    print('3. Download the whole playlist')
    print('4. Download all video from a channel')
    ins = int(input('Enter 1~4 to do what you want: '))
    return ins
    
instruction = show()
url = ''
### Remember to change it if you want to download the video in other folders
path = os.path.dirname(__file__)

if instruction == 1:
    url = input('Enter the url of the video:\n')
    DownloadAsMP4(url, path)
elif instruction == 2:
    url = input('Enter the url of the video:\n')
    DownloadAsMP3(url, path)
elif instruction == 3:
    url = input('Enter the url of the playlist:\n')
    filetype = 0
    filetype = int(input('Download as mp3(enter 1) or mp4(enter 2)?'))
    if filetype != 1 or filetype != 2:
        print('invalid input')
    DownloadPlaylist(url, path, filetype)
elif instruction == 4:
    url = input('Enter the url of the channel\'s homepage:\n')
    filetype = 0
    filetype = int(input('Download as mp3(enter 1) or mp4(enter 2)?'))
    if filetype != 1 or filetype != 2:
        print('invalid input')
    DownloadAllVideo(url, path, filetype)


    