from FileReading import Read_file
from LinguisticModules import Linguistic_modules
from Tokenization import Tokenize_file
from Sorting import Sort
import os


if __name__ == '__main__':
    def directory_listing():
        print("directory_listing")
        print(os.getcwd())

        data_file = 'BigData'
        directory_list = []
        for i in os.listdir(data_file):
            directory_list.append(data_file + '/' + i)

        print("directory_list.length:{}".format(len(directory_list)))
        print("first:{}".format(directory_list[0]))

        return directory_list

    file_list = directory_listing()

    all_tokens = []

    for index, file in enumerate(file_list):
        print("Read file: {}".format(file))
        content = Read_file(file)

        result1 = Tokenize_file(content, file)
        print("Tokens and file ID:  (count {})".format(len(result1)))
        print(result1)

        result2 = Linguistic_modules(result1)
        print("Linguistic and file ID:  (count {})".format(len(result2)))
        print(result2)
        all_tokens.extend(result2)
        if index > 0:
            break
    print("All tokens: (count {})".format(len(all_tokens)))
    print(all_tokens)
    sorted_tokens = Sort(all_tokens)
    print("Sorted tokens:  (count {})".format(len(sorted_tokens)))
    print(sorted_tokens)

    # Inverted index test case
    posting_list = {}
    for pairs in sorted_tokens:
        token, document_id = pairs[0], pairs[1]
        if not posting_list.get(token):
            posting_list[token] = [{document_id: 1}]
        else:
            is_added = 0
            for item in posting_list[token]:
                if item.get(document_id):
                    item[document_id] += 1
                    is_added = 1
                    break
            if not is_added:
                posting_list[token].append({document_id: 1})
    print("posting_list:")
    print(posting_list)