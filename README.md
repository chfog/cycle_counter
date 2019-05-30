CycleCounter
============

a program to help with cycle counts

## Table of Contents
- [About](#about)
- [Installation](#installation)
- [Use](#use)
- [FAQ](#faq)

## About

CycleCounter is a simple program, built with python, to simplify cycle counts at Copperfield's Books. At its core, it is a set of routines that will take a text file of barcodes and a `.csv` file from Basil, and put the number of books at the end of each row. By using special barcodes, one can also keep track of where in the shelf an item was scanned. It's not fancy-looking, but it's accurate.

The best way to think of CycleCounter is like a blender: you put all of the ingredients (files) in a pitcher (folder), and press a button, and it does the rest.

## Installation

1. Begin by installing the latest version of [Python 3](https://www.python.org/downloads/windows/).
1. Click the green "Clone or Download" above, and download the ZIP.
1. Unzip the file and click `installer.py`.
1. On your desktop, you should now find two folders and a file `blender.py`. `blender.py` is the file that will launch CycleCounter, `cycle_counter` is a folder containing other source code (you shouldn't need to touch it), and `Pitcher` is exactly that: the pitcher you will use the blender on.
1. Uninstalling is as easy as deleting the files on your desktop. You'll need to do this before reinstalling.

## Use

Using this program is intended to be easy, but preparing the input for it requres some care. If you follow these directions exactly, however, you shouldn't have any issues.

### Scanning Books

1. On a laptop or tablet, open a basic text document (e.g. Notepad on Windows), and name it something obvious, like the section name.
1. Scan every book in the section, in order. If there's more than one of a particular book, scan each one individually.
1. When you reach the end of a shelf, scan the barcode of "New Shelf Marker," available in Basil. Similarly, "New Bay Marker" will mark the end of a bay. Only the latter needs to be scanned at the end of a bay.
1. If you scan a book too many times, you'll have to simply use the backspace key to delete that line, leaving the cursor at the beginning of a blank line.
1. When you've scanned everything, save the file and move it to the `Pitcher` folder on the manager's computer using a flash drive.

### Pulling a Report

CycleCounter works best with reports that have not been heavily modified from Basil's format. Any deletion, swapping, renaming, etc. of columns should be done after [blending](#blending), as it hasn't been tested on every manager's version of cycle count.

1. Generate reports in Basil and copy-paste them into Excel. If you are doing a report for multiple sections, they can be pasted in sequentially, _as long as the headers match_. CycleCounter will ignore any row that matches the header.
1. If you have any rows that should be checked even if the right number of books are found (for example, books that should be moved or pulled), add a "Notes" column. Any row with a nonempty notes column will be put in the `TO_CHECK.csv` file.
1. **Very Important**: Highlight the "ID" and "Barcode" columns and format the numbers to have 0 decimal places. Without this, Excel will silently truncate the ISBNs upon saving, and none will match. 
1. Save the spreadsheet _as a .csv_ to the folder that you want to use. Excel will ask whether you're sure you want to use the `.csv` format. Say yes. When you quit Excel, it will ask you to save unsaved changes, even if you have none. Say no.

### Blending

1. Once you have the `.txt` file of ISBNs and the `.csv` in the same folder, double-click on the `blender.py` file. You will see a prompt to drag and drop a folder name. If you are using the provided `Pitcher` folder, you can just press <Enter\>. 
1. You will then be asked to name the cycle count; this is just the name of the folder that will contain everything else. Press <Enter\>.
1. If all goes well, a new folder will appear within the one provided in step (1). It will contain: a file `FOUND.csv`, which should be self-explanatory; `TO_CHECK.csv`, containing rows whose "On Hand" column didn't match the number scanned; and `EXTRAS.csv`, a list of barcodes that didn't match any in the provided `.csv`s. This folder will also contain the `.txt` and `.csv` files, so that they don't interfere with future cycle counts.
1. You may get a message that a folder already exists, especially if you're re-running a count. You'll have to delete or rename it and run `blender.py` again. Make sure to move out the `.txt` and `.csv` files from scanning and pulling reports first. 
1. If nothing appears to happen, check that you pulled the report as detailed.

## FAQ

> Does this work with remainders?

Yes! The difficulties of counting remainders was one of the major motivations for this.

----

> What about magazines?

Yup!

----

> What about sides?

Yes, but since they're usually spread out across the store, and it's not always clear which section a side should belong to, they're best avoided.

----

> Why can't you make it use an `.xlsx` file instead of a `.csv`?

There are actually a number of ways to do this, but they all involve downloading more than just python and CycleCounter, as well as configuring it. This is nontrivial, and best avoided.

----

> Why specify a folder to work on rather than individual files?

I figured that my knowledge of making pretty pointy-clicky things (otherwise known as a graphical user interface) was not sufficent for something like this, and that it would be best to minimize the amount of dos-like interaction.

----

> Why does nothing happen when I run `blender.py`?

Since making and moving files around is the last step before CycleCounter ends, any errors will kill it before this point. Check to make sure that you've set up everything as detailed in [Use](#use).

----

> I think my way of doing cycle counts is faster/more efficient.

Okay, not a question, but I understand. The scanning process is certainly quicker than doing paper-and-pencil cycle counts, but preparing the `.csv` can be tedious, and going back to check things can make it seem like you haven't saved any time at all. We found that cycle counts were more efficient overall, but the greatest benefit came from unalphabetized sections like Biography. Also, we have found quite a few books that either in the wrong section or had been scrapped, which is less likely to be noticed with paper and pen. The latter case amounted to hundreds of dollars in inventory, so even if you do most of your counts another way, it may be worth it to use CycleCounter once in a while. It won't hurt my feelings one bit if you don't, though.

----

> Why is the `TO_CHECK.csv` file so long?

Did you make sure to do step (3) in [Pulling a Report](#pulling-a-report)? If not, Excel will have ruined Basil's nice ISBNs, and nothing will be able to match. Unfortunately, this is an issue with Excel, so I can't fix it.

----

> Why is the `EXTRAS.csv` so long?

The most common cause of this was scanning a 'region' of the store without pulling reports for all of the sections in that region.

----

> Is this really necessary?

No, absolutely not. Basil is a piece of 21st century software. The fact that it has no way to automate cycle counts is, frankly, ridiculous. This program is merely a workaround, and a pretty poor one at that. I hope, for all our sakes, that it becomes obsolete with a new update to Basil. 
