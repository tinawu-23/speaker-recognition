from pydub import AudioSegment

audio = AudioSegment.from_wav("../gendervary/tina5s.wav")
length = audio.duration_seconds
half = 2 * 1000
wav1 = audio[:half]
wav1.export('./2s/user1-key.wav', format="wav")


audio = AudioSegment.from_wav("../gendervary/tina5s--2.wav")
length = audio.duration_seconds
half = 2 * 1000
wav1 = audio[:half]
wav1.export('./2s/user1.wav', format="wav")


audio = AudioSegment.from_wav("../gendervary/kat5s.wav")
length = audio.duration_seconds
half = 2 * 1000
wav1 = audio[:half]
wav1.export('./2s/user2.wav', format="wav")

audio = AudioSegment.from_wav("../gendervary/luke5s.wav")
length = audio.duration_seconds
half = 2 * 1000
wav1 = audio[:half]
wav1.export('./2s/user3.wav', format="wav")

## ==================================================##

audio = AudioSegment.from_wav("../gendervary/tina5s.wav")
length = audio.duration_seconds
half = 5 * 1000
wav1 = audio[:half]
wav1.export('./5s/user1-key.wav', format="wav")


audio = AudioSegment.from_wav("../gendervary/tina5s--2.wav")
length = audio.duration_seconds
half = 5* 1000
wav1 = audio[:half]
wav1.export('./5s/user1.wav', format="wav")


audio = AudioSegment.from_wav("../gendervary/kat5s.wav")
length = audio.duration_seconds
half = 5 * 1000
wav1 = audio[:half]
wav1.export('./5s/user2.wav', format="wav")

audio = AudioSegment.from_wav("../gendervary/luke5s.wav")
length = audio.duration_seconds
half = 5 * 1000
wav1 = audio[:half]
wav1.export('./5s/user3.wav', format="wav")

## ==================================================##

audio = AudioSegment.from_wav("../gendervary/tina5s.wav")
wav1 = audio+audio
wav1.export('./10s/user1-key.wav', format="wav")


audio = AudioSegment.from_wav("../gendervary/tina5s--2.wav")
wav1 = audio+audio
wav1.export('./10s/user1.wav', format="wav")


audio = AudioSegment.from_wav("../gendervary/kat5s.wav")
wav1 = audio+audio
wav1.export('./10s/user2.wav', format="wav")

audio = AudioSegment.from_wav("../gendervary/luke5s.wav")
wav1 = audio+audio
wav1.export('./10s/user2.wav', format="wav")