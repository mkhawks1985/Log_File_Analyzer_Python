import re
import argparse
from collections import Counter
import matplotlib.pyplot as plt
from datetime import datetime

def parse_log(file_path, start_date=None, end_date=None):
    log_pattern = re.compile(r"(?P<timestamp>\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) (?P<level>\w+) (?P<message>.+)")

    log_levels = Counter()
    messages = Counter()
    timestamps = []

    with open(file_path, 'r') as f:
        for line in f:
            match = log_pattern.match(line)
            if match:
                timestamp = datetime.strptime(match.group("timestamp"), "%Y-%m-%d %H:%M:%S")
                level = match.group("level")
                message = match.group("message")

                if start_date and timestamp < start_date:
                    continue
                if end_date and timestamp > end_date:
                    continue

                log_levels[level] += 1
                timestamps.append(timestamp)
                if level in ["ERROR", "WARNING"]:
                    messages[message] += 1

    return log_levels, messages, timestamps

def write_report(log_levels, messages, timestamps, output_file):
    with open(output_file, 'w') as f:
        f.write("Log Analysis Report\n")
        f.write("=====================\n\n")
        f.write(f"Total log entries: {sum(log_levels.values())}\n")
        for level, count in log_levels.items():
            f.write(f"{level}: {count}\n")

        f.write("\nTime Range\n")
        if timestamps:
            f.write(f"Start: {min(timestamps)}\n")
            f.write(f"End:   {max(timestamps)}\n")

        f.write("\nTop Error/Warning Messages:\n")
        for msg, count in messages.most_common(5):
            f.write(f"[{count}x] {msg}\n")

def plot_summary(log_levels):
    labels = list(log_levels.keys())
    values = list(log_levels.values())

    plt.bar(labels, values, color=['green', 'orange', 'red'])
    plt.title("Log Level Summary")
    plt.xlabel("Log Level")
    plt.ylabel("Count")
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.show()

def parse_args():
    parser = argparse.ArgumentParser(description="Analyze log files for errors, warnings, and generate a report.")
    parser.add_argument('--log', type=str, required=True, help='Path to the log file')
    parser.add_argument('--start', type=str, help='Start time (YYYY-MM-DD HH:MM)')
    parser.add_argument('--end', type=str, help='End time (YYYY-MM-DD HH:MM)')
    parser.add_argument('--report', type=str, default='log_report.txt', help='Output report file')
    return parser.parse_args()

if __name__ == "__main__":
    args = parse_args()

    start = datetime.strptime(args.start, "%Y-%m-%d %H:%M") if args.start else None
    end = datetime.strptime(args.end, "%Y-%m-%d %H:%M") if args.end else None

    log_levels, messages, timestamps = parse_log(args.log, start, end)

    print("Log Summary:", log_levels)
    write_report(log_levels, messages, timestamps, args.report)
    print(f" Report saved to: {args.report}")

    plot_summary(log_levels)
