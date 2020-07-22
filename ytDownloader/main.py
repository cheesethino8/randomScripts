import youtube_dl
link = input("insert youtube link: ") #ask user for youtube link & save input as $link

ydl_opts = { #set mp3 options to download as mp3
    'postprocessors': [{'key': 'FFmpegExtractAudio','preferredcodec': 'mp3','preferredquality': '192'}]
}
with youtube_dl.YoutubeDL(ydl_opts) as ydl: #use previously stated options
    ydl.download([link]) #main download function