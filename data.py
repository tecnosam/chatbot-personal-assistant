
# use natural language toolkit
import nltk
from nltk.stem.lancaster import LancasterStemmer
import joblib as jb

import numpy as np
import pandas as pd

# TODO: retrain catalina with updated dataset

class _Model:
    # word stemmer
    def __init__(self):
        pass
    def train(self, filename = 'users.csv'):

        self.stemmer_ = LancasterStemmer()

        data = pd.read_csv("static/users.csv")
        self.training_data_ = []

        for i in range(data.shape[0]):
            self.training_data_.append({'human': data['human'][i], 'intent': data['intent'][i]})

        print(f"There are {len(self.training_data_)}")


        # capture unique stemmed words in the training corpus
        self.corpus_words = {}
        self.class_words = {}
        # turn a list into a set (of unique items) and then a list again (this removes duplicates)
        classes = list(set([a['intent'] for a in self.training_data_]))
        for c in classes:
            # prepare a list of words within each class
            self.class_words[c] = []
        print( f"there are {len(classes)} distinct intents" )

        # loop through each sentence in our training data
        print( f"Analyzing {len(self.training_data_)} text data...")
        for data in self.training_data_:
            # tokenize each sentence into words
            for word in nltk.word_tokenize(data['human']):
                # ignore a some things
                if word not in ["?", "'s"]:
                    # stem and lowercase each word
                    stemmed_word = self.stemmer_.stem(word.lower())
                    # have we not seen this word already?
                    if stemmed_word not in self.corpus_words:
                        self.corpus_words[stemmed_word] = 1
                    else:
                        self.corpus_words[stemmed_word] += 1

                    # add the word to our words in class list
                    self.class_words[data['intent']].extend([stemmed_word])

    # calculate a score for a given class taking into account word commonality
    def calculate_class_score(self, sentence, class_name, show_details=True):
        score = 0
        # tokenize each word in our new sentence
        for word in nltk.word_tokenize(sentence):
            # check to see if the stem of the word is in any of our classes
            if self.stemmer_.stem(word.lower()) in self.class_words[class_name]:
                # treat each word with relative weight
                score += (1 / self.corpus_words[self.stemmer_.stem(word.lower())])

                if show_details:
                    print ("   match: %s (%s)" % (self.stemmer_.stem(word.lower()), 1 / self.corpus_words[self.stemmer_.stem(word.lower())]))
        return score

    def classify(self, sentence):
        high_class = None
        high_score = 0
        result = []
        # loop through our classes
        for c in self.class_words.keys():
            # calculate score of sentence for each class
            score = self.calculate_class_score(sentence, c, show_details=False)
            # keep track of highest score
            result.append( {'intent': c, 'score': score} )
            # if score > high_score:
            #     high_class = c
            #     high_score = score

        return sorted(result, key = lambda x: x['score'], reverse = True)

    def score(self):
        count = 0
        for i in self.training_data_:
            pred = self.classify( i['human'] )
            if ( pred[0]['intent'] == i['intent'] ):
                count += 1
        return count/len(self.training_data_)

    # print( classify( "Add this tea to my order cart please" ) )

# mod = _Model()
# mod.train()
# print( mod.score() )
# jb.dump( mod, "catalina.pkl" )


# score()