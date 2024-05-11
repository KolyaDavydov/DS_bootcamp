#!/bin/sh

INPUT_FILE="../ex01/hh.csv"
OUTPUT_FILE="hh_sorted.csv"

cat $INPUT_FILE | head -n 1 > $OUTPUT_FILE
cat $INPUT_FILE | tail -n 20 | sort --field-separator="," -k 2 -k 1 >> $OUTPUT_FILE