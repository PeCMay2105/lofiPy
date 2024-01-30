from moviepy.editor import *
from moviepy import *


clipe1 = ImageClip("./darkAcademia.jpg", duration=500)
audio1 = AudioFileClip("./song1.mp3")
audio2 = AudioFileClip("./song2.mp3")
audio3 = AudioFileClip("./song3.mp3")
audio4 = AudioFileClip("./song4.mp3")

def makeClips(imagem,audioList):
    clipe = ImageClip(imagem, duration=500)
    audios = [AudioFileClip(audio) for audio in audioList]
    audios = [audio.audio_loop(duration=900) for audio in audios]
    final_clips = [clipe.set_audio(audio) for audio in audios]
    trueFinal = concatenate_videoclips(final_clips)
    trueFinal = trueFinal.resize(width=1920, height=1080)
    trueFinal = trueFinal.loop(duration=3600)
    return trueFinal


def writing(final_clip,title):
    final_clip.write_videofile(title+".mp4", fps=1, codec="libx264", audio_codec="aac", temp_audiofile="temp-audio.m4a", remove_temp=True, audio_bitrate="3000k")

#final_clips = [clipe1.set_audio(audio) for audio in audios]
#trueFinal = concatenate_videoclips(final_clips)
#trueFinal = trueFinal.resize(width=1920, height=1080)
#trueFinal = trueFinal.loop(duration=3600)

#trueFinal.write_videofile("darkAcademia.mp4", fps=1, codec="libx264", audio_codec="aac", temp_audiofile="temp-audio.m4a", remove_temp=True, audio_bitrate="3000k")

