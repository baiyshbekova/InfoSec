#!/bin/bash

directory=$1

if [ ! -d "$directory" ]; then
    echo "Directory not found: $directory"
    exit 1
fi

find "$directory" -type f -empty -print -delete
