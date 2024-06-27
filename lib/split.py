import sys

name = sys.argv[1]

src = f'{name}.mp3'
dst_dir = f'{name}/'
# separate each 6 seconds into a wav file

import os
import subprocess

if not os.path.exists(src):
    print(f'File {src} not found')
    sys.exit(1)

if not os.path.exists(dst_dir):
    os.makedirs(dst_dir)

subprocess.run(['ffmpeg', '-i', src, '-f', 'segment', '-segment_time', '6', '-c', 'copy', f'{dst_dir}%03d.wav'])

