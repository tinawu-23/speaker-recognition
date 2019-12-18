'''
    Output similarity score from model2
    Created with reference from https://github.com/Jungjee/RawNet
'''

import collections

import os
import numpy as np
import yaml
import pickle
from time import sleep
from keras.optimizers import *
from keras.models import Model

from model_RawNet import get_model


def cos_sim(a,b):
  return np.dot(a,b) / (np.linalg.norm(a) * np.linalg.norm(b))


def compose_spkFeat_dic(lines, model, preprocessed_voices, f_desc_dic, base_dir):
  '''
  Extracts speaker embeddings from a given model
  =====
  lines: (list) A list of strings that indicate each utterance
  model: (keras model) DNN that extracts speaker embeddings,
  output layer should be rmoved(model_pred)
  f_desc_dic: (dictionary) A dictionary of file objects
  '''
  dic_spkFeat = {}
  preprocessed_voices = np.load(preprocessed_voices)
  for line in lines:
    full_path, _, file_pointer = line.strip().split(' ')
    i = int(file_pointer)
    spkFeat = model.predict(preprocessed_voices[f'arr_{i}'].reshape(1,-1,1))[0]
    dic_spkFeat[full_path] = spkFeat

  return dic_spkFeat
		

if __name__ == '__main__':

  # Load yaml file for settings
  with open('model/src2/RawNet.yaml', 'r') as f_yaml:
    parser = yaml.load(f_yaml)

  # Open prepcoessed files and load test paris
  preprocessed_voice = open("model/src2/"+parser['eval_scp'], 'r').readlines()
  test_file = open('model/meta/sets.txt', 'r').readlines() 
  parser['model']['nb_spk'] = 1211

  # Load model and pretrained weight
  model, m_name = get_model(argDic = parser['model'])
  model_pred = Model(inputs=model.get_layer('input_RawNet').input, outputs=model.get_layer('code_RawNet').output)
  model.load_weights("model/src2/RawNet_weights.h5")

  # Run model and write to a dict
  dic_eval = compose_spkFeat_dic(lines=preprocessed_voice, model=model_pred, \
                                preprocessed_voices='model/src2/preprocessed/test_pe.ark.npz', \
                                f_desc_dic = {}, base_dir = parser['base_dir'])

  y = []
  y_score = []

  voice_file_path = 'static/files/'

  # Computes similarity between the scores and writes to a file
  for smpl in test_file:
    target, spkMd, utt = smpl.strip().split(' ')
    print(spkMd, utt)
    target = int(target)
    cos_score = cos_sim(dic_eval[voice_file_path+spkMd], dic_eval[voice_file_path+utt])
    y.append(target)
    y_score.append(cos_score)
    print('{score} {target}\n'.format(score=cos_score,target=target))

    with open("result2.pickle", "wb") as w:
      pickle.dump(y_score, w)
