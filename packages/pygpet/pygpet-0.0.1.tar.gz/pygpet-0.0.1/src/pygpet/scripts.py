import json
from datetime import datetime
from pathlib import Path

DEFAULT_OUTPUT_DIR = "./output"
DEFAULT_OUTPUT_FILE = "log.txt"
DEFAULT_WRITE_FLAG = True


def sep(message="", 
        separator="-", 
        repeat=60,  
        fixed_date_time=datetime.now().strftime("%F %X"),
        write_flag=DEFAULT_WRITE_FLAG,
        write_dir=DEFAULT_OUTPUT_DIR,
        write_filename=DEFAULT_OUTPUT_FILE) -> str:
    """Prints a separator."""
    if message != "":
        content = f'[{fixed_date_time}] {(separator * int(repeat / 2))}  {message}  {(separator * int(repeat / 2))}'
    else:
        content = f'[{fixed_date_time}] {(separator * repeat)}'
    print(content)
    if not write_flag:
        write(content, output_dir=write_dir, file_name=write_filename)
    return content


def p(param, 
        fixed_date_time=datetime.now().strftime("%F %X"),
        write_flag=DEFAULT_WRITE_FLAG,
        write_dir=DEFAULT_OUTPUT_DIR,
        write_filename=DEFAULT_OUTPUT_FILE) -> str:
    """ Return the message (param). 
        Convert the 'param' in a formated string if it is a 'dict' """

    message = f'[{fixed_date_time}] {param}' 

    if param.__class__.__name__ == 'dict':
        message = f'[{fixed_date_time}] {json.dumps(param, indent=4, default=str)}'

    if write_flag:
        write(message, output_dir=write_dir, file_name=write_filename)

    return message



def write(message,
        output_dir=DEFAULT_OUTPUT_DIR,
        file_name=DEFAULT_OUTPUT_FILE):
    """Writes the content in the 'file_name'"""

    try:
        path = Path(output_dir)
        path.mkdir(parents=True, exist_ok=True)

        file = open(f'{output_dir}/{file_name}','a+')
        file.write(f'{message}\n')
        file.close()
    except:
        print(f'>> [ERROR] Error writing log file. Check the \'output\' directory.')




