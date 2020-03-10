from nltk.stem import PorterStemmer
import re


def Linguistic_modules(tokens_doc_list):
    modified_tokens_doc_list = []
    stemmer = PorterStemmer()
    for i in range(len(tokens_doc_list)):
        new_word = re.sub(r'[!@#$%^&*()\-_=+\'`~\":;|/.,?\[\]{\}<>—]', "",
                          tokens_doc_list[i][0])
        new_word = new_word.lower()
        new_word = stemmer.stem(new_word)
        if new_word:
            modified_tokens_doc_list.append([new_word, tokens_doc_list[i][1]])
    return modified_tokens_doc_list
