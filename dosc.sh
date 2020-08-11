#!/bin/bash
a=0
for filename in /home/tof/hash/fundacionmustakis/*.jpg; do
    python mosaic.py "$filename" "/home/tof/hash/fundacionmustakis/new/" "$filename"
    let "a += 1"
    if [ "$a" -gt "200" ];then
    	break
    fi
done
