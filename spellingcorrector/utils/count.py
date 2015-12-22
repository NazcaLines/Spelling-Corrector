import os
import functools


CORPUS_DIR = str(os.getcwd())[:str(os.getcwd()).index('spellingcorrector/')] \
             + 'data/corpus.txt'

NWORD = {}


def checkCorpus(fn):
    @functools.wraps(fn)
    def new_func(*args, **kwargs):
        t = os.path.isfile(CORPUS_DIR)
        if t == False:
            raise IOError('cannot find corpus in data/')
        return fn(*args, **kwargs)
    return  new_func


@checkCorpus
def train():
    global NWORD
    with open(CORPUS_DIR, 'r') as f:
        for line in f:
            split = line.split()
            #tmp = {split[0]:float(split[1])}
            NWORD[split[0]] = float(split[1])


def getTrain():
    """
    simple singleton implement
    """
    global NWORD
    if len(NWORD) == 0:
        train()
    return NWORD


if __name__ == "__main__":
    getTrain()
    print CORPUS_DIR
    print os.path.isfile(CORPUS_DIR)
    print len(NWORD)
