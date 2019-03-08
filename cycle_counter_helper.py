



import os


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

        matching_csv = []
        non_matching = []
        extras_csv = []

        csv_isbns = set()

        for row in csv_obj:
            csv_isbn = row[isbn_col_num]
            row.append(self.founds.setdefault(csv_isbn, 0))
            csv_isbns.add(csv_isbn)
            if int(row[on_hand_col_num]) == self.founds[csv_isbn]:
                matching_csv.append(row)
            else:
                non_matching.append(row)

        for isbn, num_found in self.founds.items():
            if isbn not in csv_isbns:
                extras_csv.append([isbn, num_found])

        return (matching_csv, non_matching, extras_csv)



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



def give_filenames(cwd = '.', excludes = ["FOUND.csv", "TO_CHECK.csv"]):
    txts, csvs = [], []
    for f in os.listdir(cwd):
        if f.split('.')[-1] == 'txt':
            txts.append(f)
        elif f.split(".")[-1] == 'csv' and f not in excludes:
            csvs.append(f)
        else: pass
    return txts, csvs
