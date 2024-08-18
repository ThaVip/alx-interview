#!/usr/bin/env python3
import sys
import signal

# Initialize variables
total_file_size = 0
status_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
line_count = 0

def print_stats():
    """Prints the accumulated statistics."""
    print(f"File size: {total_file_size}")
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print(f"{code}: {status_codes[code]}")

def handle_interrupt(signal, frame):
    """Handles the keyboard interrupt (CTRL + C)."""
    print_stats()
    sys.exit(0)

# Set up the signal handler for keyboard interrupt (CTRL + C)
signal.signal(signal.SIGINT, handle_interrupt)

# Process stdin line by line
for line in sys.stdin:
    try:
        # Parse the line
        parts = line.split()
        if len(parts) < 7:
            continue  # Skip lines that don't match the expected format

        ip_address = parts[0]
        date = parts[3] + ' ' + parts[4]
        request = parts[5] + ' ' + parts[6] + ' ' + parts[7]
        status_code = int(parts[-2])
        file_size = int(parts[-1])

        # Update the metrics
        total_file_size += file_size
        if status_code in status_codes:
            status_codes[status_code] += 1

        line_count += 1

        # Print statistics after every 10 lines
        if line_count % 10 == 0:
            print_stats()

    except Exception:
        continue  # Skip lines with errors

# Print final statistics if the input ends naturally
print_stats()

