import os


def walk_files(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            yield os.path.join(root, file)


directory = 'D:\Collab_PyQT_Net_Chat'  #на проекте тестил
for file_path in walk_files(directory):
    print(file_path)
