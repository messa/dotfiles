#!/usr/bin/env python3

from datetime import datetime
import os
import sys
from os.path import abspath, dirname, exists, islink, relpath
from os.path import join as path_join

def main():
    srcDir = dirname(dirname(abspath(__file__)))
    targetDir = os.getenv("HOME")

    def ln(srcName, targetName):
        srcPath = path_join(srcDir, srcName)
        targetPath = path_join(targetDir, targetName)
        relSrcPath = relpath(srcPath, start=dirname(targetPath))
        if not exists(srcPath):
            print("Error: file %s does not exist" % (srcPath), file=sys.stderr)
            return
        if exists(targetPath):
            if islink(targetPath) and os.readlink(targetPath) == relSrcPath:
                print("Symbolic link %s => %s already exists" % (targetPath, srcPath))
                return
            dt = datetime.now().strftime("%Y%m%d")
            targetBackupPath = "%s.backup-%s" % (targetPath, dt)
            if exists(targetBackupPath):
                print("Error: backup file %s already exists" % (targetBackupPath), file=sys.stderr)
                return
            print("Moving %s to %s" % (targetPath, targetBackupPath))
            os.rename(targetPath, targetBackupPath)

        print("Creating symbolic link %s => %s" % (targetPath, relSrcPath))
        os.symlink(relSrcPath, targetPath)


    ln("bashrc",    ".bashrc")
    ln("gtkrc-2.0", ".gtkrc-2.0")
    ln("vimrc",     ".vimrc")

if __name__ == "__main__":
    main()


