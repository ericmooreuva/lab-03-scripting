#!/bin/bash
set -euo pipefail

curl -o lab3-bundle.tar.gz "https://s3.amazonaws.com/ds2002-resources/labs/lab3-bundle.tar.gz"

tar -xzf lab3-bundle.tar.gz

# tr can squeeze repeated newlines
cat lab3_data.tsv | tr -s '\n' > cleaned.tsv

tr '\t'  ',' < cleaned.tsv > cleaned.csv

COUNTS=$(($(wc -l < cleaned.csv) -1))
echo "Number of data rows: $COUNTS"

tar -czf converted-archive-tar.gz cleaned.csv
