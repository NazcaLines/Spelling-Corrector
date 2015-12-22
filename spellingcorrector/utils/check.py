import functools


from spellingcorrector.utils import count


_ALPHABET = "abcdefghijklmnopqrstuvwxyz"


def checkDict(fn):
    @functools.wraps(fn)
    def new_func(*args, **kwargs):
        if len(count.NWORD) == 0:
            count.getTrain()
        return fn(*args, **kwargs)
    return new_func


def edit1(words):
    """
    edit distance = 1
    """
    split = [(words[:i], words[i:]) for i in range(len(words) + 1)]
    deletion = [a + b[1:] for a,b in split if b]
    insertion = [a + c + b for a,b in split for c in _ALPHABET]
    alteration = [a + c + b[1:] for a,b in split for c in _ALPHABET if b]
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


@checkDict
def correct(words):
    a = edit0([words])
    b = edit0(edit1(words))
    c = edit2(words)
    d = [words]
    # candidates = edit0([words]) or edit0(edit1(words)) \
    #                 or edit2(words) or [words]
    candidates = a or b or c or d
    e = max(candidates, key=count.NWORD.get)
    return e


if __name__ == '__main__':
    print correct('speling')