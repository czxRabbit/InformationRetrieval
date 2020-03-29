from functools import reduce
from nltk.stem import PorterStemmer
import re
import time


def intersect4(list_t1, list_t2):
    answer = []
    index_t1 = index_t2 = 0

    while index_t1 < len(list_t1) and index_t2 < len(list_t2):
        if list_t1[index_t1] == list_t2[index_t2]:
            answer.append(list_t1[index_t1])
            index_t1 += 1
            index_t2 += 1
        elif list_t1[index_t1] < list_t2[index_t2]:
            index_t1 += 1
        else:
            index_t2 += 1

    return answer


def intersect5(posting_list):
    start = time.time()
    answer = []
    keywords = []  # user inputs
    k_list = []  # a list of lists
    m = 0  # missing keywords count
    templist = []

    inputs = input("Please Enter:")
    stemmer = PorterStemmer()
    list1 = inputs.split()
    for i in range(len(list1)):
        new_word = re.sub(r'[!@#$%^&*()\-_=+\'`~\":;|/.,?\[\]{\}<>—_]', "", list1[i])
        new_word = new_word.lower()
        new_word = stemmer.stem(new_word)

        if new_word in posting_list.keys():
            keywords.append(new_word)

    # print(keywords)
    klen = len(keywords)
    if klen == 0:
        print("Your answer cannot be retrieved")
    elif klen == 1:
        for i in range(len(posting_list[keywords[0]])):
            answer.extend(list(posting_list[keywords[0]][i].keys()))

    else:

        keywords.sort(key=lambda x: len(posting_list[x]))

        for m in range(len(keywords)):
            for n in range(len(posting_list[keywords[m]])):
                templist.extend(list(posting_list[keywords[m]][n].keys()))
            k_list.append(templist)
            templist = []

        # changes
        answer = reduce(intersect4, k_list)

        while not answer:
            tlen = len(k_list)
            if tlen == 2:
                answer.extend(k_list[0])
            else:
                k_list = k_list[:-1]
                answer = reduce(intersect4, k_list)
                m += 1
    end = time.time() - start

    print(keywords)
    while True:
        option = input("\nWhat do you want to know? \n1.time \n2.result \n3.new search \n4.exit\n")
        if option == "1":
            print(end)
        elif option == "2":
            print('First ten results are: {}'.format(answer[:10]))
            if m:
                print('Missing keywords: {}'.format(keywords[-m:]))
            print()
        elif option == "3":
            intersect5(posting_list)
            break
        elif option == "4":
            break
        else:
            print("Only four options. Sorry!")






