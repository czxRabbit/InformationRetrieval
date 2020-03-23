from FileReading import Read_file
from LinguisticModules import Linguistic_modules
from Tokenization import Tokenize_file
from Sorting import Sort
from Posting import Posting
from Intersect import intersect5
import os
import time


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

    start_time = time.time()
    file_list = directory_listing()

    all_tokens = []

    for index, file in enumerate(file_list):
        # print("Read file: {}".format(file))
        content = Read_file(file)

        result1 = Tokenize_file(content, file)
        # print("Tokens and file ID:  (count {})".format(len(result1)))
        # print(result1)

        result2 = Linguistic_modules(result1)
        # print("Linguistic and file ID:  (count {})".format(len(result2)))
        # print(result2)
        all_tokens.extend(result2)
        # if index > 0:
        #     break
    print("All tokens: (count {})".format(len(all_tokens)))
    # print(all_tokens)
    sorted_tokens = Sort(all_tokens)
    print("Sorted tokens:  (count {})".format(len(sorted_tokens)))
    # print(sorted_tokens)
    posting_list = Posting(sorted_tokens)
    print("Posting list: (count {})".format(len(posting_list)))
    # print(result3)
    print("Running seconds: {}".format(time.time() - start_time))
    intersect5(posting_list)
