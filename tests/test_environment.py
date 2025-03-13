import socket
import threading
import json

print("Python environment is ready!")

try:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("Socket library is working correctly.")
    
    thread = threading.Thread(target=lambda: None)
    thread.start()
    print("Threading library is working correctly.")
    
    sample_data = {"test": "success"}
    json.dumps(sample_data)
    print("JSON library is working correctly.")
    
    print("All libraries are functioning properly!")

except Exception as e:
    print(f"Error in environment setup: {e}")