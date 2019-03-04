
import os
import cycle_counter

print("Drag and drop a folder to blend, or press ENTER to use the current folder.")
ind = input("> ")
if ind != '':
    os.chdir(ind)
cycle_counter.main()
