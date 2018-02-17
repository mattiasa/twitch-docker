#! /bin/bash

set -e

url="$1"
filename="$2"

usage() {
    echo "Usage: <url> <filename>"
    exit 1
}

if [ "X$filename" = "X" -o "X$url" = "X" ]; then
   usage
fi

cd /videos

filename=$(getfilename.py $url)

streamlink -o $filename.ts $url best
ffmpeg -i $filename.ts media/$filename.mp4
./podcast.py
