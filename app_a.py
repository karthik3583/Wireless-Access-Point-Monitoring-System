import json
import time
import socketserver

WATCH_FILE = "/tmp/access_points"
HOST, PORT = "localhost", 9999  # Customize if needed

class FileChangeHandler(socketserver.BaseRequestHandler):
    def handle(self):
        old_data = None
        while True:
            with open(WATCH_FILE, "r") as f:
                new_data = json.load(f)

            if old_data != new_data:
                self.send_changes(old_data, new_data)
                old_data = new_data

            time.sleep(2)  # Adjust polling interval as needed

    def send_changes(self, old_data, new_data):
        changes = []
        old_aps = {ap['ssid']: ap for ap in old_data.get('access_points', [])}
        new_aps = {ap['ssid']: ap for ap in new_data.get('access_points', [])}

        for ssid in set(old_aps) | set(new_aps):
            if ssid in old_aps and ssid in new_aps:
                if old_aps[ssid]['snr'] != new_aps[ssid]['snr']:
                    changes.append({'type': 'snr_change', 'ssid': ssid, 'old_snr': old_aps[ssid]['snr'], 'new_snr': new_aps[ssid]['snr']})
                if old_aps[ssid]['channel'] != new_aps[ssid]['channel']:
                    changes.append({'type': 'channel_change', 'ssid': ssid, 'old_channel': old_aps[ssid]['channel'], 'new_channel': new_aps[ssid]['channel']})
            elif ssid in old_aps:
                changes.append({'type': 'removed', 'ssid': ssid})
            else:
                changes.append({'type': 'added', 'ssid': ssid, 'snr': new_aps[ssid]['snr'], 'channel': new_aps[ssid]['channel']})

        if changes:
            self.request.sendall(json.dumps(changes).encode())    

if __name__ == "__main__":
    with socketserver.TCPServer((HOST, PORT), FileChangeHandler) as server:
        server.serve_forever()