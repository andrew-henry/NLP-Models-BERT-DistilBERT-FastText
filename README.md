# NLP-Models-BERT-DistilBERT-FastText

BERT
--
Bidirectional Encoder Representations from Transformers is a transformer-based machine learning technique for natural language processing pre-training developed by Google. BERT was created and published in 2018 by Jacob Devlin and his colleagues from Google

#### BERT Variations 

* ALBERT - ALBERT stands for A Lite BERT and is a modified version of BERT NLP model. It builds on three key points such as Parameter Sharing, Embedding Factorization and Sentence Order Prediction (SOP).

* RoBERTa - An optimized BERT pretraining approach. RoBERTa builds on BERT’s language masking strategy, wherein the system learns to predict intentionally hidden sections of text within otherwise unannotated language examples. RoBERTa, which was implemented in PyTorch, modifies key hyperparameters in BERT, including removing BERT’s next-sentence pretraining objective, and training with much larger mini-batches and learning rates. This allows RoBERTa to improve on the masked language modeling objective compared with BERT and leads to better downstream task performance.

* ELECTRA - Efficiently Learning an Encoder that Classifies Token Replacements Accurately

* SpanBERT - SpanBERT is an improvement on the BERT model providing improved prediction of spans of text.


DistilBERT
--
DistilBERT is a transformers model, smaller and faster than BERT, which was pretrained on the same corpus in a self-supervised fashion, using the BERT base model as a teacher. This means it was pretrained on the raw texts only, with no humans labelling them in any way (which is why it can use lots of publicly available data) with an automatic process to generate inputs and labels from those texts using the BERT base model. 



FastText
--
fastText is a library for learning of word embeddings and text classification created by Facebook's AI Research lab. The model allows one to create an unsupervised learning or supervised learning algorithm for obtaining vector representations for words. 
