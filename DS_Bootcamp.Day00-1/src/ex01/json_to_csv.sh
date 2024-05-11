#!/bin/sh

INPUT_FILE="../ex00/hh.json"

jq -rf filter.jq $INPUT_FILE > hh.csv