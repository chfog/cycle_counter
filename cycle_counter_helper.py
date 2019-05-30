


import isbn
import os
import blender_config
import Tables

class Record:

    def __init__(self, clean_isbn = '', number = 0, bay = '', shelf = '', book = ''):
        self.isbn = clean_isbn
        self.number = number
        self.bay = bay
        self.shelf = shelf
        self.book = book

    def increment(self):
        self.number += 1

    def get_header(start = 0):
        return ["ID", "Found", "Bay", "Shelf", "Book"][start:]

    def get_ls(self, start = 0):
        return [self.isbn, self.number, self.bay, self.shelf, self.book][start:]

    def num(self):
        return self.number



class Count:

    def __init__(self, isbns = []):
        self.founds = dict()

    def increment(self, raw_bc, bay = 0, shelf = 0, book = 0, num = 1):
        comp = isbn.to_compare(raw_bc)
        if comp in self.founds:
            self.founds[comp].increment()
        else:
            self.founds[comp] = Record(isbn.to_display(raw_bc), num, bay, shelf, book)


    def split_csvs(self, csv_obj):
        matching_csv = Tables.Table(csv_obj.get_header() + Record.get_header(1))
        non_matching = Tables.Table(csv_obj.get_header() + Record.get_header(1))
        extras_csv = Tables.Table(Record.get_header())

        matching_col = []
        non_matching_col = []

        csv_isbns = set()

        for row in csv_obj.get_rows():
            if csv_obj.has_col("Barcode") and row[csv_obj.col_number("Barcode")]:
                csv_isbn = isbn.to_compare(row[csv_obj.col_number("Barcode")])
            else:
                csv_isbn = isbn.to_compare(row[csv_obj.col_number("ID")])

            found_record = self.founds.get(csv_isbn, Record())
            csv_isbns.add(csv_isbn)

            if int(row[csv_obj.col_number("On Hand")]) == found_record.num() and \
               (not csv_obj.has_col("Notes") or \
               not row[csv_obj.col_number("Notes")]):
                matching_csv.add_row(row + found_record.get_ls(1))
            else:
                non_matching.add_row(row + found_record.get_ls(1))

        for Isbn, record in self.founds.items():
            if Isbn not in csv_isbns:
                extras_csv.add_row(record.get_ls())

        return (matching_csv, non_matching, extras_csv)


def is_excluded(f, excludes):
    for ex in excludes:
        if ex in f:
            return True
    return False



def give_filenames(cwd = '.', excludes = ["FOUND.csv", "TO_CHECK.csv", "EXTRAS.csv"]):
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
