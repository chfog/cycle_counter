
import sys
import csv
import os
import cycle_counter_helper as cch

##os.chdir('/Users/chf')
##CSV = "trial-cycle-count.csv"
##TXT = "test-isbns.txt"


def tie_txt_to_csv(txt_file, csv_file):
    rows = csv.reader(open(csv_file, 'r', newline = ''), dialect = 'excel')
    isbns = open(txt_file, 'r', newline = '')
    out_csv_found = csv.writer(open("found_" + csv_file, 'w', newline = ''), dialect = "excel")
    out_csv_to_check = csv.writer(open("to_check_" + csv_file, 'w', newline = ''), dialect = 'excel')
    founds = dict()
    extras = dict()
    for row in rows:
        row.append(0)
        founds[row[3]] = row
    for isbn in map(clean, isbns):
        if isbn in founds:
            (founds[isbn])[-1] += 1
        elif isbn in extras:
            (extras[isbn])[-1] += 1
        else:
            extras[isbn] = [isbn, 1]
    for row in founds.values():
        if int(row[5]) == row[7]:
            out_csv_found.writerow(row)
        else:
            out_csv_to_check.writerow(row)
    for row in extras.values():
        out_csv_to_check.writerow(row)



def main(wd = '.'):
    txts, csvs = cch.give_filenames()
    count = cch.Count()
    for name in txts:
        for line in open(name, 'r', newline = ''):
            count.increment(cch.isbn_clean(line))
    csv_obj = []
    for name in csvs:
        f = csv.reader(open(name, 'r', newline = ''))
        csv_obj.extend(f)
    founds, non_matching, extras = count.split_csvs(csv_obj, 3, 5)
    csv.writer(open('FOUND.csv', 'w', newline = '')).writerows(founds)
    csv.writer(open('TO_CHECK.csv', 'w', newline = '')).writerows(non_matching + extras)
