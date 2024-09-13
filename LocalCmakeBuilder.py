from glob import glob
from pathlib import Path
from Message import *
import os
import sys

SRC_ENDINGS = ['/**/*.cpp', '/**/*.c']
HEADER_ENDINGS = ['/**/*.hpp', '/**/*.h']

SET_SRC_STR = lambda x: f"""#PROJECT WAS CREATED WITH PYMAKE
#PYMAKE: https://github.com/EndMy5uffering/PyCmakeToolKit
#THIS FILE WILL BE OVERWRITTEN WHEN PYMAKE SCAN IS USED!
#CHANGES TO THIS FILE WILL NOT CARRY OVER
set(\n\tSOURCE_FILES_SRC_FOLDER\n{x}\n)"""
SET_HEADER_STR = lambda x: f"""#PROJECT WAS CREATED WITH PYMAKE
#PYMAKE: https://github.com/EndMy5uffering/PyCmakeToolKit
#THIS FILE WILL BE OVERWRITTEN WHEN PYMAKE SCAN IS USED!
#CHANGES TO THIS FILE WILL NOT CARRY OVER
set(\n\tHEADER_FILES_INCLUDE_FOLDER\n{x}\n)"""

def generate_local_cmake(relative_parent: Path, src_path: Path, include_path: Path):
    cwd = os.getcwd()
    os.chdir(relative_parent)
    INFO(f'Looking for source files in ./{src_path}')
    src_list = [f.replace('\\', '/') for e in SRC_ENDINGS for f in glob("./src/" + e, recursive=True)]
    INFO('Found source files:')
    for f in src_list:
        INFO(f'\t{f}')
    src_list = '\n'.join(['\t' + f for f in src_list])
    INFO('-'*10)

    INFO(f'Looking for source files in ./{include_path}')
    header_list = [f.replace('\\', '/') for e in HEADER_ENDINGS for f in glob("./include" + e, recursive=True)]
    INFO('Found source files:')
    for f in header_list:
        INFO(f'\t{f}')
    header_list = '\n'.join(['\t' + f for f in header_list])
    INFO('-'*10)

    spstr = f"./src/local.cmake"
    with open(spstr, 'w+') as src_make_file:
        src_make_file.write(SET_SRC_STR(src_list))
        INFO(f'Written {spstr}')

    incstr = f"./include/local.cmake"
    with open(incstr, 'w+') as src_make_file:
        src_make_file.write(SET_HEADER_STR(header_list))
        INFO(f'Written {incstr}')
    os.chdir(cwd)
    INFO('All files written')