Wireless Access Point Monitoring System
This project demonstrates communication between two Python applications for monitoring and displaying changes in wireless access point information.

Components

app_a.py: Monitors a JSON file containing access point data and sends updates via sockets
app_b.py: Receives updates from app_a.py and displays changes in a user-friendly format.
Dependencies

Python 3.9 or above
Installation

Make sure you have Python 3.9 or above installed.
Install any required packages:
Bash
pip install -r requirements.txt 
Use code with caution.
Usage

Create the JSON data file:

Place a JSON file named access_points in the /tmp directory (or modify the WATCH_FILE constant in app_a.py to your desired location).
The file should follow the format described in the coding exercise instructions.
Start the file monitor (app_a.py):

Bash
python app_a.py
Use code with caution.
Start one or more display clients (app_b.py):

Bash
python app_b.py
Use code with caution.
You can start multiple instances of app_b.py, potentially on different machines, to receive updates.

Testing

Modify the contents of the /tmp/access_points file.
Observe the changes displayed in the terminal(s) running app_b.py.
Notes

The HOST and PORT variables in both app_a.py and app_b.py can be modified if you need to run the applications on different machines or change the communication port.
The file monitoring interval in app_a.py can be adjusted as needed.
Example Output

MyAP's SNR has changed from 63 to 82
YourAP's channel has changed from 1 to 6
HisAP is removed from the list
HerAP is added to the list with SNR 71 and channel 1