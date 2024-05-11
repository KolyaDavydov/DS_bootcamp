#/bin/sh

INPUT_FILE="../ex02/hh_sorted.csv"

OUTPUT_FILE=hh_position.csv

cat $INPUT_FILE \
| head -n 1 \
> $OUTPUT_FILE

cat $INPUT_FILE \
| tail -n +2 \
| awk \
   'BEGIN{
      FS=","; OFS=",";
      Regexes[0] = "[Jj]unior\\+?/?";
      Regexes[1] = "[Mm]iddle\\+?/?";
      Regexes[2] = "[Ss]enior";
    }
    {
      result = "";
      for (i = 0; i < length(Regexes); ++i)
      {
        match($3, Regexes[i]);
        if (RLENGTH > 0) {
          first_char = substr($3, RSTART, 1);
          result = result toupper(first_char) substr($3, RSTART + 1, RLENGTH - 1);
        }
      }
      if (length(result) == 0) {
        $3 = "\"-\"";
      }
      else {
        $3 = "\"" result "\"";
      }
      
      print;
    }' \
>> $OUTPUT_FILE