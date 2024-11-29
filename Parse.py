#Open and read file
def parse_usb_logs(file_path):
    with open(file_path, 'r') as file:
        logs = file.readlines()
    
    extracted_logs = []
    for line in logs:
        fields = extract_fields(line.strip())
        extracted_logs.append(fields)
    
    return extracted_logs

#Extract specific fields from a log line
def extract_fields(log_line):
    fields = {}
    parts = log_line.split()
    fields['timestamp'] = ' '.join(parts[0:2])
    
    if "VID" in log_line and "PID" in log_line:
        vid_pid = log_line.split(':')[-1].strip()
        fields['deviceID'] = vid_pid
    
    if "connected" in log_line:
        fields['action'] = "connedted"
    elif "disconnected" in log_line:
        fields['action'] = "disconnected"
    elif "error" in log_line:
        fields['action'] = "error"

    return fields

#Main func
if __name__ == "__main__":
    file_path = "logs.txt"
    extracted_logs = parse_usb_logs(file_path)

    if extracted_logs:
        print("Žurnālfaili:")
        for log in extracted_logs:
            print(log)
    else:
        print("Nav parsēti žurnālfaili")