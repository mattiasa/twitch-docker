#! /bin/bash

set -e

url="$1"
filename="$2"

usage() {
    echo "Usage: <url> <filename>"
    exit 1
}

if [ "X$url" = "X" ]; then
   usage
fi

cd /videos

if [ "X$filename" = "X" ]; then
    filename=$(getfilename.py $url)
fi

streamlink -o $filename.ts $url best
ffmpeg -i $filename.ts media/$filename.mp4
podcast.py
