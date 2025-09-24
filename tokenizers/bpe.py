#Implementing bpe algorithm

# dataset
import os
import requests
 
# To train such a model, you need a dataset of sentence pairs. The model learns how to translate from the example sentence pairs in the dataset. You can source your own dataset. In this post, you will use the Anki dataset, which can be downloaded from https://www.manythings.org/anki/, and you can also use the copy hosted in Google:

if not os.path.exists("fra-eng.zip"):
    url = "http://storage.googleapis.com/download.tensorflow.org/data/fra-eng.zip"
    response = requests.get(url)
    with open("fra-eng.zip", "wb") as f:
        f.write(response.content)