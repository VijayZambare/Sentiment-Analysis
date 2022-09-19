from pydub import AudioSegment
import speech_recognition as sr


def convert_to_wav(music):


  """Takes an audio file of non .wav format and converts to .wav"""
  # Import audio file
  audio = AudioSegment.from_file(music.mp3)


  # Create new filename
  music1 = music.mp3.split(".")[0] + ".wav"


  # Export file as .wav
  audio.export(music1, format='wav')
  print(f"Converting {music.mp3} to {music1}")