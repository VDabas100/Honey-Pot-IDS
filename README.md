# Honeypot Intrusion Detection System

This project is a Python Based Honeypot IDS designed to simulate a fake system that listens on multiple ports, detects incoming attack attempts, and logs them while providing fake responses. This project is useful for testing and simulating attack detection.

### Features:
- Simulates multiple service ports (FTP, SSH, HTTP, etc.)
- Logs attack attempts with detailed information
- Provides fake responses to intruders
- Visual feedback and dynamic progress bar during attack simulations

### Technologies Used:
- Python 3.x
- `pyfiglet` for banner display
- `termcolor` for colored output
- `tqdm` for progress bars
- Socket Programming for network communication
- Logging for attack and event tracking

## Installation:

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/honeypot-ids.git
   cd honeypot-ids

# Requirements:

- Python 3.x
- Libraries: pyfiglet, tqdm, termcolor

# Usage:

The honeypot listens on a set of predefined ports.
When an attack is detected, it logs the attack and sends a fake response.
The honeypot.log file will record details such as the attacker's IP and the port they attempted to access.
