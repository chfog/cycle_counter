## This is the configuration file for the blender script
## If you are running this script as explained in the documentation, you should
## have no reason to edit it. However, it can be edited to provide additional
## functionality and customization.

## This variable should be set to the column in your input csv that contains
## the ISBNs. Index it from zero (eg, if it's the fifth column, put 4)
isbn_col_number = 0

## This variable is the column number of the number of items on-hand. Again,
## index from 0
on_hand_col_number = 10

## This is the column where the number of found items will be put. Again,
## index from 0. If you would like it to be at the end of the column, put -1.
## The default puts it in the column following the number on hand.
found_col_number = on_hand_col_number + 1

## This is a list of column headers, as they should appear in the output files.
col_format_list = []
