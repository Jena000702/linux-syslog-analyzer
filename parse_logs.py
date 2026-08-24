#!/usr/bin/env python3
import sys
import os
import re
import json
from collections import Counter
from datetime import datetime

LOG_FILE = "/var/log/syslog"

if len(sys.argv) < 2:
    print("Usage: python3 parse_logs.py <search_term>")
    sys.exit(1)

search_term = sys.argv[1].lower()
base_name = f"py_search_{search_term}_{datetime.now().strftime('%Y%m%d_%H%M%S')}"

if not os.path.exists(LOG_FILE):
    print(f"Error: Log file {LOG_FILE} not found!")
    sys.exit(1)

matches = []
process_counter = Counter()

# Improved regex: Skip the initial timestamp and grab the hostname + process name
log_pattern = re.compile(r'^\S+\s+\S+\s+([a-zA-Z0-9_\-\.\/]+(?:\[\d+\])?):')

with open(LOG_FILE, "r", encoding="utf-8", errors="ignore") as f:
    for line in f:
        if search_term in line.lower():
            clean_line = line.strip()
            matches.append(clean_line)
            
            # Extract actual process name
            match = log_pattern.search(clean_line)
            if match:
                process_counter[match.group(1)] += 1

# Output terminal metrics
print("==========================================")
print(f"   PYTHON LOG ANALYZER: '{search_term}'")
print("==========================================")
print(f"\n[+] Total Occurrences Found: {len(matches)}")

print("\n[+] Top 5 Processes Causing This Log:")
print("------------------------------------------")
for proc, count in process_counter.most_common(5):
    print(f"  {count:5d}  {proc}")

# Save structured report as JSON
json_data = {
    "search_term": search_term,
    "timestamp": str(datetime.now()),
    "total_matches": len(matches),
    "top_processes": dict(process_counter.most_common(5)),
    "raw_logs": matches[:50] # First 50 logs sample
}

json_file = f"{base_name}.json"
with open(json_file, "w") as jf:
    json.dump(json_data, jf, indent=4)

print("\n==========================================")
print(f" Structured JSON Report Saved: {json_file}")
print("==========================================")
