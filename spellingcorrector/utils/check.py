import functools

from spellingcorrector.utils import count

_ALPHABET = "abcdefghijklmnopqrstuvwxyz"

def check():
    pass


def edit1(words):
    """
    edit distance = 1
    """
    split = [(words[:i], words[1:]) for i in len(words)]
    deletion = [a + b[1:] for a,b in split if b]
    insertion = [a + c + b for a,b in split for c in _ALPHABET]
    alteration = [a + c + b[1:] for a,b in split for c in _ALPHABET]
    transposition = [a + b[1] + b[0] + b[2:] for a,b in split if len(b)>1]
    return set(deletion + insertion + alteration + transposition)



def edit2(words):
    """
    edit diatance = 2
    """
    return set(e2 for e1 in edit1(words)
               for e2 in edit1(e1)
               if e2 in count.NWORD)


def edit0(words):
    """
    edit distance = 0, that's say the word is correct.
    """
    return set(e0 for e0 in words
               if e0 in count.NWORD)


def correct(words):
    candidates = edit0(words) or edit1(words) \
                    or edit2(words) or [words]
    return max(candidates).keys()[0]

