'''
    Predict from model1
    modified from https://github.com/WeidiXie/VGG-Speaker-Recognition
'''


from __future__ import absolute_import
from __future__ import print_function
import os
import sys
import numpy as np

import toolkits
import utils as ut

import pdb
import pickle

import argparse
parser = argparse.ArgumentParser()
# set up training configuration.
parser.add_argument('--gpu', default='', type=str)
parser.add_argument('--resume', default='model/src/weights.h5', type=str)
parser.add_argument('--batch_size', default=16, type=int)
parser.add_argument('--data_path', default='../static/files/', type=str)

# set up network configuration.
parser.add_argument('--net', default='resnet34s', choices=['resnet34s', 'resnet34l'], type=str)
parser.add_argument('--ghost_cluster', default=2, type=int)
parser.add_argument('--vlad_cluster', default=8, type=int)
parser.add_argument('--bottleneck_dim', default=512, type=int)
parser.add_argument('--aggregation_mode', default='gvlad', choices=['avg', 'vlad', 'gvlad'], type=str)
# set up learning rate, training loss and optimizer.
parser.add_argument('--loss', default='softmax', choices=['softmax', 'amsoftmax'], type=str)
parser.add_argument('--test_type', default='ai', choices=['ai'], type=str)

global args
args = parser.parse_args()

def main():

    # gpu configuration
    toolkits.initialize_GPU(args)

    import model
    # ==================================
    #       Get Train/Val.
    # ==================================
    print('Calculating test data lists...')
    
    # AI project list file
    if args.test_type == 'ai':
        verify_list = np.loadtxt('model/meta/sets.txt', str)
    else:
        raise IOError('Unknown test type.')

    verify_lb = np.array([int(i[0]) for i in verify_list])
    list1 = np.array([os.path.join(args.data_path, i[1]) for i in verify_list])
    list2 = np.array([os.path.join(args.data_path, i[2]) for i in verify_list])

    total_list = np.concatenate((list1, list2))
    unique_list = np.unique(total_list)

    # ==================================
    #       Get Model
    # ==================================
    # construct the data generator.
    params = {'dim': (257, None, 1),
              'nfft': 512,
              'spec_len': 250,
              'win_length': 400,
              'hop_length': 160,
              'n_classes': 5994,
              'sampling_rate': 16000,
              'normalize': True,
              }

    network_eval = model.vggvox_resnet2d_icassp(input_dim=params['dim'],
                                                num_class=params['n_classes'],
                                                mode='eval', args=args)

    # ==> load pre-trained model
    if args.resume:        
        # Load pretrained weight
        if os.path.isfile('model/src/weights.h5'):
            network_eval.load_weights('model/src/weights.h5', by_name=True)
            print('Successfully loading model {}.'.format(args.resume))
        else:
            raise IOError("No checkpoint found at '{}'".format(args.resume))
    else:
        raise IOError('Please type in the model to load')

    print('\nStart testing...')

    # The feature extraction process has to be done sample-by-sample,
    # because each sample is of different lengths.
    total_length = len(unique_list)
    feats, scores, labels = [], [], []
    for c, ID in enumerate(unique_list):
        specs = ut.load_data(ID, win_length=params['win_length'], sr=params['sampling_rate'],
                             hop_length=params['hop_length'], n_fft=params['nfft'],
                             spec_len=params['spec_len'], mode='eval')
        specs = np.expand_dims(np.expand_dims(specs, 0), -1)
    
        v = network_eval.predict(specs)
        feats += [v]
    
    feats = np.array(feats)

    allscores = []
    match = []
    nomatch = []

    # ==> compute the pair-wise similarity.
    print("Model 1 scores")
    for c, (p1, p2) in enumerate(zip(list1, list2)):
        ind1 = np.where(unique_list == p1)[0][0]
        ind2 = np.where(unique_list == p2)[0][0]

        v1 = feats[ind1, 0]
        v2 = feats[ind2, 0]

        scores += [np.sum(v1*v2)]
        labels += [verify_lb[c]]

        if c != 0 and verify_lb[c] == 1:
            match.append(scores[-1])
        elif verify_lb[c] == 0:
            nomatch.append(scores[-1])

        allscores.append(scores[-1])
        print('Score : {}'.format(scores[-1]))
    
    # For evaluation
    # match = [str(x) for x in match]
    # nomatch = [str(x) for x in nomatch]

    # with open("./eval/result.txt", "a") as w:
    #     matches = ','.join(match)
    #     nomatches = ','.join(nomatch)
    #     w.write(matches+'\n')
    #     w.write(nomatches+'\n')

    with open("result1.pickle", "wb") as w:
        pickle.dump(scores, w)


if __name__ == "__main__":
    main()
