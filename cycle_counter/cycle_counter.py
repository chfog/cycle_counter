
import datetime
import csv
import os
from . import cycle_counter_helper as cch
from . import Tables
from . import blender_config

def main():

    txts, csvs = cch.give_filenames()
    count = cch.Count()

    for name in txts: ##book resets at start of bay, bay resets when we reach newbay number.
        bay =   1
        shelf = 1
        book =  1
        prev = ''
        for line in open(name, 'r', newline = ''):
            if line.strip() == blender_config.newbay:
                bay += 1
                shelf = 1
                book = 1
            elif line.strip() == blender_config.newshelf:
                shelf += 1
                book = 1
            else:
                count.increment(line, bay, shelf, book)
                if line != prev:
                    book += 1
                    prev = line

    master_csv = Tables.Table()

    for name in csvs:
        f = list(csv.reader(open(name, 'r', newline = '')))
        each_csv = Tables.Table(f[0], f[1:])
        if not each_csv.has_col("Notes"):
            each_csv.add_col("Notes")
        else:
            pass
        master_csv = master_csv.add_table(each_csv)

    founds, non_matching, extras = count.split_csvs(master_csv)
    d_str = input("Give this cycle count a name: ") + datetime.date.today().strftime("%m.%d.%Y")

    try:
        os.mkdir(d_str) 
        csv.writer(open(os.path.join(d_str, 'FOUND.csv'), 'w', newline = '')).writerows(founds.get_complete_table())
        csv.writer(open(os.path.join(d_str, 'TO_CHECK.csv'), 'w', newline = '')).writerows(non_matching.get_complete_table())
        csv.writer(open(os.path.join(d_str, 'EXTRAS.csv'), 'w', newline = '')).writerows(extras.get_complete_table())

        for name in csvs:
            os.rename(name, os.path.join(d_str, name))
        for name in txts:
            os.rename(name, os.path.join(d_str, name))

    except (FileExistsError, OSError):
        input("The folder " + d_str + " already exists. Remove it or rename it and try again.")
