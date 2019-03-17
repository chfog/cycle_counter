
import datetime
import csv
import os
import cycle_counter_helper as cch
import Tables
import blender_config

##os.chdir('/Users/chf')
##CSV = "trial-cycle-count.csv"
##TXT = "test-isbns.txt"



def main(wd = '.'):

    txts, csvs = cch.give_filenames()
    count = cch.Count()

    for name in txts:
        bay = 1
        book = 1
        for line in open(name, 'r', newline = ''):
            if line == blender_config.newbay:
                bay += 1
                book = 1
            else:
                count.increment(line, bay, book)
                book += 1
    master_csv = Tables.Table()

    for name in csvs:
        f = csv.reader(open(name, 'r', newline = ''))
        each_csv = Tables.Table(f[0], f[1:])
        if not each_csv.has_col("Notes"):
            each_csv.add_col("Notes")
        else:
            pass
        master_csv.add_table(each_csv)

    founds, non_matching, extras = count.split_csvs(master_csv)
    d_str = datetime.date.today().strftime("%m.%d.%Y_")
    csv.writer(open(d_str + 'FOUND.csv', 'w', newline = '')).writerows(founds.get_complete_table())
    csv.writer(open(d_str + 'TO_CHECK.csv', 'w', newline = '')).writerows(non_matching.get_complete_table() + extras.get_complete_table())
