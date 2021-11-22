
ls -l *.clj | awk '{split($NF,res,".");print res[1]}' | sort -n
