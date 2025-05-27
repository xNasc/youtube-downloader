import yt_dlp

url = input("Link do video(URL): ")

ydl_opts = {}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])

print("Vídeo baixado com sucesso!")