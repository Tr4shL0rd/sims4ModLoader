#!/usr/bin/env python
import os
import sys
import shutil
import zipfile
import os.path
from pyunpack import Archive

DEBUG = False
PATH = os.getcwd()
FOLDERS = "/home/tr4shl0rd/autoUnzipper/folders/"
if DEBUG:
    EXTRACT_PATH = "/home/tr4shl0rd/autoUnzipper/extract"
else:
    EXTRACT_PATH = "/home/tr4shl0rd/Games/origin/dosdevices/c:/users/tr4shl0rd/Documents/Electronic Arts/The Sims 4/Mods"
latesFile = []
normal = '\033[39m'
success = "EXTRACTED"
check = '\033[32m' + "✓"
info = '\033[33m' + "!"
warning = '\033[31m' + "X"
SupportedExts = [".package","e","zip","rar"]

try:
    def main():
        # unzips the folders
        FILES = os.listdir(FOLDERS)
        for i in FILES:
            FILES = FOLDERS + i
            # unzips .zip files
            if FILES[-1] == "p":
                with zipfile.ZipFile(FILES, "r") as zip_ref:
                    latesFile.append(FILES)
                    zip_ref.extractall(EXTRACT_PATH)
                    print("{} {}{} {}".format(check, normal, success, FILES))
            # unzips .rar files
            if FILES[-1] == "r":
                latesFile.append(FILES)
                Archive(FILES).extractall(EXTRACT_PATH)
                print("{} {}{} {}".format(check, normal, success, FILES))
            # moves .package files
            if ".package" in FILES:
                latesFile.append(FILES)
                shutil.move(FILES, EXTRACT_PATH)
                print("{} {}MOVED     {}".format(check, normal, FILES))

        # Empties the used folders
        for path, subdirs, files in os.walk(EXTRACT_PATH):
            for name in files:
                checkPatch = path
                x = os.path.join(path, name)
                if os.path.isdir(checkPatch) == True and "package" in os.path.join(path, name) and x.count("/") == 14 and os.path.isfile(x) == False:
                    shutil.move(x, EXTRACT_PATH)


        # Deletes the used folders
        #for P, s, f in os.walk(EXTRACT_PATH):
        #    if len(P) > 100:
        #        os.removedirs(P)

        if DEBUG:
            for path, subdirs, files in os.walk(EXTRACT_PATH):
                for name in files:
                    x = os.path.join(path, name)
                    shutil.move(x, FOLDERS)

        print("FILES AT {}".format(EXTRACT_PATH))
    main()
except FileNotFoundError:
    print("FILE NOT FOUND!\n{}".format(FOLDERS))
