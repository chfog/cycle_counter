
import os
from cycle_counter import cycle_counter

print("Drag and drop a folder to blend, or press ENTER to use the 'Pitcher' folder.")
ind = input("> ")
if ind != '':
    os.chdir(ind)
else:
    os.chdir("Pitcher")
cycle_counter.main()
