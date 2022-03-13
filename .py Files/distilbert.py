# -*- coding: utf-8 -*-
"""DistilBERT.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1woGv-_onpUCnI_cLWgxe1DhMgyDPnV_x

DistilBERT is a transformers model, smaller and faster than BERT, which was pretrained on the same corpus in a self-supervised fashion, using the BERT base model as a teacher. This means it was pretrained on the raw texts only, with no humans labelling them in any way (which is why it can use lots of publicly available data) with an automatic process to generate inputs and labels from those texts using the BERT base model.
"""

!pip install ktrain

!git clone https://github.com/laxmimerit/IMDB-Movie-Reviews-Large-Dataset-50k.git

import ktrain
from ktrain import text
import numpy as np
import pandas as pd
import tensorflow as tf
from google.colab import drive

data_test = pd.read_excel('/content/IMDB-Movie-Reviews-Large-Dataset-50k/test.xlsx', dtype= str)

data_train = pd.read_excel('/content/IMDB-Movie-Reviews-Large-Dataset-50k/train.xlsx', dtype = str)

data_train.sample(7)

text.print_text_classifiers()

(train, val, preproc) = text.texts_from_df(train_df=data_train, text_column='Reviews', label_columns='Sentiment',
                   val_df = data_test,
                   maxlen = 400,
                   preprocess_mode = 'distilbert')

model = text.text_classifier(name = 'distilbert', train_data = train, preproc=preproc)

learner = ktrain.get_learner(model = model,
                             train_data = train,
                             val_data = val,
                             batch_size = 6)

learner.fit_onecycle(lr = 2e-5, epochs=2)

predictor = ktrain.get_predictor(learner.model, preproc)

drive.mount('/content/drive')

predictor.save('/content/drive/My Drive/distilbert')

data = ['this movie was much better than I expected. storyline was really well written',
        'the movie was straight trash. I would rather watch paint dry than watch 5 mins of this movie again']

predictor.predict(data)

predictor.get_classes()

predictor.predict(data, return_proba=True)
