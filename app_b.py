import socket

HOST, PORT = "localhost", 9999  

def process_changes(changes):
    for change in changes:
        if change['type'] == 'snr_change':
            print(f"{change['ssid']}'s SNR has changed from {change['old_snr']} to {change['new_snr']}")
        elif change['type'] == 'channel_change':
            print(f"{change['ssid']}'s channel has changed from {change['old_channel']} to {change['new_channel']}")
        elif change['type'] == 'added':
            print(f"{change['ssid']} is added to the list with SNR {change['snr']} and channel {change['channel']}")
        elif change['type'] == 'removed':
            print(f"{change['ssid']} is removed from the list")

if __name__ == "__main__":
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect((HOST, PORT))
        while True:
            data = sock.recv(1024).decode()
            if data:
                changes = json.loads(data)
                process_changes(changes)