# lib/generate_log.py

from datetime import datetime

def generate_log(log_data):
    """
    Generate a log file with today's date in the filename.
    
    Args:
        log_data: A list of strings to write to the log file.
        
    Returns:
        str: The filename of the created log file.
        
    Raises:
        ValueError: If log_data is not a list.
    """
    if not isinstance(log_data, list):
        raise ValueError("Input must be a list")
    
    # Generate filename with today's date
    today = datetime.now().strftime("%Y%m%d")
    filename = f"log_{today}.txt"
    
    # Write log data to file
    with open(filename, "w") as file:
        for entry in log_data:
            file.write(f"{entry}\n")
    
    return filename