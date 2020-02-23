import os

data_file = 'BigData'
directory_list = []
for i in os.listdir(data_file):
    directory_list.append(data_file + '/' + i)