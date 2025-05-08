#Log File Analyzer (Python3)

A simple, command-line tool to analyze log files for errors, warnings,
and informational messages.It provides summary statistics, a visual chart,
and generates a plain-text report.

---

##Feature

- Parses logs with timestamp, log level, and message
- Counts occurrences of `INFO`, `WARNING`, and `ERROR`
- Filters logs by optional date/time range
- Outputs a clean summary report (`.txt`)
- Displays a bar chart of log levels
- Lightweight and easy to modify for any log format

---

##Example Log Format

2025-05-07 10:16:01 WARNING Disk space low on /dev/sda1
2025-05-07 10:16:22 ERROR Failed to connect to database
2025-05-07 10:17:03 INFO Scheduled backup completed



---

##Installation

1. Clone this repo:
   ```bash
   git clone https://github.com/yourusername/log-file-analyzer.git
   cd log-file-analyzer
2. Install required packages:
    $ pip install matplotlib
3. example command to use:
    python log_analyzer.py --log sample.log --start "2025-05-07 10:16" --end "2025-05-07 10:19" --report output.txt
4.

| Flag       | Description                                  |
| ---------- | -------------------------------------------- |
| `--log`    | Path to the log file (required)              |
| `--start`  | Start time (format: `YYYY-MM-DD HH:MM`)      |
| `--end`    | End time (format: `YYYY-MM-DD HH:MM`)        |
| `--report` | Output file name (default: `log_report.txt`) |

5. Output:
    -A  .txt report with:
        -log counts
        -time range of entries
        -top error/warning messages
6. Customize:
    -Modify the log_pattern regex in log_analyzer.py to match your own log format.
    -Add support for more log levels or advanced filters
        (ie, keyword search, export to CSV)
7. Example Output:

    Log Analysis Report
=====================

Total log entries: 7
INFO: 3
WARNING: 2
ERROR: 2

Time Range
Start: 2025-05-07 10:15:32
End:   2025-05-07 10:20:55

Top Error/Warning Messages:
[1x] Disk space low on /dev/sda1
[1x] Failed to connect to database
...
