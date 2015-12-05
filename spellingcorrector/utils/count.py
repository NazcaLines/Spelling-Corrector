import os
import sys
import traceback
import functools

    _CORPUS_DIR = '../data/corpus.txt'

def checkCorpus(fn):
    @functools.wraps(fn)
    def new_func(ins, *args, **kwargs):
        if not os.path.isfile(Count._CORPUS_DIR):
            raise IOError('cannot find corpus in data/')
        return fn(ins, *args, **kwargs)
    return  new_func





    def __init__(self):
        self.corpus = []
        self.nword = []
        try:
            self.train()
        except IOError:
            print traceback.print_exc(file=sys.stderr)



    @checkCorpus
    def train():
        f = file(_CORPUS_DIR).open()
        for line in f:
            split = line.split()
            tmp = {split[0]:split[1]}
            nword.append(tmp)

if __name__ == "__main__":
    c = Count()



