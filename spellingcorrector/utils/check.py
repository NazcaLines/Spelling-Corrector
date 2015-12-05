import functools

from spellingcorrector.utils import count

_ALPHABET = "abcdefghijklmnopqrstuvwxyz"

def check():
    pass


def checkIns():

    def wrapper(fn):
        @functools.wraps(fn)
        def new_func(*args, **kwargs):
            ins = args[1]
            if isinstance(ins, count.Count):
                args = list(args)
                return fn(*args, **kwargs)
            else:
                raise TypeError(
                    'must passed into an instance of utils.count:Conut')
        return new_func
    return wrapper


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



@checkIns
def edit2(words, ins):
    """
    edit diatance = 2
    """
    return set(e2 for e1 in edit1(words)
               for e2 in edit1(e1)
               if e2 in ins.nwords)


@checkIns
def edit0(words, ins):
    """
    edit distance = 0, that's say the word is correct.
    """
    return set(e0 for e0 in words
               if e0 in ins.nwords)


@checkIns
def correct(words, ins):
    candidates = edit0(words, ins) or edit1(words) \
                    or edit2(words, ins) or [words]
    return max(candidates).keys()[0]

