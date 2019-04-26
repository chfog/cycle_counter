



def to_compare(isbn):
    if isbn.startswith("{"):
        return isbn[4:13]
    elif isbn.startswith("978"):
        return isbn[3:12]
    elif isbn.startswith("991"):
        return isbn[0:9]
    elif isbn.startswith("^"):
        return isbn[0:13].lstrip("^0")
    else:
        return isbn


def to_display(isbn):
    if isbn.startswith("{"):
        return isbn[1:14]
    elif isbn.startswith("^"):
        return isbn[1:13]
    else: return isbn
