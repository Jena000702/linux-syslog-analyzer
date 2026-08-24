# Linux Syslog Analyzer & Telemetry Parser

A dual-tool set (Bash & Python) designed to parse Linux system logs (`/var/log/syslog`), extract critical security events, group offending processes, and export telemetry into structured JSON reports.

## Features
- **Bash Script (`parse_logs.sh`)**: Fast CLI log searching using `grep`, `awk`, `sort`, and `uniq` with dynamic argument passing.
- **Python Parser (`parse_logs.py`)**: Uses Regular Expressions (`re`) to parse log headers and exports structured telemetry reports as `.json` files.
- **Error Handling**: Validates positional parameters and ensures target log file existence before processing.

## Usage

### 1. Bash Parser
```bash
chmod +x parse_logs.sh
./parse_logs.sh <search_term>
# Example: ./parse_logs.sh kernel
```

### 2. Python Analyzer & JSON Exporter
```bash
python3 parse_logs.py <search_term>
# Example: python3 parse_logs.py error
```

## Sample JSON Output
```json
{
    "search_term": "error",
    "total_matches": 49,
    "top_processes": {
        "kernel": 22,
        "systemd[1]": 14
    }
}
```
