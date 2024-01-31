import pytube

def get_videos(url,pasta_de_destino):
    playlist = pytube.Playlist(url)
    for item in playlist:
        video = pytube.YouTube(item)
        video.streams.get_audio_only().download(pasta_de_destino)
    print('Videos downloaded successfully!')


get_videos("https://www.youtube.com/playlist?list=PLRPR8uJQx5tHZXO06KtUrdMhbeKiPwDoM","C:/Users/User/Desktop/sideMoney/source/videos")
