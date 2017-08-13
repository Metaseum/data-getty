#!/usr/local/bin/python3

import os, shutil

base_dir = 'json'

for directory, directories, files in os.walk(base_dir, topdown=False):
    for name in files:
        path = os.path.join(directory, name)
        if name.endswith('.json'):
            new_dir = '{}/{}/{}'.format(base_dir, name[2:4], name[4:6])
            new_path = '{}/{}'.format(new_dir, name)

            os.makedirs(new_dir, exist_ok=True)

            shutil.move(path, new_dir)