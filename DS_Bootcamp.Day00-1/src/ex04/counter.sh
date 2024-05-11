#/bin/sh

INPUT_FILE="../ex03/hh_position.csv"

OUTPUT_FILE="hh_uniq_position.csv"

echo "name","count" > $OUTPUT_FILE

cat $INPUT_FILE \
	| awk 'BEGIN{FS=OFS=",";} NR>1 {print $3;}' \
	| sort \
	| uniq -c \
	| awk 'BEGIN{OFS=","} {print $2, $1;}' \
	>> $OUTPUT_FILE