def Range(x, y, func=None, filt=None):
    if func:
        if filt:
            for i in range(x, y):
                if filt(i):
                    yield func(i)
        else:
            for i in range(x, y):
                yield func(i)
    else:
        if filt:
            for i in range(x, y):
                if filt(i):
                    yield i
        else:
            for i in range(x, y):
                yield i
