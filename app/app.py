import logging
import re
from datetime import datetime

var_log_file_path = '/Users/adeoke/Documents/mocking_example/app.log'

logging.basicConfig(level=logging.INFO,
                    filename=var_log_file_path,
                    filemode='w',
                    format="%(asctime)-15s %(funcName)s:")


def was_i_called(time_in_seconds_ago):
    logging.info("I've been called")
    return get_last_called_function_time('was_i_called', time_in_seconds_ago)


def get_last_called_function_time(function_name, seconds_ago,
                                  log_file_path=var_log_file_path):
    lines_with_method_call = []

    with open(log_file_path, "r") as file:
        for line in file:
            if function_name in line:
                lines_with_method_call.append(line)

    if lines_with_method_call:
        match = re.search(r'(\d{2}:\d{2}:\d{2})',
                          lines_with_method_call[-1]).groups()
        original_time = datetime.strptime(match[0], '%H:%M:%S')

        time_now = datetime.now().strftime("%H:%M:%S")
        current_time_obj = datetime.strptime(time_now, '%H:%M:%S')

        delta = current_time_obj - original_time
        if delta.seconds < seconds_ago:
            print('method was called within the time frame')
            return True
        else:
            print('No method was not called in the time frame')
            return False
    else:
        return 'No log for the method {} in time frame {} seconds'.format(
            function_name, seconds_ago)



