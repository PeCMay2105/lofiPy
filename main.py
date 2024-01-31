from moviepy.editor import *
from moviepy import *
import os


clipe1 = ImageClip("./darkAcademia.jpg", duration=500)
audio1 = AudioFileClip("./song1.mp3")
audio2 = AudioFileClip("./song2.mp3")
audio3 = AudioFileClip("./song3.mp3")
audio4 = AudioFileClip("./song4.mp3")

lista_audios = [os.path.join("C:/Users/User/Desktop/sideMoney/source/videos",video) for video in os.listdir("C:/Users/User/Desktop/sideMoney/source/videos") if os.path.isfile("C:/Users/User/Desktop/sideMoney/source/videos",video)] 
lista1 = [audio for audio in lista_audios if lista_audios.index(audio) <= 25 ]
lista2 = [audio for audio in lista_audios if lista_audios.index(audio) > 25 and lista_audios.index(audio) <= 50]
lista3 = [audio for audio in lista_audios if lista_audios.index(audio) > 50 and lista_audios.index(audio) <= 75]
lista4 = [audio for audio in lista_audios if lista_audios.index(audio) > 75 and lista_audios.index(audio) <= 100]

def makeClips(imagem,audioList):
    clipe = ImageClip(imagem, duration=500)
    audios = [AudioFileClip(audio) for audio in audioList]
    audios = [audio.audio_loop(duration=900) for audio in audios]
    final_clips = [clipe.set_audio(audio) for audio in audios]
    trueFinal = concatenate_videoclips(final_clips)
    trueFinal = trueFinal.resize(width=1920, height=1080)
    trueFinal = trueFinal.loop(duration=1800)
    return writing(trueFinal,"autoLofi")


def writing(final_clip,title):

    arquivo_destino = os.path.join('C:\Users\User\Desktop\sideMoney\out',title+".mp4")
    final_clip.write_videofile(arquivo_destino, fps=1, codec="libx264", audio_codec="aac", temp_audiofile="temp-audio.m4a", remove_temp=True, audio_bitrate="3000k")


makeClips("./source/images/books.webp",lista1)
print("done")
makeClips("./source/images/imagem.jpg",lista2)
print("done")
makeClips("./source/images/cafe.jpg",lista3)
print("done")
makeClips("./source/images/library.jpg",lista4)
print("done")



#final_clips = [clipe1.set_audio(audio) for audio in audios]
#trueFinal = concatenate_videoclips(final_clips)
#trueFinal = trueFinal.resize(width=1920, height=1080)
#trueFinal = trueFinal.loop(duration=3600)

#trueFinal.write_videofile("darkAcademia.mp4", fps=1, codec="libx264", audio_codec="aac", temp_audiofile="temp-audio.m4a", remove_temp=True, audio_bitrate="3000k")

