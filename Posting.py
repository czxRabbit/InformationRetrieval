def Posting(sorted_tokens):
    posting_list = {}
    pre_token, pre_document_id = sorted_tokens[0][0], sorted_tokens[0][1]
    posting_list[pre_token] = [{pre_document_id: 1}]
    index = 0
    for pairs in sorted_tokens[1:]:
        token, document_id = pairs[0], pairs[1]
        # After optimization
        if token != pre_token:
            posting_list[token] = [{document_id: 1}]
            index = 0
            pre_token, pre_document_id = token, document_id
        elif token == pre_token and document_id != pre_document_id:
            posting_list[token].append({document_id: 1})
            index += 1
            pre_document_id = document_id
        else:
            posting_list[token][index][document_id] += 1

        # Before optimization
        # if not posting_list.get(token):
        #     posting_list[token] = [{document_id: 1}]
        # else:
        #     is_added = 0
        #     for item in posting_list[token]:
        #         if item.get(document_id):
        #             item[document_id] += 1
        #             is_added = 1
        #             break
        #     if not is_added:
        #         posting_list[token].append({document_id: 1})
    return posting_list
