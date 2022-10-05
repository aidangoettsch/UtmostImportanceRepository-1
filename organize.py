import os
from random import randint, shuffle

WORDS = open('/usr/share/dict/words').read().splitlines()

def get_random_dirname ():
    return '-'.join([WORDS[randint(0, len(WORDS))] for _ in range(3)])

dirs = [get_random_dirname() for _ in range(10)]
files = [f for f in os.listdir() if os.path.isfile(f)]
n = len(files) // len(dirs)

files.remove('organize.py')
shuffle(files)

for new_dir in dirs:
    os.mkdir(new_dir)

    for _ in range(n):
        filename = files.pop()
        os.rename(filename, f"{new_dir}/{filename}")

while len(files):
    filename = files.pop()
    os.rename(filename, f"{dirs[-1]}/{filename}")
