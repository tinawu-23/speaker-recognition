'''
    Combined prediction model for two speaker recognition models
    MLP for binary classification
'''

from keras.models import Sequential
from keras.layers import Dense, Dropout
import pickle
import numpy as np


class Classifier():
    def __init__(self):

        self.model = Sequential()
        self.model.add(Dense(64, input_dim=1, activation='relu'))
        #self.model.add(Dropout(0.5))
        self.model.add(Dense(128, activation='relu'))
        self.model.add(Dense(512, activation='relu'))
        self.model.add(Dropout(0.5))
        self.model.add(Dense(256, activation='relu'))

        self.model.add(Dense(1, activation='sigmoid'))

        self.model.compile(optimizer='rmsprop',
              loss='binary_crossentropy',
              metrics=['accuracy'])

    def train(self, scores, labels, epochs=30):
        # Need to partition scores and labels
        scores_train = scores[:4300]
        scores_dev = scores[4300:]
        labels_train = labels[:4300]
        labels_dev = labels[4300:]

        self.model.fit(scores_train, labels_train, epochs=epochs, batch_size=64)
        score = self.model.evaluate(scores_dev, labels_dev, batch_size=64)
        print(f"Score: {score}")

    def predict(self, scores):
        return self.model.predict(scores, batch_size=4)


if __name__ == '__main__':
    classifier = Classifier()

    # scores = np.load("model/prediction_scores.npy")
    # labels = np.load("model/groundtruth_labels.npy")
    # print(scores, labels)
    # classifier.train(scores, labels)



    with open("result1.pickle", "rb") as f:
        model1_scores = pickle.load(f)
    with open("result2.pickle", "rb") as f:
        model2_scores = pickle.load(f)
    scores = [sum(x)/2 for x in zip(model1_scores, model2_scores)]

    print('Scores: \n')
    print(scores)

    with open("result.txt", "w+") as w:
        print('HEREERERERE!!!!!!!!!!!!!!!!!!!!!!')
        threshold = scores[0]
        scores = scores[1:]
        first_key_scores = scores[:len(scores)//2]
        second_key_scores = scores[len(scores)//2:]
        y_pred = [1 if x > threshold or y > threshold else 0 for x, y in zip(first_key_scores, second_key_scores)]
        indexes = [i+1 for i,x in enumerate(y_pred) if x == 1]
        print(indexes)
        try:
            w.write(' '.join(str(x) for x in indexes))
        except ValueError:
            w.write("")
    
