import os

def reset(path):
    if input('Reset? (o/x)\n').lower() == 'o':
        for file in os.listdir(path):
            os.remove(path + '/' + file)
        print(f'All files in {path} are removed.')