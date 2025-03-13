import json
from datetime import datetime

def write_log(data, filename="logs/honeypot_log.json"):
    """
    Ghi dữ liệu vào file log dưới dạng JSON.

    Args:
        data (dict): Dữ liệu cần ghi vào log.
        filename (str): Đường dẫn tới file log.
    """
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    data['timestamp'] = timestamp
    
    try:
        with open(filename, 'a') as f:
            json.dump(data, f)
            f.write('\n')
    except Exception as e:
        print(f"Error writing to log: {e}")

if __name__ == "__main__":
    sample_data = {"event": "test_connection", "source_ip": "192.168.1.1"}
    write_log(sample_data) 
