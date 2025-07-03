# ==============================
# 1. Sample Logs
# Simulated server log entries with different formats
# ==============================
logs = {
    "server": [
        "[2023-10-05 14:30:45] [INFO] User 'admin' logged in from 192.168.1.1",
        "[2023-10-05 14:32:12] [ERROR] Database connection failed: Timeout",
        "[2023-10-05 14:35:01] [WARNING] Disk usage at 92%",
        "[2023-10-05 14:36:45] [DEBUG] Memory usage: 75%",
        "[2023-10-05 14:38:30] [INFO] User 'guest' logged out"
    ],
    "financial": [
        "[2023-10-05 14:31:22] [TRANSACTION] ID: TXN1001 | Amount: $1,234.56 | Status: Success",
        "[2023-10-05 14:33:15] [WITHDRAWAL] Account: 1234567890 | Amount: $500.00 | Location: ATM_001"
    ],
    "error": [
        "[2023-10-05 14:34:55] [CRITICAL] Failed to load module: network_module.dll",
        "[2023-10-05 14:37:22] [ERROR] Connection refused: 127.0.0.1:8080"
    ]
}

# ==============================
# 2. Log Parser Functions
# ==============================
def parse_server_log(log_entry):
    """Parse timestamp, level, and message from server log"""
    # Format: "[YYYY-MM-DD HH:MM:SS] [LEVEL] Message"
    timestamp = log_entry[1:20]  # Positive index slicing
    level = log_entry[22:26]     # Fixed length for level
    message = log_entry[28:]     # Slice to end
    
    return {
        "timestamp": timestamp,
        "level": level,
        "message": message
    }

def parse_financial_log(log_entry):
    """Parse financial log with field-based slicing"""
    # Format: "[timestamp] [type] ID: ... | Amount: $... | Status: ..."
    timestamp = log_entry[1:20]
    log_type = log_entry[22:31]
    
    # Extract amount with negative indexing
    amount_start = log_entry.index("$")
    amount_end = log_entry.index(" |", amount_start)
    amount = log_entry[amount_start:amount_end]
    
    return {
        "timestamp": timestamp,
        "type": log_type,
        "amount": amount
    }

def parse_error_log(log_entry):
    """Use negative indexing to extract error code"""
    # Format: "[timestamp] [level] Failed to load module: filename.dll"
    error_code = log_entry[-12:-4]  # Last module name before .dll
    level = log_entry[22:30]
    return {
        "error_code": error_code,
        "level": level
    }

# ==============================
# 3. Advanced Slicing Techniques
# ==============================
def reverse_string(text):
    """Reverse string using step=-1"""
    return text[::-1]

def every_second_char(text):
    """Get every second character using step=2"""
    return text[::2]

def extract_ip_address(log_entry):
    """Extract IP address using dynamic slicing"""
    start = log_entry.find("from ") + 3
    end = log_entry.find(" ", start)
    return log_entry[start:end]

# ==============================
# 4. Main Program
# ==============================
def main():
    print("=== Server Log Parser with String Slicing ===\n")
    
    print("1. Basic Server Log Parsing")
    server_log = logs["server"][0]
    parsed = parse_server_log(server_log)
    print("Timestamp:", parsed["timestamp"])
    print("Level:", parsed["level"])
    print("Message:", parsed["message"])
    print()
    
    print("2. Financial Log Parsing with Dynamic Slicing")
    fin_log = logs["financial"][0]
    parsed = parse_financial_log(fin_log)
    print("Timestamp:", parsed["timestamp"])
    print("Type:", parsed["type"])
    print("Amount:", parsed["amount"])
    print()
    
    print("3. Error Log with Negative Indexing")
    err_log = logs["error"][0]
    parsed = parse_error_log(err_log)
    print("Error Code:", parsed["error_code"])
    print("Level:", parsed["level"])
    print()
    
    print("4. Advanced Slicing Techniques")
    text = "Python Programming"
    print("Original:", text)
    print("Reversed:", reverse_string(text))
    print("Every Second Character:", every_second_char(text))
    print()
    
    print("5. IP Address Extraction")
    ip = extract_ip_address(logs["server"][0])
    print("Extracted IP:", ip)

# ==============================
# 6. Run the Program
# ==============================
if __name__ == "__main__":
    main()