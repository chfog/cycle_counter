


import isbn
import os
import blender_config
import Tables

class Record:

    def __init__(self, clean_isbn, number = 0, bay = 0, book = 0):
        self.isbn = clean_isbn
        self.number = number
        self.bay = bay
        self.book = book

    def increment(self):
        self.number += 1

    def get_header(self):
        return ["ID", "Found", "Bay", "book"]

    def get_ls(self):
        return [clean_isbn, number, bay, book]

    def num(self):
        return self.number



class Count:

    def __init__(self, isbns = []):
        self.founds = dict()

    def increment(self, raw_bc, bay = 0, book = 0, num = 1):
        comp = isbn.to_compare(raw_bc)
        if comp in self.founds:
            self.founds[comp].increment()
        else:
            self.founds[comp] = Record(isbn.to_display(raw_bc), num, bay, book)


    def split_csvs(self, csv_obj):

        matching_csv = Tables.Table(csv_obj.get_header() + ['Found'])
        non_matching = Tables.Table(csv_obj.get_header() + ['Found'])
        extras_csv = Tables.Table(Record.get_header())

        matching_col = []
        non_matching_col = []

        csv_isbns = set()

        for row in csv_obj.rows():

            if row[csv_obj.col_number("Barcode")]:
                csv_isbn = isbn.to_compare(row[csv_obj.col_number("Barcode")])
            else:
                csv_isbn = isbn.to_compare(row[csv_obj.col_number("ID")])

            num_found = self.founds.get(csv_isbn, Record()).num()
            csv_isbns.add(csv_isbn)

            if int(row[csv_obj.col_number("On Hand")]) == num_found and \
               (not csv_obj.has_col("Notes") or \
               not row[csv_obj.col_number("Notes")]):
                matching_csv.add_row(row + [num_found])
            else:
                non_matching.add_row(row + [num_found])

        for isbn, record in self.founds.items():
            if isbn not in csv_isbns:
                extras_csv.add_row(record.get_ls())

        return (matching_csv, non_matching, extras_csv)


def is_excluded(f, excludes):
    for ex in excludes:
        if ex in f:
            return True
    return False



def give_filenames(cwd = '.', excludes = ["FOUND.csv", "TO_CHECK.csv"]):
    txts, csvs = [], []
    for fname in os.listdir(cwd):
        if is_excluded(fname, excludes):
            pass
        elif fname.endswith('txt'):
            txts.append(fname)
        elif fname.endswith('csv'):
            csvs.append(fname)
        else: pass
    return txts, csvs
