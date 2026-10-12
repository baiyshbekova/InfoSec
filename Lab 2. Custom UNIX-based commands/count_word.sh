#!/bin/bash

file_name=$1
word=$2

if [ ! -f "$file_name" ]; then
    echo "File not found: $file_name"
    exit 1
fi

count=$(grep -o -iw "$word" "$file_name" | wc -l)

echo "The word '$word' appears $count times."
