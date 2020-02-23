def Tokenize_file(file_content, document_id):
    tokens_doc_list = []
    for token in file_content.split():
        tokens_doc_list.append([token, document_id])
    return tokens_doc_list
