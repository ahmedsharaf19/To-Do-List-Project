import json
import datetime as dt
import os

#########################################################################
def clear_cli():
  """
    Clear Console 
  """
  os.system('cls') if os.name == 'nt' else os.system('clear')

def convert_to_time(date_string):
  """
    Converts a date string to a datetime object.
    Args:
        date_string (str): A string representing a date in the format "m/d/Y".
    Returns:
        datetime.date: A datetime object representing the input date.
  """
  # 1/2/2024   1-2-2024   
  # To Find Seperator Between Date
  symp = '-'
  for x in date_string:
    if x.isdigit():
      continue
    symp = x
    break
  
  # Convert String To datetime
  convertd = dt.datetime.strptime(date_string,f"%d{symp}%m{symp}%Y").date()

  return convertd

def write_json(data, path):
    """
    Write data to a JSON file with datetime objects serialized as ISO format strings.
    
    Args:
        data: The data to be written to the JSON file.
    """
    # Open the file in write mode with UTF-8 encoding
    with open(path, 'w', encoding='utf-8') as file:
        # Dump the data to the file in JSON format
        json.dump(data, file)


def read_json(path):
    """
    Read data from a JSON file.

    Args:
        path (str): Path to the JSON file.

    Returns:
        list: Data read from the JSON file.
    """
    # Open the file in read mode with UTF-8 encoding
    with open(path, 'r', encoding='utf-8') as file:
        # Get the length of the file
        x = len(file.read())
        
        # If the file is empty, return an empty list
        if x == 0:
            return []
        
        # Reset the file pointer to the beginning
        file.seek(0)
        
        # Load the data from the file
        data = json.load(file)
    
    return data
