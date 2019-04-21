#!/usr/bin/env python

import glob
import os

def latest():
    list_of_files = glob.glob('./videos/*.mp4')
    latest_file = max(list_of_files, key=os.path.getctime)
    print(latest_file)
    return latest_file