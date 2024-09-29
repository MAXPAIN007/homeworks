import re
from datetime import datetime


def analyze_heartbeat_log(input_file, output_file, key):
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        previous_time = None
        previous_line = None

        for line in infile:
            if key in line:
                timestamp_match = re.search(r'Timestamp (\d{2}:\d{2}:\d{2})', line)
                if timestamp_match:
                    current_time_str = timestamp_match.group(1)
                    current_time = datetime.strptime(current_time_str, '%H:%M:%S')

                    if previous_time:
                        time_diff = (previous_time - current_time).total_seconds()

                        if 31 < time_diff < 33:
                            # WARNING
                            outfile.write(f'WARNING: Heartbeat {time_diff:.0f} seconds at {previous_time_str} - {current_time_str}\n')
                        elif time_diff >= 33:
                            # ERROR
                            outfile.write(f'ERROR: Heartbeat {time_diff:.0f} seconds at {previous_time_str} - {current_time_str}\n')

                    previous_time = current_time
                    previous_line = line
                    previous_time_str = current_time_str

input_log_file = 'hblog.txt'
output_log_file = 'my_hb_test.log'

key_to_filter = 'TSTFEED0300|7E3E|0400'

analyze_heartbeat_log(input_log_file, output_log_file, key_to_filter)

print(f"Логування завершено. Результати записані у {output_log_file}")
