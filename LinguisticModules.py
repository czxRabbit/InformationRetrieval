from nltk.stem import PorterStemmer


def Linguistic_modules(tokens_doc_list):
    modified_tokens_doc_list = []
    punctuation_symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+', '`', '~', '"', '\'',
                           ':', ';', '|', '/', '.', ',', '?', '[', ']', '{', '}', '<', '>']
    stemmer = PorterStemmer()
    for i in range(len(tokens_doc_list)):
        if tokens_doc_list[i][0] not in punctuation_symbols:
            new_word = tokens_doc_list[i][0].lower()
            new_word = stemmer.stem(new_word)
            modified_tokens_doc_list.append([new_word, tokens_doc_list[i][1]])
    return modified_tokens_doc_list
