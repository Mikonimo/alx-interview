#!/usr/bin/python3
"""This module contains a function about log parsing"""

import sys

# Initialize metrics
total_file_size = 0
status_codes_count = {
    "200": 0,
    "301": 0,
    "400": 0,
    "401": 0,
    "403": 0,
    "404": 0,
    "405": 0,
    "500": 0
}
valid_status_codes = set(status_codes_count.keys())
line_count = 0


def print_metrics():
    """Prints the collected metrics."""
    print(f"File size: {total_file_size}")
    for code in sorted(status_codes_count.keys()):
        if status_codes_count[code] > 0:
            print(f"{code}: {status_codes_count[code]}")


try:
    for line in sys.stdin:
        line_count += 1
        parts = line.split()

        # Check the expected format
        if len(parts) >= 7:
            # Extract <status code> and <file size>
            status_code = parts[-2]
            file_size = parts[-1]

            # Update total file size
            try:
                total_file_size += int(file_size)
            except ValueError:
                continue

            # Update status code count if valid
            if status_code in valid_status_codes:
                status_codes_count[status_code] += 1

        # Print metrics after every 10 lines
        if line_count % 10 == 0:
            print_metrics()

except KeyboardInterrupt:
    # Print metrics on KeyboardInterrupt (CTRL + C)
    print_metrics()
    raise

# Final print after reading all lines
print_metrics()
