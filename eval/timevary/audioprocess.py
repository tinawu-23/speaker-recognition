from pydub import AudioSegment

audio = AudioSegment.from_wav("./5s/vaishali5s.wav")
length = audio.duration_seconds
half = (length//2) * 1000
wav1 = audio[:half]
wav1.export('./2s/vaishali2s.wav', format="wav")

audio = AudioSegment.from_wav("./5s/kat5s.wav")
length = audio.duration_seconds
half = (length//2) * 1000
wav1 = audio[:half]
wav1.export('./2s/kat2s.wav', format="wav")

audio = AudioSegment.from_wav("./5s/lisa5s.wav")
length = audio.duration_seconds
half = (length//2) * 1000
wav1 = audio[:half]
wav1.export('./2s/lisa2s.wav', format="wav")
