#Converting MP3 file into WAV file 
from pydub import AudioSegment
sound = AudioSegment.from_mp3("C:/Users/ANUPAMA/Desktop/audio_atributes/Stairway_to_heaven.mp3")
sound.export("C:/Users/ANUPAMA/Desktop/audio_atributes/Stairway_to_heaven.wav", format="wav")

#Converting mutlichannel into monochannel 

from pydub import AudioSegment
sound = AudioSegment.from_wav("C:/Users/ANUPAMA/Desktop/audio_atributes/music.mp3")
sound = sound.set_channels(1)
sound.export("C:/Users/ANUPAMA/Desktop/audio_atributes/classical.wav", format="wav")