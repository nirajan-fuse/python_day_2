# Create a function search_log that takes a log file and a search keyword as input. The function should find and 
# display all lines containing the search keyword.

import logging

# logging.basicConfig(level=logging.DEBUG, filename='log.log', filemode='w',
#                         format='%(asctime)s - %(levelname)s - %(message)s')


# logging.info('Searching')
# logging.warning('The file is already in use!')
# logging.error('An error occurred!')

def search_log(log_file, keyword):
    try:
        with open(log_file, 'r') as file:
            for line in file:
                if keyword in line:
                    print(line)
    except FileNotFoundError:
        print('Error: File not found!')


search_log('log.log', 'WARNING')