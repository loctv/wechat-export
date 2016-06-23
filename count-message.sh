#!/bin/bash -e
# File: count-message.sh
# Date: Sun Apr 12 21:01:01 2015 +0900
# Author: Kangjing Huang <huangkangjing@gmail.com>


if [[ -z $1 ]]
then
    echo "Usage: $0 [Directory of text messages]"
    exit 1
fi
# TODO work on db directly

echo -e "Filename\tCounts of message\tCounts of chars\tCounts of words"

SAVEIFS=$IFS
IFS=$(echo -en "\n\b")

for i in "$1"/*.txt
do
    echo -en "$i\t"
    LINECOUNT=$(cat "$i"| wc -l )
    CHARCOUNT=$(cat "$i"| sed 's/.*:[0-9][0-9]:\(.*\)/\1/g'  | sed 's/\[.*\]//g'  | grep  -v img | wc -m)
    WORDCOUNT=$(cat "$i"| sed 's/.*:[0-9][0-9]:\(.*\)/\1/g'  | sed 's/\[.*\]//g'  | grep  -v img | wc -w)
    echo -e "$LINECOUNT\t$CHARCOUNT\t$WORDCOUNT"
done

IFS=$SAVEIFS
