# -*- coding: utf-8 -*-
"""BERT Sentiment Classification.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Vu7iBXB5bkzjCM2e06nvsanYCSIrwXIL

#### Notebook contents 

* BERT- Bidirectional Encoder Representations from Transformers is a transformer-based machine learning technique for natural language processing pre-training developed by Google. BERT was created and published in 2018 by Jacob Devlin and his colleagues from Google

* Installing & importing packages 

* Cloning github repo
"""

import numpy as np
import pandas as pd
import ktrain
from ktrain import text

import tensorflow as tf

!pip install ktrain

tf.__version__

!git clone https://github.com/laxmimerit/IMDB-Movie-Reviews-Large-Dataset-50k.git

data_train = pd.read_excel('/content/IMDB-Movie-Reviews-Large-Dataset-50k/train.xlsx', dtype = str)

data_test = pd.read_excel('/content/IMDB-Movie-Reviews-Large-Dataset-50k/test.xlsx',dtype = str)

data_train.tail(7)

data_test.head(7)

data_train.shape

data_test.shape

(X_train, y_train), (X_test, y_test), preproc = text.texts_from_df(train_df = data_train, text_column= 'Reviews',
                                                                   label_columns= 'Sentiment', val_df= data_test,
                                                                   maxlen= 500, preprocess_mode= 'bert')

model = text.text_classifier(name = 'bert', train_data = (X_train, y_train), preproc = preproc)

learner = ktrain.get_learner(model = model, train_data = (X_train, y_train), val_data = (X_test, y_test), batch_size = 6)

learner.fit_onecycle(lr=2e-5, epochs=1)

predictor = ktrain.get_predictor(learner.model, preproc)

data = ['this was a well put together film. great acting', 
        'would rewatch this movie again and again',
        'do no waste time seeing this movie. I would rather watch paint dry']

predictor.predict(data)

predictor.predict(data, return_proba = True)

predictor.get_classes()

predictor.save('/content/bert')

!zip -r /content/bert.zip /content/bert

predictor_load = ktrain.load_predictor('/content/bert')

predictor_load.get_classes()

predictor_load.predict(data)

