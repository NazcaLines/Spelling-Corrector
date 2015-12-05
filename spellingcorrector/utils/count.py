import os
import sys
import traceback
import functools

CORPUS_DIR = '../data/corpus.txt'

global NWORD

def checkCorpus(fn):
    @functools.wraps(fn)
    def new_func(*args, **kwargs):
        if not os.path.isfile(CORPUS_DIR):
            raise IOError('cannot find corpus in data/')
        return fn(*args, **kwargs)
    return  new_func


@checkCorpus
def train():
    global NWORD
    NWORD = []
    f = file(CORPUS_DIR).open()
    for line in f:
        split = line.split()
        tmp = {split[0]:split[1]}
        NWORD.append(tmp)


def getTrain():
    """
    simple singleton implement
    """
    global NWORD
    try:
        NWORD
    except:
        train()
    return NWORD



if __name__ == "__main__":
    getTrain()