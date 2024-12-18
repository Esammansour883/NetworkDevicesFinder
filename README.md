# Network Scanner

A Python script to scan a network and list all connected devices with their IP and MAC addresses. This tool is useful for network administration, testing, and security assessments.

## Features

- **Network Scanning**: Scan a specified IP address range to find active devices.
- **Display IP and MAC Addresses**: Easily view the IP and MAC addresses of devices on the network.
- **Error Handling**: Validates IP address input and provides usage instructions if the input is invalid.
- **Cross-platform**: The script works on Linux and macOS.

## Prerequisites

Before using the script, make sure you have the following:

- **Python**: Ensure you have Python 3.x installed.
- **Administrator/Sudo Privileges**: Scanning networks may require elevated privileges.
- **Linux or macOS**: The script uses `scapy`, which is compatible with Unix-like systems.

## Installation

### Clone the repository

First, clone the repository to your local machine:

 ```bash
 git clone https://github.com/Esammansour883/network-scanner.git
 cd network-scanner
```

### Install Dependencies

This script uses Python’s scapy and argparse libraries. You can install scapy using pip if it’s not already installed:

 ```bash
pip install scapy
 ```

## Usage

To scan a network and list connected devices, run the script with the following command:

 ```bash
python network_scanner.py -i <IP_ADDRESS_RANGE>
 ```

Where:
- <IP_ADDRESS_RANGE>: The IP address range to scan (e.g., 192.168.1.1/24)

### Example:

 ```bash
 python network_scanner.py -i 192.168.1.1/24
 ```


## How It Works

- The script first checks whether the provided IP address range is valid.
- It sends ARP requests to the specified IP address range to discover active devices.
- The script then collects the IP and MAC addresses of the responding devices and displays them.

## Enhancements and Use Cases

- **Network Administration: Useful for administrators to monitor and manage network devices.
- **Security Assessments: Can be used to identify unauthorized devices on the network.
- **Testing and Troubleshooting: Helps in testing network configurations and identifying connectivity issues.

## Limitations

- **Windows Compatibility: This script is primarily designed for Unix-like systems. Modifications may be needed for compatibility with Windows.
- **Network Adapter Support: Performance and compatibility may vary depending on the network adapter and hardware used.
- 
## License

This project is licensed under the MIT License - see the LICENSE file for details.


## Author

Created by Essam Mansour.
