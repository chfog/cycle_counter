

import os
import shutil

desk_dir = os.path.join(os.path.expanduser('~'), 'Desktop')

shutil.copytree('cycle_counter', os.path.join(desk_dir, 'cycle_counter'))
shutil.copy2('blender.py', desk_dir)
shutil.copy2('README.md', os.path.join(desk_dir, 'cycle_counter'))
os.mkdir(os.path.join(desk_dir, 'Pitcher'))
