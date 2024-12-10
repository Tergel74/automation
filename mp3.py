# from pytube import YouTube
from sys import argv
import yt_dlp

link = argv[1]

# yt = YouTube(link)
# audio = yt.streams.get_audio_only()
# # filter(only_audio=True).first()

print("Destination or leave blank for default")
out_path = input(">> ") or "/Users/tergel/Downloads"

# audio.download(output_path=out_path, filename=f"{audio.title}.mp3")

# print(yt.title + "has been successfully downloaded!")

ydl_opts = {
    'format': 'bestaudio/best',
    'outtmpl': f"{out_path}/%(title)s.%(ext)s",
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([link])
