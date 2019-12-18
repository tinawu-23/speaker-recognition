'''
	Preprocess voice 
'''


import numpy as np
import struct
import os
import soundfile as sf
from multiprocessing import Process

def pre_emp(x):
	'''
	Pre-emphasize raw waveform '''
	return np.asarray(x[1:] - 0.97 * x[:-1], dtype=np.float32)

def extract_waveforms(lines, dir_trg):

	f_scp_pe = open(dir_trg + 'test_pe.scp', 'w')
	processed_voices = []
	for i, line in enumerate(lines):
		full_path, file_name = line

		wav ,_= sf.read(full_path, dtype='int16')
		wav = pre_emp(wav)
		voice_list_path = os.path.abspath(dir_trg + 'test_pe.ark')
		f_scp_pe.write('%s %s %d\n'%(full_path, voice_list_path, i))
		processed_voices.append(wav)
	
	np.savez(dir_trg + 'test_pe.ark', *processed_voices)

	f_scp_pe.close()


if __name__ == '__main__':

	voice_dir = 'static/files'
	scp_dir = 'model/src2/preprocessed/' 
	dataset = 'eval'

	input_voices = []
	for r, ds, fs in os.walk(voice_dir):
		input_voices = [(r+"/"+f, f) for f in fs]
			
	list_proc = []

	extract_waveforms(input_voices, scp_dir)
