import os
path_dir = './darknet/data/img'

file_list = os.listdir(path_dir)

f = open("train.txt", 'w')
for i in file_list:
    if i[-4:] != '.txt':
        f.write('./darknet/data/img' + i + '\n')

f.close()