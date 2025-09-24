import re

with open("verdict.txt", 'r', encoding='utf-8') as f:
    raw_text = f.read()

# print('raw_text', raw_text)
# print('type(raw_text)', type(raw_text))
print('len(raw_text)', len(raw_text))

# Let's tokenise (words) in the text
# words = raw_text.split()

# using re
example_text = "hello, there everyone. Hope you are doing well."
result = re.split(r'([,.]|\s)', example_text)
# print(result)

preprocessed = re.split(r'[,.:;?_!"()\']|--|\s', raw_text)
preprocessed = [item.strip() for item in preprocessed if item.strip()]


# Converting tokens into token IDs
all_words = sorted(set(preprocessed))
vocab_size = len(all_words)
# print(vocab_size)

vocab = {token:integer for integer,token in enumerate(all_words)}

class SimpleTokenizer:
    def __init__(self, vocab):
        self.str_to_int = vocab
        self.int_to_str = {i:s for i,s in vocab.items()}
        pass

    def encode(self, text):
        preprocessed = re.split(r'[,.::?\'!_()"]|--|\s', text)
        preprocessed = [item.split() for item in preprocessed if item.strip()]
        ids = [self.str_to_int[s] for s in preprocessed]
        return ids

    def decode(self, token_ids):
        text = " ".join([self.int_to_str[i] for i in token_ids])
        text = re.sub(r'\s+([,.?!"()\'])', r'\1', text)
        return text




