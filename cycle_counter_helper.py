






class Count:

    def __init__(self, isbns = []):
        self.founds = dict()
        for isbn in isbns:
            self.increment(isbn)

    def increment(self, isbn, num = 1):
        if isbn in self.founds:
            self.founds[isbn] += 1
        else:
            self.founds[isbn] = 1

    def split_csvs(self, csv_obj, isbn_col_num = 0, on_hand_col_num = 10):
        founds_csv = []
        non_matching = []
        extras_csv = []

        rows_dict = dict(map(lambda x: (x[isbn_col_num], x)))

        for isbn, num_found in self.founds.items():
            if isbn in rows_dict:
                rows_dict[isbn].append(num_found)
                if int((rows_dict[isbn])[on_hand_col_num]) == num_found:
                    founds_csv.append(rows_dict[isbn])
                else:
                    non_matching.append(rows_dict[isbn])
            else:
                extras_csv.append()

        return (founds_csv, non_matching, extras_csv)



def isbn_clean(isbn):
    if isbn[0] == '{':
        return isbn[1:14]
    elif isbn[0] == '^':
        return isbn[1:13]
    else:
        raise ValueError


def csv_clean(csv_obj):
    return csv_obj[1:]
    #todo: check to see whether header is included
    #      maybe cut columns based on configuration?
    #      maybe this should be its own class



def give_filenames(cwd = '.'):
    txts, csvs = [], []
    for f in os.listdir(cwd):
        if f.split('.')[-1] == 'txt':
            txts.append(f)
        elif f.split(".") == 'csv':
            csvs.append(f)
        else: pass
    return txts, csvs
