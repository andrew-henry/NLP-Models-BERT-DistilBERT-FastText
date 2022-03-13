# -*- coding: utf-8 -*-
"""FastText.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1fGEF_WguEllw9gFSDNV3UNKseXV4C2ML
"""

!pip install ktrain

!git clone https://github.com/laxmimerit/Toxic-Comment.git

import numpy as np
import ktrain
from ktrain import text
import pandas as pd

PATH = "/content/Toxic-Comment/train.csv"
NUM_WORDS = 50000
MAXLEN = 150

train, val, preproc = text.texts_from_csv(PATH, 'comment_text', label_columns=['toxic', 'severe_toxic', 'obscene', 'threat', 'insult', 'identity_hate'],
                    ngram_range = 1, max_features = NUM_WORDS, maxlen = MAXLEN)

text.print_text_classifiers()

model = text.text_classifier('fasttext', train, preproc)

learner = ktrain.get_learner(model, train, val)

learner.autofit(0.001, 2)

predictor  = ktrain.get_predictor(learner.model, preproc)

predictor.predict(['I hate you'])
