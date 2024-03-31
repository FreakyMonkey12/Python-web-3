import asyncio
import json
import datetime
from aiohttp im
import os
import shutil
import argparse
from concurrent.futures import ThreadPoolExecutor

def copy_files(source_dir, dest_dir):
    for root, _, files in os.walk(source_dir):
        for file in files:
            source_file_path = os.path.join(root, file)
            extension = os.path.splitext(file)[1][1:]
            dest_subdir = os.path.join(dest_dir, extension)
            os.makedirs(dest_subdir, exist_ok=True)
            shutil.copy(source_file_path, dest_subdir)

def main():
    parser = argparse.ArgumentParser(description="Copy files from source directory to destination directory sorted by extensions.")
    parser.add_argument("source_dir", help="Path to source directory.")
    parser.add_argument("dest_dir", nargs="?", default="dist", help="Path to destination directory. Default is 'dist'.")
    args = parser.parse_args()

    source_dir = args.source_dir
    dest_dir = args.dest_dir

    with ThreadPoolExecutor() as executor:
        executor.submit(copy_files, source_dir, dest_dir)

if __name__ == "__main__":
    main()
