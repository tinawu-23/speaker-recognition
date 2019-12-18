from pydub import AudioSegment

audio = AudioSegment.from_wav("../static/files/user1.wav")
length = audio.duration_seconds
half = (length//2) * 1000
wav1 = audio[:half]
wav1.export('./2s/user1.wav', format="wav")

audio = AudioSegment.from_wav("../static/files/user2.wav")
length = audio.duration_seconds
half = (length//2) * 1000
wav1 = audio[:half]
wav1.export('./2s/user2.wav', format="wav")

audio = AudioSegment.from_wav("../static/files/user3.wav")
length = audio.duration_seconds
half = (length//2) * 1000
wav1 = audio[:half]
wav1.export('./2s/user3.wav', format="wav")