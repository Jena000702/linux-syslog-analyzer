#!/bin/bash

LOG_FILE="/var/log/syslog"

if [ -z "$1" ]; then
    echo "Usage: ./parse_logs.sh <search_term>"
    exit 1
fi

SEARCH_TERM="$1"
OUTPUT_FILE="search_${SEARCH_TERM}_$(date +%Y%m%d_%H%M%S).txt"

echo "=========================================="
echo "      ANALYZING SYSLOG FOR: $SEARCH_TERM  "
echo "=========================================="

echo -e "\n[+] Total Occurrences: $(grep -ic "$SEARCH_TERM" "$LOG_FILE")"

echo -e "\n[+] TOP 5 PROCESSES GENERATING THIS LOG:"
echo "------------------------------------------"
grep -i "$SEARCH_TERM" "$LOG_FILE" | awk '{print $5}' | sort | uniq -c | sort -nr | head -n 5

grep -i "$SEARCH_TERM" "$LOG_FILE" > "$OUTPUT_FILE"

echo -e "\n=========================================="
echo " Full output saved to: $OUTPUT_FILE"
echo "=========================================="

